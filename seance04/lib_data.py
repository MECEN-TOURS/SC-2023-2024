"""Description.

Implémentation de structure de données représentant les grilles de sudoku.
"""
from enum import Enum
from dataclasses import dataclass


class Case(Enum):
    UN = "1"
    DEUX = "2"
    TROIS = "3"
    QUATRE = "4"
    VIDE = " "


@dataclass
class Grille:
    cases: list[Case]

    def __post_init__(self):
        if len(self.cases) != 16:
            raise ValueError("Une grille a exactement 16 éléments!")


def verifie_lignes(grille: Grille) -> bool:
    for ligne in [grille.cases[i:i+4] for i in (0, 4, 8, 12)]:
        vus = set()
        for case in ligne:
            if case != Case.VIDE:
                if case in vus:
                    return False
                else:
                    vus.add(case)
    return True


def verifie_colonnes(grille: Grille) -> bool:
    for colonne in [grille.cases[i::4] for i in (0, 1, 2, 3)]:
        vus = set()
        for case in colonne:
            if case != Case.VIDE:
                if case in vus:
                    return False
                else:
                    vus.add(case)
    return True


def verifie_interne(grille: Grille) -> bool:
    for interne in [[grille.cases[i + j] for i in (0, 1, 4, 5)] for j in (0, 2, 8, 10)]:
        vus = set()
        for case in interne:
            if case != Case.VIDE:
                if case in vus:
                    return False
                else:
                    vus.add(case)
    return True


def genere_voisins(grille: Grille) -> list[Grille]:
    ...
