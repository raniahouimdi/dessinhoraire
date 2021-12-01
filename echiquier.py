##################################################################
######## Author : Rania Houimdi  #################################
######## Date : 29 November 2021 #################################
########       Exercice 9        #################################
##################################################################

# Dans ce code j'ai defini une fonction échiquier qui permet 
# de retourner le dessin d'une grille n x n représentant
# un jeu d'échecs dont les dimensions sont données en paramètres.

import functools
case = '#'
texte = ''
ligne = ""

# Fonction permettant de retourner la largeur
# de la grille en fonction de la case
def Largeur(x,y):
    global case
    return x + case

# Comme est definie la fonction accumulateur permet
# de transformer plusieurs valeurs en une seule,
# ici je l'ai utilisé comme étant une 
# somme de deux chaînes de caractères 
def Accumulateur(x,y):
    return str(x) + str(y)
        
def Hauteur(x,y):
    # Global variable donne la permission de changer 
    # la valeur de la variable locale
    global ligne
    return x + ligne
    
def echiquier(n,largeur,hauteur):
    
    def lignes(i):
        global case
        global texte
        global ligne
    
        def colonnes(j):
            global texte
            global case                
            if (i%2)!=(j%2) :
                   case = " "             
            else:            
                   case = "#"            
            cellule= functools.reduce(Largeur,range(largeur-1),case)  
            return cellule            
        ligne= (functools.reduce(Accumulateur,
                                  (list(map(colonnes,range(n)))))+'\n')    
        texte  = texte + functools.reduce(Hauteur,range(hauteur-1),ligne)    
    list(map(lignes,range(n)))    
    return texte

print(echiquier(8,3,2))

def testEchiquier():
    assert functools.reduce(Largeur,range(0),"") == ''
    assert functools.reduce(Largeur,range(3),"") == '###'
    assert functools.reduce(Largeur,range(4),"") == '####'
    assert functools.reduce(Largeur,range(1),"") == '#'
    assert functools.reduce(Accumulateur,list(range(4))) == '0123'
    assert functools.reduce(Accumulateur,list(range(1))) == 0
    assert functools.reduce(Accumulateur,list(range(5,0,-1)))== '54321'

testEchiquier()
