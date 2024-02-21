"""Description.

Tests du module lib_taches.py
"""
from lib_taches import tri_topologique, Tache, CahierDesCharges, Arrete, Graphe, cahier_to_graphe
import pytest


def test_init_tache():
    tache = Tache(nom="A", duree=1., prerequis=["J", "E"])
    assert isinstance(tache, Tache)


def test_plantage_tache():
    with pytest.raises(ValueError):
        Tache(nom="A", duree=-1., prerequis=["J", "E"])
    with pytest.raises(ValueError):
        Tache(nom="A", duree=float("inf"), prerequis=["J", "E"])


def test_init_cahier():
    cahier = CahierDesCharges(
        taches=[
            Tache(nom="A", duree=1., prerequis=["B"]),
            Tache(nom="B", duree=2., prerequis=[]),
        ]
    )
    assert isinstance(cahier, CahierDesCharges)


def test_plantage_cahier():
    with pytest.raises(ValueError):
        CahierDesCharges(
            taches=[
                Tache(nom="A", duree=1., prerequis=["J", "E"]),
                Tache(nom="B", duree=2., prerequis=["C", "E"]),
            ]
        )


def test_acces_cahier():
    a = Tache(nom="A", duree=1., prerequis=["B"])
    b = Tache(nom="B", duree=2., prerequis=["C"])
    c = Tache(nom="C", duree=3., prerequis=["A"])
    cahier = CahierDesCharges(taches=[a, b, c])
    assert cahier["A"] == a
    with pytest.raises(KeyError):
        cahier["D"]


def test_cahier_to_graphe():
    a = Tache(nom="A", duree=1., prerequis=["B"])
    b = Tache(nom="B", duree=2., prerequis=["C"])
    c = Tache(nom="C", duree=3., prerequis=["A"])
    cahier = CahierDesCharges(taches=[a, b, c])
    graphe = Graphe(
        [
            Arrete((b, a, 2.)),
            Arrete((c, b, 3.)),
            Arrete((a, c, 1.))
        ]
    )
    assert cahier_to_graphe(cahier) == graphe


def test_tri():
    a = Tache(nom="A", duree=1., prerequis=["J", "E"])
    b = Tache(nom="B", duree=2., prerequis=["C", "E"])
    c = Tache(nom="C", duree=3., prerequis=["E"])
    d = Tache(nom="D", duree=3., prerequis=["B", "A"])
    e = Tache(nom="E", duree=3., prerequis=[])
    f = Tache(nom="F", duree=3., prerequis=["A"])
    g = Tache(nom="G", duree=3., prerequis=["B"])
    h = Tache(nom="H", duree=3., prerequis=["C"])
    i = Tache(nom="I", duree=3., prerequis=["F"])
    j = Tache(nom="J", duree=3., prerequis=["E"])
    cahier = CahierDesCharges(taches=[a, b, c, d, e, f, g, h, i, j])
    assert tri_topologique(cahier) == [e, c, j, a, b, h, d, f, g, i]


def test_plantage_tri():
    a = Tache(nom="A", duree=1., prerequis=["J", "E"])
    b = Tache(nom="B", duree=2., prerequis=["C", "E"])
    c = Tache(nom="C", duree=3., prerequis=["D", "E"])
    d = Tache(nom="D", duree=3., prerequis=["B", "A"])
    e = Tache(nom="E", duree=3., prerequis=[])
    f = Tache(nom="F", duree=3., prerequis=["A"])
    g = Tache(nom="G", duree=3., prerequis=["B"])
    h = Tache(nom="H", duree=3., prerequis=["C"])
    i = Tache(nom="I", duree=3., prerequis=["F"])
    j = Tache(nom="J", duree=3., prerequis=["E"])
    cahier = CahierDesCharges(taches=[a, b, c, d, e, f, g, h, i, j])
    with pytest.raises(ValueError):
        tri_topologique(cahier)
