"""Description.

Implémentation de structure de données représentant les grilles de sudoku.
"""
from enum import Enum
from dataclasses import dataclass
from typing import Generator


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

    @classmethod
    def from_str(cls, caracteres: str) -> "Grille":
        cases = list()
        for ligne in caracteres:
            for caractere in ligne:
                if caractere == "1":
                    cases.append(Case.UN)
                elif caractere == "2":
                    cases.append(Case.DEUX)
                elif caractere == "3":
                    cases.append(Case.TROIS)
                elif caractere == "4":
                    cases.append(Case.QUATRE)
                elif caractere == "X":
                    cases.append(Case.VIDE)
        return Grille(cases=cases)


def detecte_doublon(cases: list[Case]) -> bool:
    vus = set()
    for case in cases:
        if case != Case.VIDE:
            if case in vus:
                return True
            else:
                vus.add(case)
    return False


def verifie_lignes(grille: Grille) -> bool:
    for ligne in [[grille.cases[i + j] for i in (0, 1, 2, 3)] for j in (0, 4, 8, 12)]:
        if detecte_doublon(ligne):
            return False
    return True


def verifie_colonnes(grille: Grille) -> bool:
    for colonne in [[grille.cases[i + j] for i in (0, 4, 8, 12)] for j in (0, 1, 2, 3)]:
        if detecte_doublon(colonne):
            return False
    return True


def verifie_interne(grille: Grille) -> bool:
    for interne in [[grille.cases[i + j] for i in (0, 1, 4, 5)] for j in (0, 2, 8, 10)]:
        if detecte_doublon(interne):
            return False
    return True


def renvoie_premiere_case_vide(grille: Grille) -> int:
    for indice, case in enumerate(grille.cases):
        if case == Case.VIDE:
            return indice
    raise ValueError("Pas de case vide!")


def genere_voisins(grille: Grille) -> list[Grille]:
    try:
        a_remplir = renvoie_premiere_case_vide(grille)
    except ValueError:
        return []
    resultat = list()
    for choix in (Case.UN, Case.DEUX, Case.TROIS, Case.QUATRE):
        resultat.append(
            Grille(
                cases=[
                    choix if indice == a_remplir else case
                    for (indice, case) in enumerate(grille.cases)
                ]
            )
        )
    return resultat


def resolution(grille: Grille) -> list[Grille]:
    voisins = genere_voisins(grille)
    if voisins == []:
        if (
            verifie_colonnes(grille)
            and verifie_lignes(grille)
            and verifie_interne(grille)
        ):
            return [grille]
        else:
            return []
    resultat = list()
    for voisin in voisins:
        if (
            verifie_colonnes(voisin)
            and verifie_lignes(voisin)
            and verifie_interne(voisin)
        ):
            resultat.extend(resolution(grille=voisin))
    return resultat


def itere_voisins(grille: Grille) -> Generator[Grille, None, None]:
    ...


def resolution_efficace(grille: Grille) -> Generator[Grille, None, None]:
    ...
