"""Description.

Tests du module lib_taches.py
"""

from exemple_sc.lib_taches import (
    _tri_topologique,
    Planning,
    Intervalle,
    Tache,
    CahierDesCharges,
    calcule_chronologie,
)
import pytest  # type: ignore


def test_init_tache():
    tache = Tache(nom="A", duree=1.0, prerequis=frozenset(["J", "E"]))
    assert isinstance(tache, Tache)


def test_plantage_tache():
    with pytest.raises(ValueError):
        Tache(nom="A", duree=-1.0, prerequis=frozenset(["J", "E"]))
    with pytest.raises(ValueError):
        Tache(nom="A", duree=float("inf"), prerequis=frozenset(["J", "E"]))


def test_init_cahier():
    cahier = CahierDesCharges(
        taches=[
            Tache(nom="A", duree=1.0, prerequis=frozenset(["B"])),
            Tache(nom="B", duree=2.0, prerequis=frozenset([])),
        ]
    )
    assert isinstance(cahier, CahierDesCharges)


def test_plantage_cahier():
    with pytest.raises(ValueError):
        CahierDesCharges(
            taches=[
                Tache(nom="A", duree=1.0, prerequis=frozenset(["J", "E"])),
                Tache(nom="B", duree=2.0, prerequis=frozenset(["C", "E"])),
            ]
        )


def test_acces_cahier():
    cahier = CahierDesCharges(
        taches=[
            Tache(nom="A", duree=1.0, prerequis=frozenset(["B"])),
            Tache(nom="B", duree=2.0, prerequis=frozenset(["C"])),
            Tache(nom="C", duree=3.0, prerequis=frozenset(["A"])),
        ]
    )
    assert cahier["A"] == Tache(nom="A", duree=1.0, prerequis=frozenset(["B"]))
    with pytest.raises(KeyError):
        cahier["D"]


def test_tri():
    a = Tache(nom="A", duree=1.0, prerequis=frozenset(["J", "E"]))
    b = Tache(nom="B", duree=2.0, prerequis=frozenset(["C", "E"]))
    c = Tache(nom="C", duree=3.0, prerequis=frozenset(["E"]))
    d = Tache(nom="D", duree=3.0, prerequis=frozenset(["B", "A"]))
    e = Tache(nom="E", duree=3.0, prerequis=frozenset([]))
    f = Tache(nom="F", duree=3.0, prerequis=frozenset(["A"]))
    g = Tache(nom="G", duree=3.0, prerequis=frozenset(["B"]))
    h = Tache(nom="H", duree=3.0, prerequis=frozenset(["C"]))
    i = Tache(nom="I", duree=3.0, prerequis=frozenset(["F"]))
    j = Tache(nom="J", duree=3.0, prerequis=frozenset(["E"]))
    cahier = CahierDesCharges(taches=[a, b, c, d, e, f, g, h, i, j])
    resultat = _tri_topologique(cahier)
    attendu = [e, j, a, c, f, h, i, b, d, g]
    assert resultat == attendu


def test_plantage_tri():
    a = Tache(nom="A", duree=1.0, prerequis=frozenset(["J", "E"]))
    b = Tache(nom="B", duree=2.0, prerequis=frozenset(["C", "E"]))
    c = Tache(nom="C", duree=3.0, prerequis=frozenset(["D", "E"]))
    d = Tache(nom="D", duree=3.0, prerequis=frozenset(["B", "A"]))
    e = Tache(nom="E", duree=3.0, prerequis=frozenset([]))
    f = Tache(nom="F", duree=3.0, prerequis=frozenset(["A"]))
    g = Tache(nom="G", duree=3.0, prerequis=frozenset(["B"]))
    h = Tache(nom="H", duree=3.0, prerequis=frozenset(["C"]))
    i = Tache(nom="I", duree=3.0, prerequis=frozenset(["F"]))
    j = Tache(nom="J", duree=3.0, prerequis=frozenset(["E"]))
    cahier = CahierDesCharges(taches=[a, b, c, d, e, f, g, h, i, j])
    with pytest.raises(ValueError):
        _tri_topologique(cahier)


def test_calcule_chronologie():
    a = Tache(nom="A", duree=1.0, prerequis=frozenset(["J", "E"]))
    b = Tache(nom="B", duree=2.0, prerequis=frozenset(["C", "E"]))
    c = Tache(nom="C", duree=3.0, prerequis=frozenset(["E"]))
    d = Tache(nom="D", duree=4.0, prerequis=frozenset(["B", "A"]))
    e = Tache(nom="E", duree=3.0, prerequis=frozenset([]))
    f = Tache(nom="F", duree=2.0, prerequis=frozenset(["A"]))
    g = Tache(nom="G", duree=1.0, prerequis=frozenset(["B"]))
    h = Tache(nom="H", duree=2.0, prerequis=frozenset(["C"]))
    i = Tache(nom="I", duree=3.0, prerequis=frozenset(["F"]))
    j = Tache(nom="J", duree=4.0, prerequis=frozenset(["E"]))
    cahier = CahierDesCharges(taches=[a, b, c, d, e, f, g, h, i, j])
    attendu = Planning(
        {
            a: Intervalle(debut=7.0, fin=8.0),
            b: Intervalle(debut=6.0, fin=8.0),
            c: Intervalle(debut=3.0, fin=6.0),
            d: Intervalle(debut=8.0, fin=12.0),
            e: Intervalle(debut=0.0, fin=3.0),
            f: Intervalle(debut=8.0, fin=10.0),
            g: Intervalle(debut=8.0, fin=9.0),
            h: Intervalle(debut=6.0, fin=8.0),
            i: Intervalle(debut=10.0, fin=13.0),
            j: Intervalle(debut=3.0, fin=7.0),
        }
    )
    calculee = calcule_chronologie(cahier)
    assert attendu == calculee

    calcule_chronologie(
        CahierDesCharges(
            taches=[
                Tache(nom="A", duree=1.0, prerequis=frozenset(["J", "E"])),
                Tache(nom="B", duree=2.0, prerequis=frozenset(["C", "E"])),
                Tache(nom="C", duree=3.0, prerequis=frozenset(["E"])),
                Tache(nom="D", duree=4.0, prerequis=frozenset(["B", "A"])),
                Tache(nom="E", duree=3.0, prerequis=frozenset([])),
                Tache(nom="F", duree=2.0, prerequis=frozenset(["A"])),
                Tache(nom="G", duree=1.0, prerequis=frozenset(["B"])),
                Tache(nom="H", duree=2.0, prerequis=frozenset(["C"])),
                Tache(nom="I", duree=3.0, prerequis=frozenset(["F"])),
                Tache(nom="J", duree=4.0, prerequis=frozenset(["E"])),
            ]
        )
    )
