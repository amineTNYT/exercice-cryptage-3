# exercice-cryptage-3

# Énoncé du problème

Créez un programme qui vérifie la validité des Codes d'Identification Nationaux (CIN) tunisiens.

Algorithme de vérification :
Pour un CIN de 8 chiffres : c1 c2 c3 c4 c5 c6 c7 c8

Appliquer les poids : 1, 3, 1, 3, 1, 3, 1 aux 7 premiers chiffres

Calculer : somme = c1×1 + c2×3 + c3×1 + c4×3 + c5×1 + c6×3 + c7×1

Calculer : reste = somme % 10

Calculer : chiffre_control = (10 - reste) % 10

Le CIN est valide si c8 = chiffre_control

Le programme utilise :

Un tableau t pour stocker les CIN saisis

Un tableau cin pour stocker les résultats ("valider" ou "faux")

Le programme doit :

Saisir plusieurs CIN dans le tableau t

Vérifier chaque CIN selon l'algorithme

Afficher "valider" ou "faux" pour chaque CIN dans le tableau cin
# example

ajouter une cin pour verifier O/N= O
t[0]= 78452141
ajouter une cin pour verifier O/N= O
t[1]= 12345678  
ajouter une cin pour verifier O/N= O
t[2]= 78452147
ajouter une cin pour verifier O/N= N
valider | valider | faux |
