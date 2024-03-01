"""Description.

Datastructure représentant les cahiers des charges.
Fonction créant le graphe à partir d'un cahier des charges.
"""

from dataclasses import dataclass
from typing import NewType
from serde import serde  # type: ignore


@serde
@dataclass(frozen=True, unsafe_hash=True)
class Tache:
    """Représente une tache

    nom: nom de la tache
    duree: durée de la tache, doit etre un float positif et fini!
    prerequis: liste des noms des taches qui doivent etre complétées
               avant de commencer la tache courante

    Exemple:
    >>> Tache(nom="A", duree=1., prerequis=frozenset(["J", "E"]))
    Tache(nom='A', duree=1.0, prerequis=frozenset({'J', 'E'}))
    >>> Tache(nom="A", duree=-1., prerequis=frozenset(["J", "E"]))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<string>", line 6, in __init__
        raise ValueError(f"La tache {self} n'est pas valide.")
    ValueError: La tache Tache(nom='A', duree=-1.0, prerequis=frozenset({'J', 'E'})) n'est pas valide.
    >>> Tache(nom="A", duree=float("inf"), prerequis=frozenset(["J", "E"]))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<string>", line 6, in __init__
        raise ValueError(f"La tache {self} n'est pas valide.")
    ValueError: La tache Tache(nom='A', duree=inf, prerequis=frozenset({'J', 'E'})) n'est pas valide.
    """

    nom: str
    duree: float
    prerequis: frozenset[str]

    def __post_init__(self):
        """Vérifie la validité de la durée"""
        if self.duree < 0 or self.duree == float("inf"):
            raise ValueError(f"La tache {self} n'est pas valide.")


@serde
@dataclass
class CahierDesCharges:
    """Liste de taches avec des outils de manipulation

    On vérifie que les prérequis de chaque tache sont des noms de tache valides

    Exemples:
    >>> CahierDesCharges(
    ...         taches=[
    ...             Tache(nom="A", duree=1., prerequis=frozenset(["B"])),
    ...             Tache(nom="B", duree=2., prerequis=frozenset([])),
    ...         ]
    ...     )
    CahierDesCharges(taches=[Tache(nom='A', duree=1.0, prerequis=frozenset({'B'})), Tache(nom='B', duree=2.0, prerequis=frozenset())])
    >>> CahierDesCharges(
    ...             taches=[
    ...                 Tache(nom="A", duree=1., prerequis=frozenset(["J", "E"])),
    ...                 Tache(nom="B", duree=2., prerequis=frozenset(["C", "E"])),
    ...             ]
    ...         )
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<string>", line 4, in __init__
        raise ValueError("{prerequis} n'est pas une tache valide")
    ValueError: {prerequis} n'est pas une tache valide
    >>> cahier = CahierDesCharges(
    ...         taches=[
    ...             Tache(nom="A", duree=1., prerequis=frozenset(["B"])),
    ...             Tache(nom="B", duree=2., prerequis=frozenset(["C"])),
    ...             Tache(nom="C", duree=3., prerequis=frozenset(["A"])),
    ...         ]
    ...     )
    >>> cahier["A"]
    Tache(nom='A', duree=1.0, prerequis=frozenset({'B'}))
    >>> cahier["D"]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
        File "<string>", line 4, in __init__
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    KeyError: "D n'est pas une tache valide"
    """

    taches: list[Tache]

    def __post_init__(self):
        """Vérifie la validité des noms de prérequis"""
        noms = set(tache.nom for tache in self.taches)
        for tache in self.taches:
            for prerequis in tache.prerequis:
                if prerequis not in noms:
                    raise ValueError(f"{prerequis} n'est pas une tache valide")

    def __getitem__(self, nom_tache: str) -> Tache:
        """Permet d'accéder à une tache à partir de son nom"""
        for tache in self.taches:
            if tache.nom == nom_tache:
                return tache
        raise KeyError(f"{nom_tache} n'est pas une tache valide")


