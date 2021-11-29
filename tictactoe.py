n = 3
hauteur = 3
largeur = 6
caractereDesLignes = '#'
ligne = ''
    
for x in range(n):
    for u in range(hauteur):
        for i in range(n):
            for j in range(largeur):
                ligne += ' '
            if i != 2:
                ligne += caractereDesLignes
        print(ligne)
        ligne = ''
    if x != 2:
        for c in range(largeur * n + n -1):
            ligne += caractereDesLignes
    print(ligne)
    ligne = ''


       
            