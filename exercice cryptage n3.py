from numpy import array
def remplir(t):
	R=input("ajouter une cin pour verifier O/N= ")
	i=0
	while R.upper()=="O":
		t[i]=int(input("t["+str(i)+"]= "))
		i=i+1
		R=input("ajouter une cin pour verifier O/N= ")
	n=i
	return(n)
	


	
def verif(x):
    ch = str(x)
    
    s1=0
    s2=0
    for i in range(len(ch)-1):  # range(7) - correct
        if i % 2 == 0:
            s1 = s1 + int(ch[i]) * 1  # Accumuler dans s
        else:
            s2 = s2 + int(ch[i]) * 3  # Accumuler dans s
    
    reste = (s1+s2) % 10
    chiffre_controle = (10 - reste) % 10
    
    return int(ch[7]) == chiffre_controle
		
def remplir2(t,n,cin):
		
	x=0
	for i in range(n):
		if verif(t[i])==True:
			cin[i]="valider"
			x=x+1
		else:
			cin[i]="faux"
			x=x+1
	return x
def affichage(cin,n):
	for i in range(n):
		print(cin[i],end=" | ")




#programme.principale
t=array([int]*100)
n=remplir(t)
cin=array([str]*n)
x=remplir2(t,n,cin)
affichage(cin,x)
