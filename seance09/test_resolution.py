"""Description.

Tests du module resolution
"""

from lib_graphe import Arretes
from lib_resolution import GrapheInvalide, resolution, genere_Aeq, genere_beq, genere_c, genere_bounds, genere_indices_lignes
import pytest
import numpy as np


@pytest.fixture
def arretes():
    return Arretes([
        ("entree", "A", float('inf')),
        ("A", "B", 1.),
        ("A", "D", 4.),
        ("B", "C", 2.),
        ("B", "E", 1.),
        ("C", "F", 3.),
        ("D", "C", 2.),
        ("D", "E", 2.),
        ("E", "F", 1.),
        ("F", "sortie", float("inf")),
    ])


def test_genere_indices_lignes(arretes):
    assert genere_indices_lignes(arretes) == dict(A=0, B=1, D=2, C=3, E=4, F=5)


def test_genere_Aeq(arretes: Arretes):
    attendu = np.array(
        [
            [1, -1, -1,  0,  0,  0,  0,  0,  0,  0],
            [0,  1,  0, -1, -1,  0,  0,  0,  0,  0],
            [0,  0,  1,  0,  0,  0, -1, -1,  0,  0],
            [0,  0,  0,  1,  0, -1,  1,  0,  0,  0],
            [0,  0,  0,  0,  1,  0,  0,  1, -1,  0],
            [0,  0,  0,  0,  0,  1,  0,  0,  1, -1],
        ]
    )
    assert np.all(genere_Aeq(arretes) == attendu)


def test_genere_c(arretes: Arretes):
    attendu = np.zeros(shape=(10,))
    attendu[-1] = -1
    assert np.all(genere_c(arretes) == attendu)


def test_genere_bounds(arretes: Arretes):
    attendu = [(0, None), (0, 1), (0, 4), (0, 2),
               (0, 1), (0, 3), (0, 2), (0, 2), (0, 1), (0, None)]
    assert genere_bounds(arretes) == attendu


def test_genere_beq(arretes: Arretes):
    attendu = np.zeros(shape=(6,))
    assert np.all(genere_beq(arretes) == attendu)


def test_resolution(arretes):
    attendu = Arretes([
        ("entree", "A", 4.),
        ("A", "B", 1.),
        ("A", "D", 3.),
        ("B", "C", 1.),
        ("B", "E", 0.),
        ("C", "F", 3.),
        ("D", "C", 2.),
        ("D", "E", 1.),
        ("E", "F", 1.),
        ("F", "sortie", 4.),
    ])
    calculee = resolution(arretes)
    assert sorted(calculee) == sorted(attendu)


def test_plantage_resolution():
    with pytest.raises(GrapheInvalide):
        resolution(Arretes([
            ("A", "B", 1.),
            ("A", "D", 3.),
            ("B", "C", 1.),
            ("B", "E", 0.),
            ("C", "F", 3.),
            ("D", "C", 2.),
            ("D", "E", 1.),
            ("E", "F", 1.),
            ("F", "sortie", float("inf")),
        ]))
    with pytest.raises(GrapheInvalide):
        resolution(Arretes([
            ("entree", "A", float("inf")),
            ("A", "B", 1.),
            ("A", "D", 3.),
            ("B", "C", 1.),
            ("B", "E", 0.),
            ("C", "F", 3.),
            ("D", "C", 2.),
            ("D", "E", 1.),
            ("E", "F", 1.),
        ]))
    with pytest.raises(GrapheInvalide):
        resolution(Arretes([
            ("entree", "A", float("inf")),
            ("A", "B", 1.),
            ("A", "D", 3.),
            ("B", "C", 1.),
            ("B", "E", 0.),
            ("C", "F", -3.),
            ("D", "C", 2.),
            ("D", "E", 1.),
            ("E", "F", 1.),
            ("F", "sortie", float("inf")),
        ]))
