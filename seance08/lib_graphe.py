"""Description.

Librairie pour manipuler des graphes pondérés. 
"""
from dataclasses import dataclass
from typing import Generator


@dataclass
class Graphe:
    sommets: set[str]
    arretes: list[tuple[str, str, float]]

    def __post_init__(self):
        for depart, arrivee, poids in self.arretes:
            if poids < 0:
                raise ValueError(
                    "Les pondérations des arrêtes doivent être positives!")
            if depart not in self.sommets:
                raise ValueError(
                    f"{depart=} n'est pas dans la liste des sommets!")
            if arrivee not in self.sommets:
                raise ValueError(
                    f"{arrivee=} n'est pas dans la liste des sommets!")


def itere_distance(
    graphe: Graphe, distance: dict[str, float], cible: str
) -> dict[str, float]:
    resultat = dict()
    for sommet_courant in graphe.sommets:
        try:
            if sommet_courant == cible:
                resultat[sommet_courant] = 0.
            else:
                minimum = float("inf")
                for depart, arrivee, poids in graphe.arretes:
                    if depart == sommet_courant:
                        if minimum > poids + distance[arrivee]:
                            minimum = poids + distance[arrivee]
                resultat[sommet_courant] = minimum
        except KeyError:
            raise ValueError("La distance n'est pas valide!")
    return resultat


def calcule_distance(depart: str, arrivee: str, graphe: Graphe) -> float:
    d0 = {sommet: 0 if sommet == arrivee else float(
        "inf") for sommet in graphe.sommets}
    d1 = itere_distance(graphe=graphe, distance=d0, cible=arrivee)
    while d0 != d1:
        d0, d1 = d1, itere_distance(graphe=graphe, distance=d1, cible=arrivee)
    return d0[depart]


def itere_distance_enrichie(
    graphe: Graphe, distance: dict[str, tuple[float, str | None]], cible: str
) -> dict[str, tuple[float, str | None]]:
    resultat = dict()
    for sommet_courant in graphe.sommets:
        try:
            if sommet_courant == cible:
                resultat[sommet_courant] = (0, cible)
            else:
                minimum = float("inf")
                sommet_minimal = None
                for depart, arrivee, poids in graphe.arretes:
                    if depart == sommet_courant:
                        valeur, _ = distance[arrivee]
                        if minimum > poids + valeur:
                            minimum = poids + valeur
                            sommet_minimal = arrivee
                resultat[sommet_courant] = (minimum, sommet_minimal)
        except KeyError:
            raise ValueError("La distance n'est pas valide!")
    return resultat


def calcule_chemin_optimal(depart: str, arrivee: str, graphe: Graphe) -> list[str]:
    d0 = {sommet: (0, arrivee) if sommet == arrivee else (
        float("inf"), None) for sommet in graphe.sommets}
    d1 = itere_distance_enrichie(graphe=graphe, distance=d0, cible=arrivee)
    while d0 != d1:
        d0, d1 = d1, itere_distance_enrichie(
            graphe=graphe, distance=d1, cible=arrivee)
    resultat = [depart]
    while resultat[-1] != arrivee:
        _, suivant = d0[resultat[-1]]
        resultat.append(suivant)
        if suivant is None:
            raise ValueError(f"Pas de chemin entre les {depart} et {arrivee}")
    return resultat


def itere_distance_doublement_enrichie(
    graphe: Graphe, distance: dict[str, tuple[float, list[str]]], cible: str
) -> dict[str, tuple[float, list[str]]]:
    resultat = dict()
    for sommet_courant in graphe.sommets:
        try:
            if sommet_courant == cible:
                resultat[sommet_courant] = (0, [cible])
            else:
                minimum = float("inf")
                sommets_minimaux = []
                for depart, arrivee, poids in graphe.arretes:
                    if depart == sommet_courant:
                        valeur, _ = distance[arrivee]
                        if minimum > poids + valeur:
                            minimum = poids + valeur
                            sommets_minimaux = [arrivee]
                        elif minimum == poids + valeur:
                            sommets_minimaux.append(arrivee)
                resultat[sommet_courant] = (minimum, sommets_minimaux)
        except KeyError:
            raise ValueError("La distance n'est pas valide!")
    return resultat


def calcule_chemins_optimaux(depart: str, arrivee: str, graphe: Graphe) -> Generator[list[str], None, None]:
    d0 = {sommet: (0, [arrivee]) if sommet == arrivee else (
        float("inf"), []) for sommet in graphe.sommets}
    d1 = itere_distance_doublement_enrichie(
        graphe=graphe, distance=d0, cible=arrivee)
    while d0 != d1:
        d0, d1 = d1, itere_distance_doublement_enrichie(
            graphe=graphe, distance=d1, cible=arrivee)

    yield from parcours_distance(depart=depart, arrivee=arrivee, distance=d0)


def parcours_distance(depart: str, arrivee: str, distance: dict[str, tuple[float, list[str]]]) -> Generator[list[str], None, None]:
    if depart == arrivee:
        yield [depart]
    else:
        _, suivants = distance[depart]
        for suivant in suivants:
            for chemin in parcours_distance(depart=suivant, arrivee=arrivee, distance=distance):
                yield [depart] + chemin
