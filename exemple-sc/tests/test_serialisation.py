#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Tests des propriétés de sérialisation des objets de la librairie.
"""
from exemple_sc import Planning, Tache, CahierDesCharges, Intervalle
from serde.json import to_json, from_json


def test_tache():
    a = Tache(nom="A", duree=3.0, prerequis=frozenset(("B", "C")))
    json = to_json(a)
    tache = from_json(c=Tache, s=json)
    assert a == tache


def test_cahier_des_charges():
    ...


def test_intervalle():
    ...


def test_planning():
    ...
