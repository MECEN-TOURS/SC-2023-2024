# Séance 04

- Modélisation d'un solveur de Sudoku par parcours de graphe
  - On commence par des grilles 4x4
  - Un sommet est une grille partiellement remplie
  - $5^16$ sommets à priori donc on ne va pas chercher à stocker le graphe en mémoire
  - Les voisins d'une grille vont etre celles où la première case vide a été remplie
  - De ce fait, on a un graphe sans boucle i.e. un arbre!
  - Comme la hauteur maximale  va etre 16, on peut se contenter d'un algorithme récursif
- Brainstorming pour la représentation informatique d'une grille partiellement remplie
  1. une liste de 4 listes de 4 cases : les sous listes représentant les lignes
  2. une liste de 4 listes de 4 cases : les sous listes représentant les colonnes
  3. une liste de 4 listes de 4  cases: les sous listes représentant les sous carrés
  4. une liste avec 16 cases
  5. une case étant au choix: 
    - un int avec la convention que ce qui n'est pas 1, 2, 3 ou 4 est vide
    - un str avec la convention "1", "2", "3", "4" ou  " " le problème étant les autres str
    - un enum avec 5 états admissibles
- Utilisation Enum et dataclass: on ne peut représenter que des états valides
- Méthode `__post_init__` pour garantir l'état construit
- TDD: signature -> test -> implémentation
