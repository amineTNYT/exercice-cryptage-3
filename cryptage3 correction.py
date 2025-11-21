from numpy import array

def remplir(t):
    # Demander à l'utilisateur s'il veut ajouter un CIN
    R = input("ajouter une cin pour verifier O/N= ")
    i = 0
    # Tant que l'utilisateur répond "O" (oui)
    while R.upper() == "O":
        # Saisir le CIN et le stocker dans le tableau t
        t[i] = int(input("t[" + str(i) + "]= "))
        i = i + 1  # Passer à l'indice suivant
        # Redemander si l'utilisateur veut ajouter un autre CIN
        R = input("ajouter une cin pour verifier O/N= ")
    n = i  # n contient le nombre de CIN saisis
    return n  # Retourner le nombre de CIN


def verif(x):
    # Convertir le CIN en chaîne de caractères
    ch = str(x)
    
    # Initialiser les sommes pour les positions paires et impaires
    s1 = 0  # Somme pour les positions paires (poids 1)
    s2 = 0  # Somme pour les positions impaires (poids 3)
    
    # Parcourir les 7 premiers chiffres du CIN
    for i in range(len(ch) - 1):  # range(7) - correct
        if i % 2 == 0:
            # Position paire : multiplier par 1 et ajouter à s1
            s1 = s1 + int(ch[i]) * 1
        else:
            # Position impaire : multiplier par 3 et ajouter à s2
            s2 = s2 + int(ch[i]) * 3
    
    # Calculer le reste de la division par 10 de la somme totale
    reste = (s1 + s2) % 10
    # Calculer le chiffre de contrôle
    chiffre_controle = (10 - reste) % 10
    
    # Vérifier si le 8ème chiffre correspond au chiffre de contrôle calculé
    return int(ch[7]) == chiffre_controle


def remplir2(t, n, cin):
    # Initialiser le compteur
    x = 0
    # Parcourir tous les CIN du tableau t
    for i in range(n):
        if verif(t[i]) == True:
            # Si le CIN est valide, stocker "valider" dans cin
            cin[i] = "valider"
            x = x + 1
        else:
            # Si le CIN est invalide, stocker "faux" dans cin
            cin[i] = "faux"
            x = x + 1
    return x  # Retourner le nombre total de CIN traités


def affichage(cin, n):
    # Afficher tous les résultats de validation
    for i in range(n):
        print(cin[i], end=" | ")


# Programme principal
# Créer un tableau t de 100 entiers pour stocker les CIN
t = array([int] * 100)
# Remplir le tableau t avec les CIN saisis et récupérer le nombre n
n = remplir(t)
# Créer un tableau cin de n strings pour stocker les résultats
cin = array([str] * n)
# Vérifier les CIN et remplir le tableau cin avec les résultats
x = remplir2(t, n, cin)
# Afficher les résultats de validation
affichage(cin, x)
