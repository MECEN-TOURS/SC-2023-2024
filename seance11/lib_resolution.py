"""Description.

Résolution du problème de flot maximal
On utilise en entrée des graphes décrit par table de correspondance
On se ramène à un programme linéaire
"""
from lib_graphe import Table
from scipy.optimize import linprog
import numpy as np


def genere_bounds(table: Table) -> list[tuple[float, float | None]]:
    resultat = list()
    for depart in table:
        for _, poids in table[depart].items():
            if poids == float("inf"):
                resultat.append((0, None))
            else:
                resultat.append((0, poids))
    return resultat


def genere_c(table: Table) -> np.ndarray:
    resultat = list()
    for depart in table:
        for arrivee, _ in table[depart].items():
            if arrivee == "sortie":
                resultat.append(-1)
            else:
                resultat.append(0)
    return np.array(resultat)


def genere_Aeq(table: Table) -> np.ndarray:
    # calcul des dimensions de la matrice
    nb_lignes, = genere_beq(table).shape
    nb_colonnes, = genere_c(table).shape
    resultat = np.zeros(shape=(nb_lignes, nb_colonnes))
    # génération d'un index de ligne pour les sommets internes
    indice_ligne = dict()
    compteur = 0
    for depart in table:
        if depart not in indice_ligne and depart not in {"entree", "sortie"}:
            indice_ligne[depart] = compteur
            compteur += 1
        for arrivee in table[depart]:
            if arrivee not in indice_ligne and arrivee not in {"entree", "sortie"}:
                indice_ligne[arrivee] = compteur
                compteur += 1
    # remplissage de la matrice à partir des index calcules
    indice_colonne = 0
    for depart in table:
        for arrivee in table[depart]:
            if depart not in {"entree", "sortie"}:
                resultat[indice_ligne[depart], indice_colonne] = -1
            if arrivee not in {"entree", "sortie"}:
                resultat[indice_ligne[arrivee], indice_colonne] = 1
            indice_colonne += 1
    return resultat


def genere_beq(table: Table) -> np.ndarray:
    sommets = set()
    for depart in table:
        sommets.add(depart)
        for arrivee in table[depart]:
            sommets.add(arrivee)
    sommets.discard("entree")
    sommets.discard("sortie")
    return np.zeros(shape=(len(sommets), ))


def calcule_flot_max(table: Table) -> Table:
    solution = linprog(
        c=genere_c(table),
        A_eq=genere_Aeq(table),
        b_eq=genere_beq(table),
        bounds=genere_bounds(table),
    )
    resultat = dict()
    debits = iter(solution.x)
    for depart in table:
        resultat[depart] = dict()
        for arrivee in table[depart]:
            resultat[depart][arrivee] = next(debits)
    return Table(resultat)
