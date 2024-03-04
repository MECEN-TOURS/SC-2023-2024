# Affectation des sujets

## Groupes

1. Hugo et Grégory
2. Mohamed et Jarod
3. Paul et Gabin
4. Alison et Laxmitha
5. Alexis et Raphaël
6. Gabriel et Jawad
7. Corentin et Romain

## Affectation

On exécutera le script `affectation.py` pour obtenir la correspondance
entre groupe et sujet.

## Consignes

Les sujets sont constitués d'un _exemple_ de problème.

1. On commencera évidemment par le résoudre.
2. Dans un second temps, il faudra _le généraliser_ en une classe de problème.
   Il est bien entendu que plus le problème sera généralisé meilleure sera la note.
3. On codera ensuite une librairie permettant à des développeurs python
   de résoudre un problème de cette classe
4. On ajoutera finalement une interface graphique permettant à
   des personnes n'utilisant pas python de résoudre de tels problemes .

## Projet complet

On devra avoir en particulier:

- Une gestion des dépendances pour garantir la portabilité entre machines.
  On pourra utiliser `poetry` pour ceci.
- Une librairie typée/testée/documentée.
  On pourra entre autre utiliser `mypy`, `pytest` (et `pytest-cov` pour la couverture).
  On suggère fortement d'utiliser un linter tel que `ruff` pour éviter les bogues.
- Une interface en ligne de commande (via `typer`).
- On pourra faire une démonstration via un fichier `README.md`.
  Par exemple, en utilisant l'interface pour résoudre le problème exemple.
  On pourra s'inspirer de [rich](https://github.com/Textualize/rich) pour le README.
- Les personnes ambitieuses pourront chercher à proposer une interface graphique
  en utilisant la bibliothèque `streamlit`.

On pourra aussi s'inspirer de l'exemple présenté lors du dernier cours.
