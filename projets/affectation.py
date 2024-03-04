#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Script effectuant la répartition des sujets au élèves.
"""
import random as rd
from rich.console import Console

GROUPES = (
    ("Hugo", "Grégory"),
    ("Mohamed", "Jarod"),
    ("Paul", "Gabin"),
    ("Alison", "Lxamitha"),
    ("Alexis", "Raphael"),
    ("Gabriel", "Jawad"),
    ("Corentin", "Romain"),
)

SUJETS = [f"{numero:02}" for numero in range(1, 13)]
rd.seed(2024)
rd.shuffle(SUJETS)

CS = Console()

AFFECTATION = {eleve: sujet for eleve, sujet in zip(GROUPES, SUJETS)}
CS.print(AFFECTATION)
