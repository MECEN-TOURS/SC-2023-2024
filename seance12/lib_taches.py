"""Description.

Datastructure représentant les cahiers des charges.
Fonction créant le graphe à partir d'un cahier des charges.
"""
from dataclasses import dataclass
from typing import Generator, NewType


@dataclass
class Tache:
    nom: str
    duree: float
    prerequis: list[str]

    def __post_init__(self):
        if self.duree < 0 or self.duree == float("inf"):
            raise ValueError(f"La tache {self} n'est pas valide.")


@dataclass
class CahierDesCharges:
    taches: list[Tache]

    def __post_init__(self):
        noms = set(tache.nom for tache in self.taches)
        for tache in self.taches:
            for prerequis in tache.prerequis:
                if prerequis not in noms:
                    raise ValueError("{prerequis} n'est pas une tache valide")

    def __getitem__(self, nom_tache: str) -> Tache:
        for tache in self.taches:
            if tache.nom == nom_tache:
                return tache
        raise KeyError(f"{nom_tache} n'est pas une tache valide")


Arrete = NewType("Arrete", tuple[Tache, Tache, float])
Graphe = NewType("Graphe", list[Arrete])


def cahier_to_graphe(cahier: CahierDesCharges) -> Graphe:
    resultat = list()
    for tache in cahier.taches:
        for prerequis in tache.prerequis:
            resultat.append(
                Arrete((cahier[prerequis], tache, cahier[prerequis].duree)))
    return Graphe(resultat)


def idenfie_sans_prerequis(cahier: CahierDesCharges) -> Generator[Tache, None, None]:
    for tache in cahier.taches:
        if tache.prerequis == []:
            yield tache


def elaguage(cahier: CahierDesCharges) -> CahierDesCharges:
    it = iter(idenfie_sans_prerequis(cahier))
    try:
        a_elaguer = next(it)
    except StopIteration:
        return cahier
    nouvelles_taches = list()
    for tache_courante in cahier.taches:
        if tache_courante != a_elaguer:
            nouvelles_taches.append(
                Tache(
                    nom=tache_courante.nom,
                    duree=tache_courante.duree,
                    prerequis=[
                        prerequis
                        for prerequis in tache_courante.prerequis
                        if prerequis != a_elaguer.nom
                    ],
                )
            )
    return CahierDesCharges(taches=nouvelles_taches)


def tri_topologique(cahier: CahierDesCharges) -> list[Tache]:
    ...
