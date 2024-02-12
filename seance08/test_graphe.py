"""Description.

Module de test de lib_graphe.py
"""

from lib_graphe import Graphe, calcule_distance, itere_distance, calcule_chemin_optimal, itere_distance_enrichie, calcule_chemins_optimaux, itere_distance_doublement_enrichie
import pytest


def test_initialisation():
    g = Graphe(sommets=set("ABC"), arretes=[("A", "B", 1.5)])
    assert isinstance(g, Graphe)


def test_verifications_ponderations():
    with pytest.raises(ValueError):
        g = Graphe(sommets=set("ABC"), arretes=[("A", "B", -1.5)])


def test_verifications_sommets():
    with pytest.raises(ValueError):
        g = Graphe(sommets=set("AC"), arretes=[("A", "B", 1.5)])
    with pytest.raises(ValueError):
        g = Graphe(sommets=set("BC"), arretes=[("A", "B", 1.5)])


@pytest.fixture
def exemple_graphe():
    return Graphe(
        sommets=set("ABCD"),
        arretes=[
            ("A", "B", 1.0),
            ("B", "C", 3.0),
            ("A", "C", 5.0),
            ("B", "D", 1.0),
            ("D", "C", 1.0),
        ],
    )


@pytest.fixture
def exemple_graphe_multiples():
    """Plusieurs chemins minimaux de A vers C"""
    return Graphe(
        sommets=set("ABCD"),
        arretes=[
            ("A", "B", 1.0),
            ("B", "C", 2.0),
            ("A", "C", 5.0),
            ("B", "D", 1.0),
            ("D", "C", 1.0),
        ],
    )


def test_itere_distance(exemple_graphe):
    entree = dict(A=float("inf"), B=float("inf"), C=0, D=float("inf"))
    attendue = dict(A=5.0, B=3.0, C=0, D=1.0)
    assert itere_distance(graphe=exemple_graphe,
                          distance=entree, cible="C") == attendue


def test_plantage_itere_distance(exemple_graphe):
    entree = dict(A=float("inf"), B=float("inf"), C=0)
    with pytest.raises(ValueError):
        itere_distance(graphe=exemple_graphe, distance=entree, cible="C")


def test_plantage_distance():
    g = Graphe(sommets=set("ABC"), arretes=[("A", "B", 1.0), ("B", "C", 2.0)])
    assert calcule_distance(depart="C", arrivee="A", graphe=g) == float("inf")


def test_distance_simple():
    g = Graphe(sommets=set("ABC"), arretes=[("A", "B", 1.0), ("B", "C", 2.0)])
    assert calcule_distance(depart="A", arrivee="C", graphe=g) == 3.0


def test_distance(exemple_graphe):
    assert calcule_distance(depart="A", arrivee="C",
                            graphe=exemple_graphe) == 3.0


def test_chemin(exemple_graphe):
    assert calcule_chemin_optimal(
        depart="A", arrivee="C", graphe=exemple_graphe
    ) == ["A", "B", "D", "C"]


def test_absence_chemin(exemple_graphe):
    with pytest.raises(ValueError):
        calcule_chemin_optimal(
            depart="C", arrivee="A", graphe=exemple_graphe
        )


def test_itere_distance_enrichie(exemple_graphe):
    entree = dict(A=(float("inf"), None), B=(float("inf"), None),
                  C=(0, "C"), D=(float("inf"), None))
    attendue = dict(A=(5.0, "C"), B=(3.0, "C"), C=(0, "C"), D=(1.0, "C"))
    assert itere_distance_enrichie(graphe=exemple_graphe,
                                   distance=entree, cible="C") == attendue


def test_plantage_itere_distance_enrichie(exemple_graphe):
    entree = dict(A=(float("inf"), None), B=(float("inf"), None), C=(0, "C"))
    with pytest.raises(ValueError):
        itere_distance_enrichie(graphe=exemple_graphe,
                                distance=entree, cible="C")


def test_chemins_multiples(exemple_graphe_multiples):
    it = calcule_chemins_optimaux(
        depart="A", arrivee="C", graphe=exemple_graphe_multiples)
    assert next(it) == ["A", "B", "C"]
    assert next(it) == ["A", "B", "D", "C"]
    with pytest.raises(StopIteration):
        next(it)


def test_absence_chemins(exemple_graphe_multiples):
    it = calcule_chemins_optimaux(
        depart="C", arrivee="A", graphe=exemple_graphe_multiples)
    with pytest.raises(StopIteration):
        next(it)


def test_itere_distance_doublement_enrichie(exemple_graphe_multiples):
    entree = dict(A=(float("inf"), []), B=(float("inf"), []),
                  C=(0, ["C"]), D=(float("inf"), []))
    attendue = dict(A=(5.0, ["C"]), B=(2.0, ["C"]),
                    C=(0, ["C"]), D=(1.0, ["C"]))
    assert itere_distance_doublement_enrichie(graphe=exemple_graphe_multiples,
                                              distance=entree, cible="C") == attendue


def test_itere_distance_doublement_enrichie_multiples(exemple_graphe_multiples):
    entree = dict(A=(5.0, ["C"]), B=(2.0, ["C"]),
                  C=(0, ["C"]), D=(1.0, ["C"]))
    attendue = dict(A=(3.0, ["B"]), B=(2.0, ["C", "D"]),
                    C=(0, ["C"]), D=(1.0, ["C"]))
    assert itere_distance_doublement_enrichie(graphe=exemple_graphe_multiples,
                                              distance=entree, cible="C") == attendue


def test_plantage_itere_distance_doublement_enrichie(exemple_graphe_multiples):
    entree = dict(A=(float("inf"), None), B=(float("inf"), None), C=(0, "C"))
    with pytest.raises(ValueError):
        itere_distance_enrichie(graphe=exemple_graphe_multiples,
                                distance=entree, cible="C")
