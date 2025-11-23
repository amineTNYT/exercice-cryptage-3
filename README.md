# Vérification des CIN Tunisiens

## Problème

Créez un programme qui vérifie la validité des Codes d'Identification Nationaux (CIN) tunisiens selon l'algorithme officiel.

### Algorithme de vérification

Pour un CIN composé de 8 chiffres : **c1 c2 c3 c4 c5 c6 c7 c8**

1. **Appliquer les poids** : 1, 3, 1, 3, 1, 3, 1 aux 7 premiers chiffres
2. **Calculer** : `somme = c1×1 + c2×3 + c3×1 + c4×3 + c5×1 + c6×3 + c7×1`
3. **Calculer** : `reste = somme % 10`
4. **Calculer** : `chiffre_control = (10 - reste) % 10`
5. **Le CIN est valide si** : `c8 = chiffre_control`

### Structures de données

- **Tableau t** : stocke les CIN saisis par l'utilisateur 
- **Tableau cin** : stocke les résultats de validation ("valider" ou "faux")

## Exemple

### Calcul détaillé

Pour le CIN : **78452141**

| Chiffre | Poids | Produit |
|---------|-------|---------|
| 7 × 1 = | 7     |
| 8 × 3 = | 24    |
| 4 × 1 = | 4     |
| 5 × 3 = | 15    |
| 2 × 1 = | 2     |
| 1 × 3 = | 3     |
| 4 × 1 = | 4     |

**Somme** = 7 + 24 + 4 + 15 + 2 + 3 + 4 = **59**  

**Reste** = 59 % 10 = **9**  
$`\textcolor{red}{\text{**Chiffre contrôle** = (10 - 9) % 10 = **1**}}$`

✅ **Résultat** : CIN valide (le 8ème chiffre est bien 1)                          
                                                                              <img width="617" height="717" alt="image" src="https://github.com/user-attachments/assets/a9095cf0-3bf3-4969-b415-4768bde156e1" />


[annoncer de problem.xlsx](https://github.com/user-attachments/files/23683895/annoncer.de.problem.xlsx)

