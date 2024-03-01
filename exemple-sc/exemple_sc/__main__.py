#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Description.

Exemple d'utilisation de typer
"""
from .lib_taches import Tache, CahierDesCharges, calcule_chronologie
from typer import Typer  # type: ignore
from serde.json import to_json, from_json  # type: ignore
from rich import print  # type:ignore
from rich.table import Table

app = Typer()


@app.command()
def demonstration(nom_fichier: str = "demo.json"):
    """Ecrie dans le fichier spécifié un exemple de cahier des charges"""
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
    with open(nom_fichier, "w") as fichier:
        fichier.write(to_json(cahier))
        print(f"{nom_fichier} a été créé")


@app.command()
def resolution(nom_fichier: str):
    with open(nom_fichier, "r") as fichier:
        cahier = from_json(c=CahierDesCharges, s=fichier.read())
    solution = calcule_chronologie(cahier)
    table = Table(title="Planning")
    table.add_column(header="Nom de Tache", justify="center", style="red")
    table.add_column(header="Debut", justify="right")
    table.add_column(header="Fin", justify="right")
    for tache, intervalle in solution.items():
        table.add_row(tache.nom, str(intervalle.debut), str(intervalle.fin))
    print(table)


if __name__ == "__main__":
    app()
