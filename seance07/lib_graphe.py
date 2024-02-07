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
                raise ValueError("Les pondérations des arrêtes doivent être positives!")
            if depart not in self.sommets:
                raise ValueError(f"{depart=} n'est pas dans la liste des sommets!")
            if arrivee not in self.sommets:
                raise ValueError(f"{arrivee=} n'est pas dans la liste des sommets!")


def itere_distance(
    graphe: Graphe, distance: dict[str, float], cible: str
) -> dict[str, float]:
    resultat = dict()
    for sommet_courant in graphe.sommets:
        try:
            resultat[sommet_courant] = min(
                poids + distance[arrivee]
                for depart, arrivee, poids in graphe.arretes
                if depart == sommet_courant
            )
        except KeyError:
            raise ValueError("La distance n'est pas valide!")
        except ValueError:
            if sommet_courant == cible:
                resultat[sommet_courant] = 0
            else:
                resultat[sommet_courant] = float("inf")
    return resultat


def calcule_distance(depart: str, arrivee: str, graphe: Graphe) -> float:
    d0 = {sommet: 0 if sommet == arrivee else float("inf") for sommet in graphe.sommets}
    d1 = itere_distance(graphe=graphe, distance=d0, cible=arrivee)
    while d0 != d1:
        d0, d1 = d1, itere_distance(graphe=graphe, distance=d1, cible=arrivee)
    print(d0)
    return d0[depart]


def calcule_chemins_optimaux(depart: str, arrivee: str, graphe: Graphe) -> Generator[list[str], None, None]:
    ...