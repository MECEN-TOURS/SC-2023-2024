"""Description.

Tests du module lib_graphe.py
"""
from lib_graphe import arretes_to_table, table_to_arretes, Arretes, Table
import pytest


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


@pytest.fixture
def table():
    return Table({
        "entree": dict(A=float("inf")),
        "A": dict(B=1., D=4.),
        "B": dict(C=2., E=1.),
        "C": dict(F=3.),
        "D": dict(C=2., E=2.),
        "E": dict(F=1.),
        "F": dict(sortie=float("inf")),
    })


def test_arretes_to_table(arretes, table):
    assert arretes_to_table(arretes) == table


def test_table_to_arretes(arretes, table):
    assert sorted(table_to_arretes(table)) == sorted(arretes)
