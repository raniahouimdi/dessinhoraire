###################################################################
######## Author : Rania Houimdi   #################################
######## Date :  06 Decembre 2021 #################################
########       Exercice 10        #################################
###################################################################


# Ce code permet d'afficher un triangle équilatéral fractal
# en se serrant de la fonction fractal definie ci-dessous 
# qui prend deux parametres positifs, le premier indique 
# la longeur des côtés et le deuxième indique le niveau 
# de décomposition du triangle.

from turtle import*
import geometrie
import math

def fractal(côté,d):
    
    # Variables permettent d'aider le déplacement de la tortue   
    moitieInferieure = 1/3
    moitieSuperieure = 2/3

    if d==0:
        
        # J'ai dû appeler la procédure trianglePlein qui permet de dessiner 
        # un triangle équilatéral plein centré 
        geometrie.trianglePlein(côté)  
  
    else:
        
        # Dimension du triangle fractal
        perimetre = (3*côté)/2
        côté = perimetre/3
        # Formule permet de calculer la hauteur du triangle 
        hauteur = math.sqrt(côté**2 * 3/4)
 
        # Cette première commande permet de dessiner la partie superieure
        # du triangle initial en positionnant la tortue à la bonne place
        pu();fd((hauteur*moitieInferieure)*2);pd();fractal(côté,d-1);pu()
        bk((hauteur*moitieInferieure)*2)
        
        # Cette deuxième commande permet de dessiner la partie inférieure
        # droite du triangle en positionnant la tortue à la bonne place
        bk(hauteur*moitieSuperieure);lt(90);fd(côté/2);rt(90)
        fd(hauteur*moitieInferieure);pd();fractal(côté,d-1);pu()
        bk(hauteur*moitieInferieure);rt(90);fd(côté);lt(90)
        
        # Cette première commande permet de dessiner la partie inférieure
        # gauche du triangle en positionnant la tortue à la bonne place
        fd(hauteur*moitieInferieure);pd();fractal(côté,d-1);pu()
        bk(hauteur*moitieInferieure);rt(90);bk(côté/2);lt(90)
        fd(hauteur*moitieSuperieure);pd()

        




        

        