# exercice-cryptage-3

# Énoncé du problème
Créez un programme qui génère des Codes d'Identification Nationaux (CIN) tunisiens avec les règles suivantes :

Contraintes
Le programme demande la taille n du tableau T1

Chaque élément de T1 est une chaîne de 7 chiffres

Le premier chiffre de chaque chaîne peut apparaître au maximum 2 fois dans tout la chaine

Calcul du chiffre de contrôle selon l'algorithme tunisien

Algorithme de calcul du chiffre de contrôle
Pour une chaîne c1 c2 c3 c4 c5 c6 c7 :

Appliquer les poids : 1, 3, 1, 3, 1, 3, 1

somme = c1×1 + c2×3 + c3×1 + c4×3 + c5×1 + c6×3 + c7×1

reste = somme % 10

chiffre_control = (10 - reste) % 10
