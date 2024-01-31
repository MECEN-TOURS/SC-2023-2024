"""Description.

Tests pour le module lib_data.py
"""
from lib_data import (
    Case,
    Grille,
    verifie_lignes,
    verifie_colonnes,
    verifie_interne,
    detecte_doublon,
    genere_voisins,
    renvoie_premiere_case_vide,
    resolution,
    itere_voisins,
)
import pytest


def test_initialisation():
    essai = Grille(cases=[Case.UN for _ in range(16)])
    assert isinstance(essai, Grille)
    with pytest.raises(ValueError):
        essai = Grille(cases=[Case.UN for _ in range(15)])
    with pytest.raises(ValueError):
        essai = Grille(cases=[Case.UN for _ in range(17)])


def test_constructeur():
    attendue = Grille(
        cases=[
            Case.UN,
            Case.DEUX,
            Case.VIDE,
            Case.QUATRE,
            Case.QUATRE,
            Case.VIDE,
            Case.UN,
            Case.DEUX,
            Case.VIDE,
            Case.QUATRE,
            Case.VIDE,
            Case.VIDE,
            Case.VIDE,
            Case.VIDE,
            Case.VIDE,
            Case.UN,
        ]
    )
    calculee1 = Grille.from_str("12X4\n4X12\nX4XX\nXXX1")
    assert calculee1 == attendue
    calculee2 = Grille.from_str("12X4 \n  4X12\nX4 XX\nXX X1")
    assert calculee2 == attendue
    calculee3 = Grille.from_str("\n12X4 \n4X12\nX4XX  \nXXX1\n")
    assert calculee3 == attendue
    with pytest.raises(ValueError):
        Grille.from_str("12 4\n4X12\nX4XX\nXXX1")


def test_detecte_doublons():
    assert detecte_doublon(cases=[Case.UN, Case.UN])
    assert detecte_doublon(cases=[Case.DEUX, Case.DEUX])
    assert detecte_doublon(cases=[Case.TROIS, Case.TROIS])
    assert detecte_doublon(cases=[Case.QUATRE, Case.QUATRE])
    assert not detecte_doublon(cases=[])
    assert not detecte_doublon(cases=[Case.VIDE, Case.VIDE])
    assert not detecte_doublon(cases=[Case.VIDE, Case.UN])
    assert not detecte_doublon(cases=[case for case in Case])


def test_verifie_lignes():
    correct = Grille(cases=[Case.VIDE for _ in range(16)])
    assert verifie_lignes(correct)

    problematique1 = Grille(
        cases=[Case.UN if indice in {0, 1}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_lignes(problematique1)

    problematique2 = Grille(
        cases=[Case.DEUX if indice in {4, 5}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_lignes(problematique2)

    problematique3 = Grille(
        cases=[Case.TROIS if indice in {8, 9}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_lignes(problematique3)

    problematique4 = Grille(
        cases=[Case.QUATRE if indice in {12, 13}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_lignes(problematique4)


def test_verifie_interne():
    correct = Grille(cases=[Case.VIDE for _ in range(16)])
    assert verifie_interne(correct)

    problematique1 = Grille(
        cases=[Case.UN if indice in {0, 4}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_interne(problematique1)

    problematique2 = Grille(
        cases=[Case.DEUX if indice in {3, 7}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_interne(problematique2)

    problematique3 = Grille(
        cases=[Case.TROIS if indice in {9, 12}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_interne(problematique3)

    problematique4 = Grille(
        cases=[Case.QUATRE if indice in {10, 15}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_interne(problematique4)


def test_verifie_colonnes():
    correct = Grille(cases=[Case.VIDE for _ in range(16)])
    assert verifie_colonnes(correct)

    problematique1 = Grille(
        cases=[Case.UN if indice in {0, 4}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_colonnes(problematique1)

    problematique2 = Grille(
        cases=[Case.DEUX if indice in {5, 9}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_colonnes(problematique2)

    problematique3 = Grille(
        cases=[Case.TROIS if indice in {10, 14}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_colonnes(problematique3)

    problematique4 = Grille(
        cases=[Case.QUATRE if indice in {3, 15}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_colonnes(problematique4)


def test_premiere_case_vide():
    assert 5 == renvoie_premiere_case_vide(
        grille=Grille.from_str("12144X12X4XXXXX1"))
    problematique = Grille.from_str("1214411214111111")
    with pytest.raises(ValueError):
        renvoie_premiere_case_vide(grille=problematique)


def test_genere_voisins():
    depart = Grille.from_str(
        """
12X4
4X12
X4XX
XXX1
        """
    )
    assert genere_voisins(grille=depart) == [
        Grille.from_str("12144X12X4XXXXX1"),
        Grille.from_str("12244X12X4XXXXX1"),
        Grille.from_str("12344X12X4XXXXX1"),
        Grille.from_str("12444X12X4XXXXX1"),
    ]
    depart = Grille.from_str(
        """
1234
4312
3421
2134
        """
    )
    assert genere_voisins(grille=depart) == []


def test_resolution_completes():
    valide = Grille.from_str("1234" "3412" "2143" "4321")
    assert resolution(grille=valide) == [valide]
    invalide = Grille.from_str("1234" "3412" "2113" "4321")
    assert resolution(grille=invalide) == []


def test_resolution_simple():
    valide = Grille.from_str("1234" "3412" "21X3" "4321")
    assert resolution(grille=valide) == [
        Grille.from_str("1234" "3412" "2143" "4321")]


def test_resolution():
    valide = Grille.from_str("1XX4" "X4X2" "21X3" "XX2X")
    assert resolution(grille=valide) == [
        Grille.from_str("1234" "3412" "2143" "4321")]


def test_itere_voisins():
    depart = Grille.from_str("12X4" "4X12" "X4XX" "XXX1")
    it = iter(itere_voisins(depart))
    assert next(it) == Grille.from_str("1214" "4X12" "X4XX" "XXX1")
    assert next(it) == Grille.from_str("1224" "4X12" "X4XX" "XXX1")
    assert next(it) == Grille.from_str("1234" "4X12" "X4XX" "XXX1")
    assert next(it) == Grille.from_str("1244" "4X12" "X4XX" "XXX1")
    with pytest.raises(StopIteration):
        next(it)


def test_resolution_efficace():
    ...
