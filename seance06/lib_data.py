#!--coding: utf8 --
"""Description.

Module fournissant des fonctionnalités de résolution d'un sudoku 4x4
"""
from enum import Enum
from dataclasses import dataclass
from typing import Generator


class GrilleComplete(Exception):
    """Exception représentant la présence d'une grille sans case vide"""
    pass


class Case(Enum):
    """Type représentant les 5 valeurs d'une grille incomplète"""
    UN = "1"
    DEUX = "2"
    TROIS = "3"
    QUATRE = "4"
    VIDE = " "


@dataclass
class Grille:
    """Classe permettant de représenter une grille de Sudoku partiellement remplie

    Exemples:
    >>> Grille(
...         cases=[
...             Case.UN,
...             Case.DEUX,
...             Case.VIDE,
...             Case.QUATRE,
...             Case.QUATRE,
...             Case.VIDE,
...             Case.UN,
...             Case.DEUX,
...             Case.VIDE,
...             Case.QUATRE,
...             Case.VIDE,
...             Case.VIDE,
...             Case.VIDE,
...             Case.VIDE,
...             Case.VIDE,
...             Case.UN,
...         ]
...     )
Grille(cases=[<Case.UN: '1'>, <Case.DEUX: '2'>, <Case.VIDE: ' '>, <Case.QUATRE: '4'>, <Case.QUATRE: '4'>, <Case.VIDE: ' '>, <Case.UN: '1'>, <Case.DEUX: '2'>, <Case.VIDE: ' '>, <Case.QUATRE: '4'>, <Case.VIDE: ' '>, <Case.VIDE: ' '>, <Case.VIDE: ' '>, <Case.VIDE: ' '>, <Case.VIDE: ' '>, <Case.UN: '1'>])
    >>> Grille.from_str("1234" "3X12" "214X" "X321")
Grille(cases=[<Case.UN: '1'>, <Case.DEUX: '2'>, <Case.TROIS: '3'>, <Case.QUATRE: '4'>, <Case.TROIS: '3'>, <Case.VIDE: ' '>, <Case.UN: '1'>, <Case.DEUX: '2'>, <Case.DEUX: '2'>, <Case.UN: '1'>, <Case.QUATRE: '4'>, <Case.VIDE: ' '>, <Case.VIDE: ' '>, <Case.TROIS: '3'>, <Case.DEUX: '2'>, <Case.UN: '1'>])
    >>> print(Grille.from_str("1234" "3X12" "214X" "X321"))
1234
3 12
214 
 321
    >>> Grille.from_str("1234" "3X12" "214X" " 321")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ValueError: Une grille a exactement 16 éléments!
    """
    cases: list[Case]

    def __post_init__(self):
        """On vérifie qu'il n'y a que 16 éléments, ce qui ne se voit pas dans la signature"""
        if len(self.cases) != 16:
            raise ValueError("Une grille a exactement 16 éléments!")

    def __str__(self) -> str:
        caracteres = list()
        for indice, case in enumerate(self.cases):
            if indice in {4, 8, 12}:
                caracteres.append("\n")
            if case == Case.UN:
                caracteres.append("1")
            elif case == Case.DEUX:
                caracteres.append("2")
            elif case == Case.TROIS:
                caracteres.append("3")
            elif case == Case.QUATRE:
                caracteres.append("4")
            elif case == Case.VIDE:
                caracteres.append(" ")
        return "".join(caracteres)

    @classmethod
    def from_str(cls, caracteres: str) -> "Grille":
        """Constructeur alternatif plus concis pour créer une grille"""
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


def _detecte_doublon(cases: list[Case]) -> bool:
    """Détecte si deux cases non vides sont répétées dans la liste"""
    vus = set()
    for case in cases:
        if case != Case.VIDE:
            if case in vus:
                return True
            else:
                vus.add(case)
    return False


def _verifie_lignes(grille: Grille) -> bool:
    """Vérifie qu'il n'y a pas de répétion de 1, 2, 3, ou 4 sur aucune ligne de la grille"""
    for ligne in [[grille.cases[i + j] for i in (0, 1, 2, 3)] for j in (0, 4, 8, 12)]:
        if _detecte_doublon(ligne):
            return False
    return True


def _verifie_colonnes(grille: Grille) -> bool:
    """Vérifie qu'il n'y a pas de répétion de 1, 2, 3, ou 4 sur aucune colonne de la grille"""
    for colonne in [[grille.cases[i + j] for i in (0, 4, 8, 12)] for j in (0, 1, 2, 3)]:
        if _detecte_doublon(colonne):
            return False
    return True


def _verifie_interne(grille: Grille) -> bool:
    """Vérifie qu'il n'y a pas de répétion de 1, 2, 3, ou 4 sur aucune sous-grille de la grille"""
    for interne in [[grille.cases[i + j] for i in (0, 1, 4, 5)] for j in (0, 2, 8, 10)]:
        if _detecte_doublon(interne):
            return False
    return True


def est_valide(grille: Grille) -> bool:
    """Vérifie que la grille respecte les trois règles"""
    return _verifie_colonnes(grille) and _verifie_lignes(grille) and _verifie_interne(grille)


def _renvoie_premiere_case_vide(grille: Grille) -> int:
    """Renvoie l'indice de la première case vide ou génère GrilleComplete"""
    for indice, case in enumerate(grille.cases):
        if case == Case.VIDE:
            return indice
    raise GrilleComplete("Pas de case vide!")


def _itere_voisins(grille: Grille) -> Generator[Grille, None, None]:
    """Permet d'itérer sur les grilles avec la première case vide remplie de quatre façons"""
    indice = _renvoie_premiere_case_vide(grille)
    for valeur in (Case.UN, Case.DEUX, Case.TROIS, Case.QUATRE):
        yield Grille(cases=[valeur if i == indice else case for i, case in enumerate(grille.cases)])


def resolution(grille: Grille) -> Generator[Grille, None, None]:
    """Permet d'itérer sur les solutions associées à la grille d'entrée"""
    try:
        for voisin in _itere_voisins(grille):
            if est_valide(grille):
                for solution in resolution(voisin):
                    yield solution
    except GrilleComplete:
        if est_valide(grille):
            yield grille
