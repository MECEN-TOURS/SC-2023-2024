# Contenu séance 02

- Bascule 
  * d'un paradigme interactif en notebook 
  * vers un paradigme librairie + test 
  * en utilisant `python -m pytest test_traversee`
- Introduction des conventions pour CONSTANTE, Classe, variable, fonction, plusieurs_mots
- Installation d'une librairie externe via `python -m pip install pytest`
- Utilisation d'un formatteur de code 
  * installation via `python -m pip install black`
  * utilisation via `black lib_traversee.py test_traversee.py`
- Utilisation d'un typechecker
  * installation via `python -m pip install --user mypy`
  * utilisation via `python -m mypy ./lib_traversee.py`
  * introduction d'un bogue pour voir l'intérêt
- Utilisation d'un linter 
  * installation via `python -m pip install ruff`
  * utilisation via `python -m ruff .\test_traversee.py`
- Introduction des docstrings pour fonctions et classes
  * Première phrase descriptive
  * Exemples d'utilisation copiant/collant les tests dans un terminal
  * Intérêt utilisateur: pas besoin d'aller regarder le code source
- Introduction de la bibliothèque `rich` pour une meilleur affichage
  * Installation par `python -m pip install --user rich`
  * Utilisation du nouveau print par `from rich import print`
  * Utilisation de `from rich import inspect`
  * Démonstration via `python -m rich`, `python -m rich.progress`
- EXERCICE: compléter la documentation en ajoutant des exmples pour Rive, Etat, sont_connectes
- algorithmes de recherche de chemin dans un graphe dfs/bfs