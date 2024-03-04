# Sujet 04 : Adduction d'eau

Trois villes J, K, L sont alimentées en eau grâce à quatre réserves A, B, C, D.
Les réserves journalières disponibles sont

- de 15 millier de $m^3$ pour A,B et C
- de 10 milliers de $m^3$ pour D.

Le réseau historique comporte même quelques aqueducs romains.
Il emprunte cinq anciens noeuds E, F, G, H, I.
Voici le tableau des capacités de débits du réseau.
La ligne x colonne y est le flux maximal du noeud x vers le noeud y.

|     | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A   |     |     |     |     | 7   |     |     |     |     |     |     |     |
| B   |     |     |     |     |     | 10  | 7   |     |     |     |     |     |
| C   | 5   |     |     |     |     | 5   |     |     |     |     |     |     |
| D   |     |     |     |     |     |     | 10  |     |     |     |     |     |
| E   |     |     |     |     |     | 5   |     | 4   | 15  |     |     |     |
| F   |     |     |     |     |     |     | 5   |     | 15  |     |     |     |
| G   |     |     |     |     |     |     |     |     | 15  |     |     |     |
| H   |     |     |     |     |     |     |     |     |     | 7   |     |     |
| I   |     |     |     |     |     |     |     |     |     |     | 30  | 4   |
| J   |     |     |     |     |     |     |     |     |     |     |     |     |
| K   |     |     |     |     |     |     |     |     |     | 10  |     |     |
| L   |     |     |     |     |     |     |     |     |     |     |     |     |

Ces trois villes sont en pleine évolution.
Elles désirent améliorer leur réseau d'alimentation afin de satisfaire
des besoins futurs.
Les prévisions des demandes journalières maximales sont de

- 15 milliers de m^3 pour les villes J et L
- 20 milliers de m^3 pour la ville K.

1. Dessiner le graphe de ce réseau.
   Déterminer la valeur du flot maximal pouvant passer dans le réseau actuel.
2. La valeur de ce flot est jugée nettement insuffisante.
   La région décide de refaire les canalisations (AE) et (IL).
   Déterminer les capacités à prévoir pour ces deux canalisations.
   Déterminer aussi la valeur du nouveau flot optimal.
3. Devant l'importance des travaux, la région décide de faire les travaux
   en deux temps.
   Déterminer l'ordre de la réfection des canalisations permettant d'augmenter
   le flot maximal après chaque travaux.
   Calculer ce flot maximal à chaque étape.
