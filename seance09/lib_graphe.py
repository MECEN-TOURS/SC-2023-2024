"""Description.

Librairie pour représenter les graphes pondérés.
"""
from typing import NewType


Arretes = NewType("Arretes", list[tuple[str, str, float]])
Table = NewType("Table", dict[str, dict[str, float]])


def arretes_to_table(arretes: Arretes) -> Table:
    resultat = dict()
    for depart, arrivee, poids in arretes:
        if depart not in resultat:
            resultat[depart] = {arrivee: poids}
        resultat[depart][arrivee] = poids
    return Table(resultat)


def table_to_arretes(table: Table) -> Arretes:
    resultat = list()
    for depart in table:
        for arrivee, poids in table[depart].items():
            resultat.append((depart, arrivee, poids))
    return Arretes(resultat)
