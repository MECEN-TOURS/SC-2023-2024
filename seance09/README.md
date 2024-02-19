# Séances 09 et 10

- Introduction du problème de flot maximal
  - On se donne un graphe pondéré positivement (le poids sera la capacité de l'arrête)
  - Deux arrêtes spécifiques sont identifiés: l'entrée et la sortie
  - On va chercher à affecter un nombre positif sur chaque arrête (le débit) de sorte que
  - Sur chaque arrête le débit est inférieur à la capacité
  - A chaque sommet la somme des débits entrant est égale à la somme des débits sortants
- Après modélisation on voit qu'on peut se ramener à un programme linéaire
- On va coder les passerelles et utiliser `scipy` pour la résolution
- Choix des structures de données: liste d'arretes vs table d'adjacence
- Conversion entre les différentes représentations
- Lorsqu'on utilise des listes comme structures non ordonnées, les tests doivent se faire **après** tri.
- Introduction de `NewType` pour créer des types dérivées
- Utilisation du typechecker (dans vscode via pylance)
- On passe d'une représentation `arretes: Arretes` (en liste d'arr^etes) vers le tableau numpy `x` en entrée de `linprog` de façon à ce que le nombre à l'indice `i` dans `x` représente le débit de l'arrete à l'indice `i` de `arretes`.
