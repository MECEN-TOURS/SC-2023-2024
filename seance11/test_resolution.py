"""Description.

Tests du module lib_resolution.py
"""
from lib_graphe import Table
from lib_resolution import calcule_flot_max, genere_Aeq, genere_bounds, genere_beq, genere_c
import pytest
import numpy as np


@pytest.fixture
def exemple_table():
    return Table(
        {
            "entree": {"A": float("inf")},
            "A": {"B": 2, "C": 3},
            "B": {"C": 1},
            "C": {"sortie": float("inf")},
        }
    )


def test_genere_bounds(exemple_table):
    assert genere_bounds(exemple_table) == [
        (0, None), (0, 2), (0, 3), (0, 1), (0, None)
    ]


def test_genere_c(exemple_table):
    assert np.all(genere_c(exemple_table) == np.array([0, 0, 0, 0, -1]))


def test_genere_beq(exemple_table):
    calcule = genere_beq(exemple_table)
    assert calcule.shape == (3,)
    egalites = calcule == np.zeros(shape=(3,))
    assert np.all(egalites)


def test_genere_Aeq(exemple_table):
    attendu = np.array(
        [
            [1, -1, -1,  0,  0],
            [0,  1,  0, -1,  0],
            [0,  0,  1,  1, -1],
        ]
    )
    calcule = genere_Aeq(exemple_table)
    assert calcule.shape == attendu.shape
    egalites = calcule == attendu
    assert np.all(egalites)


def test_calcule_flot_max(exemple_table):
    attendu = Table(
        {
            "entree": {"A": 4},
            "A": {"B": 1, "C": 3},
            "B": {"C": 1},
            "C": {"sortie": 4},
        }
    )
    assert attendu == calcule_flot_max(exemple_table)