def _tri_topologique(cahier: CahierDesCharges) -> list[Tache]:
    """Ordonne les taches linéairement

    On produit une liste où les prérequis d'une tache apparaisse avant celle-ci
    Génère ValueError si un tel ordonnancement n'existe pas.
    """
    resultat = list()
    completees = {tache: False for tache in cahier.taches}
    while True:
        elagage_utile = False
        for tache in cahier.taches:
            if not completees[tache] and all(
                completees[cahier[prerequis]] for prerequis in tache.prerequis
            ):
                resultat.append(tache)
                completees[tache] = True
                elagage_utile = True
        if all(completees.values()):
            return resultat
        if not elagage_utile:
            raise ValueError("Le cahier des charges est insolvable!")


@serde
@dataclass
class Intervalle:
    """Représente une plage d'exécution d'une tache

    Vérifie que la fin est après le début sinon génère ValueError!

    Exemples:
    >>> Intervalle(debut=1., fin=2.)
    Intervalle(debut=1.0, fin=2.0)
    >>> Intervalle(debut=1., fin=0.)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<string>", line 5, in __init__

    ValueError: debut doit etre plus petit que fin!
    """

    debut: float
    fin: float

    def __post_init__(self):
        """Vérifie que la fin est après le début"""
        if self.debut > self.fin:
            raise ValueError("debut doit etre plus petit que fin!")


Planning = NewType("Planning", dict[Tache, Intervalle])


def calcule_chronologie(cahier: CahierDesCharges) -> Planning:
    """Créé un planning le plus serré possible satisfaisant le cahier des charges

    Génère ValueError si aucun planning n'existe!

    Exemples:
    >>> calcule_chronologie(
    ...         CahierDesCharges(
    ...             taches=[
    ...                 Tache(nom="A", duree=1., prerequis=frozenset(["J", "E"])),
    ...                 Tache(nom="B", duree=2., prerequis=frozenset(["C", "E"])),
    ...                 Tache(nom="C", duree=3., prerequis=frozenset(["E"])),
    ...                 Tache(nom="D", duree=4., prerequis=frozenset(["B", "A"])),
    ...                 Tache(nom="E", duree=3., prerequis=frozenset([])),
    ...                 Tache(nom="F", duree=2., prerequis=frozenset(["A"])),
    ...                 Tache(nom="G", duree=1., prerequis=frozenset(["B"])),
    ...                 Tache(nom="H", duree=2., prerequis=frozenset(["C"])),
    ...                 Tache(nom="I", duree=3., prerequis=frozenset(["F"])),
    ...                 Tache(nom="J", duree=4., prerequis=frozenset(["E"])),
    ...             ]
    ...         )
    ...     )
        {
            Tache(nom='E', duree=3.0, prerequis=frozenset()): Intervalle(debut=0.0, fin=3.0),
            Tache(nom='J', duree=4.0, prerequis=frozenset({'E'})): Intervalle(debut=3.0, fin=7.0),
            Tache(nom='A', duree=1.0, prerequis=frozenset({'J', 'E'})): Intervalle(debut=7.0, fin=8.0),
            Tache(nom='C', duree=3.0, prerequis=frozenset({'E'})): Intervalle(debut=3.0, fin=6.0),
            Tache(nom='F', duree=2.0, prerequis=frozenset({'A'})): Intervalle(debut=8.0, fin=10.0),
            Tache(nom='H', duree=2.0, prerequis=frozenset({'C'})): Intervalle(debut=6.0, fin=8.0),
            Tache(nom='I', duree=3.0, prerequis=frozenset({'F'})): Intervalle(debut=10.0, fin=13.0),
            Tache(nom='B', duree=2.0, prerequis=frozenset({'C', 'E'})): Intervalle(debut=6.0, fin=8.0),
            Tache(nom='D', duree=4.0, prerequis=frozenset({'B', 'A'})): Intervalle(debut=8.0, fin=12.0),
            Tache(nom='G', duree=1.0, prerequis=frozenset({'B'})): Intervalle(debut=8.0, fin=9.0),
        }
    """
    ordre = _tri_topologique(cahier)
    resultat = Planning({})
    for tache in ordre:
        debut = (
            0.0
            if not tache.prerequis
            else max(resultat[cahier[prerequis]].fin for prerequis in tache.prerequis)
        )
        resultat[tache] = Intervalle(debut=debut, fin=debut + tache.duree)
    return resultat
