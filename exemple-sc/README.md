# Exemple de projet python

- Utilisation de poetry
  - `poetry new`
    pour créer un nouveau projet
    attention dans le nom du projet les - sont convertis en \_ en interne
  - `poetry add`
    pour ajouter une dépendance
  - `poetry add --group=dev`
    pour ajouter une dépendance de développement
  - `poetry install`
    pour créer l'environnement virtuel
  - `poetry shell`
    pour exécuter des commandes dans l'environnement virtuel
  - `poetry run`
    pour ceux qui ne peuvent pas exécuter de script sur leur machine
- Sérialisation vers json
  - Installation de la bibliothèque `pyserde`
  - Utilisation du décorateur `@serde` arès `from serde import serde`
  - Utilisation de `from_json` et `to_json`
    après `from serde.json import to_json, from_json`
- Interface ligne de commande
  - Installation de `typer`
  - Commande de génération d'un fichier entrée
  - Commande de résolution à partir d'un fichier entrée
  - Commande de visualisation d'un fichier sortie
- On réécrira le projet en utilisant `pydantic` pour les dataclass et leur sérialisation
