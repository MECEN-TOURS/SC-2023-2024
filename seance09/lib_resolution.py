"""Description.

Librairie permettant de résoudre le problème de flot maximal en s'appuyant sur scipy
"""

from scipy.optimize import linprog
from lib_graphe import Arretes
import numpy as np


class GrapheInvalide(Exception):
    pass


def genere_c(arretes: Arretes) -> np.ndarray:
    return np.array([-1 if arrivee == "sortie" else 0 for (_, arrivee, _) in arretes])


def genere_bounds(arretes: Arretes) -> list[tuple[float, float | None]]:
    resultat = list()
    for _, _, poids in arretes:
        if poids == float("inf"):
            resultat.append((0, None))
        else:
            resultat.append((0, poids))
    return resultat


def genere_indices_lignes(arretes: Arretes) -> dict[str, int]:
    resultat = dict()
    indice_courant = 0
    for depart, arrivee, poids in arretes:
        if depart not in resultat and depart not in {"entree", "sortie"}:
            resultat[depart] = indice_courant
            indice_courant += 1
        if arrivee not in resultat and arrivee not in {"entree", "sortie"}:
            resultat[arrivee] = indice_courant
            indice_courant += 1

    return resultat


def genere_Aeq(arretes: Arretes) -> np.ndarray:
    indices_lignes = genere_indices_lignes(arretes)
    resultat = np.zeros(shape=(len(indices_lignes), len(arretes)))
    for j, (depart, arrivee, _) in enumerate(arretes):
        if depart not in {"entree", "sortie"}:
            resultat[indices_lignes[depart], j] = -1
        if arrivee not in {"entree", "sortie"}:
            resultat[indices_lignes[arrivee], j] = 1
    return resultat


def genere_beq(arretes: Arretes) -> np.ndarray:
    return np.zeros(shape=(len(genere_indices_lignes(arretes)), ))


def resolution(arretes: Arretes) -> Arretes:
    entree_vue = False
    sortie_vue = False
    for (depart, arrivee, poids) in arretes:
        if poids < 0:
            raise GrapheInvalide("Les poids doivent etre positifs!")
        if depart == "entree":
            entree_vue = True
        if arrivee == "sortie":
            sortie_vue = True
    if (not entree_vue):
        raise GrapheInvalide("Il faut une entrée")
    if (not sortie_vue):
        raise GrapheInvalide("Il faut une sortie")

    solution = linprog(
        c=genere_c(arretes),
        A_eq=genere_Aeq(arretes),
        b_eq=genere_beq(arretes),
        bounds=genere_bounds(arretes)
    )
    return Arretes(
        [(depart, arrivee, debit)
         for ((depart, arrivee, _), debit) in zip(arretes, solution.x)]
    )
