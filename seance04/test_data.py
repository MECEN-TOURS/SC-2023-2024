"""Description.

Tests pour le module lib_data.py
"""
from lib_data import Case, Grille, verifie_lignes, verifie_colonnes, verifie_interne
import pytest


def test_initialisation():
    essai = Grille(cases=[Case.UN for _ in range(16)])
    assert isinstance(essai, Grille)
    with pytest.raises(ValueError):
        essai = Grille(cases=[Case.UN for _ in range(15)])
    with pytest.raises(ValueError):
        essai = Grille(cases=[Case.UN for _ in range(17)])


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

    problematique3 = Grille(cases=[Case.TROIS if indice in {
                            8, 9} else Case.VIDE for indice in range(16)])
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

    problematique3 = Grille(cases=[Case.TROIS if indice in
                            {9, 12} else Case.VIDE for indice in range(16)])
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

    problematique3 = Grille(cases=[Case.TROIS if indice in {
                            10, 14} else Case.VIDE for indice in range(16)])
    assert not verifie_colonnes(problematique3)

    problematique4 = Grille(
        cases=[Case.QUATRE if indice in {3, 15}
               else Case.VIDE for indice in range(16)]
    )
    assert not verifie_colonnes(problematique4)
