"""Description.

Tests pour le module lib_data.py
"""
from lib_data import (
    Case,
    Grille,
    GrilleComplete,
    _verifie_lignes,
    _verifie_colonnes,
    _verifie_interne,
    _detecte_doublon,
    _renvoie_premiere_case_vide,
    _itere_voisins,
    resolution,
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


def test_grille_str():
    entree = Grille.from_str("1234" "X41X" "2143" "4321")
    assert str(entree) == "1234\n 41 \n2143\n4321"


def test_detecte_doublons():
    assert _detecte_doublon(cases=[Case.UN, Case.UN])
    assert _detecte_doublon(cases=[Case.DEUX, Case.DEUX])
    assert _detecte_doublon(cases=[Case.TROIS, Case.TROIS])
    assert _detecte_doublon(cases=[Case.QUATRE, Case.QUATRE])
    assert not _detecte_doublon(cases=[])
    assert not _detecte_doublon(cases=[Case.VIDE, Case.VIDE])
    assert not _detecte_doublon(cases=[Case.VIDE, Case.UN])
    assert not _detecte_doublon(cases=[case for case in Case])


def test_verifie_lignes():
    correct = Grille(cases=[Case.VIDE for _ in range(16)])
    assert _verifie_lignes(correct)

    problematique1 = Grille(
        cases=[Case.UN if indice in {0, 1}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_lignes(problematique1)

    problematique2 = Grille(
        cases=[Case.DEUX if indice in {4, 5}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_lignes(problematique2)

    problematique3 = Grille(
        cases=[Case.TROIS if indice in {8, 9}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_lignes(problematique3)

    problematique4 = Grille(
        cases=[Case.QUATRE if indice in {12, 13}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_lignes(problematique4)


def test_verifie_interne():
    correct = Grille(cases=[Case.VIDE for _ in range(16)])
    assert _verifie_interne(correct)

    problematique1 = Grille(
        cases=[Case.UN if indice in {0, 4}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_interne(problematique1)

    problematique2 = Grille(
        cases=[Case.DEUX if indice in {3, 7}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_interne(problematique2)

    problematique3 = Grille(
        cases=[Case.TROIS if indice in {9, 12}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_interne(problematique3)

    problematique4 = Grille(
        cases=[Case.QUATRE if indice in {10, 15}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_interne(problematique4)


def test_verifie_colonnes():
    correct = Grille(cases=[Case.VIDE for _ in range(16)])
    assert _verifie_colonnes(correct)

    problematique1 = Grille(
        cases=[Case.UN if indice in {0, 4}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_colonnes(problematique1)

    problematique2 = Grille(
        cases=[Case.DEUX if indice in {5, 9}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_colonnes(problematique2)

    problematique3 = Grille(
        cases=[Case.TROIS if indice in {10, 14}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_colonnes(problematique3)

    problematique4 = Grille(
        cases=[Case.QUATRE if indice in {3, 15}
               else Case.VIDE for indice in range(16)]
    )
    assert not _verifie_colonnes(problematique4)


def test_premiere_case_vide():
    assert 5 == _renvoie_premiere_case_vide(
        grille=Grille.from_str("12144X12X4XXXXX1"))
    problematique = Grille.from_str("1214411214111111")
    with pytest.raises(GrilleComplete):
        _renvoie_premiere_case_vide(grille=problematique)


def test_itere_voisins():
    depart = Grille.from_str("12X4" "4X12" "X4XX" "XXX1")
    it = iter(_itere_voisins(depart))
    assert next(it) == Grille.from_str("1214" "4X12" "X4XX" "XXX1")
    assert next(it) == Grille.from_str("1224" "4X12" "X4XX" "XXX1")
    assert next(it) == Grille.from_str("1234" "4X12" "X4XX" "XXX1")
    assert next(it) == Grille.from_str("1244" "4X12" "X4XX" "XXX1")
    with pytest.raises(StopIteration):
        next(it)


def test_resolution_simple():
    attendu = Grille.from_str("1234" "3412" "2143" "4321")
    entree = Grille.from_str("X234" "3412" "2143" "4321")
    it = iter(resolution(entree))
    assert next(it) == attendu
    with pytest.raises(StopIteration):
        next(it)


def test_resolution_long():
    attendu = Grille.from_str("1234" "3412" "2143" "4321")
    entree = Grille.from_str("123X" "3XX2" "2XX3" "X32X")
    it = iter(resolution(entree))
    assert next(it) == attendu
    with pytest.raises(StopIteration):
        next(it)
