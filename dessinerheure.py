##################################################################
######## Author : Rania Houimdi  #################################
######## Date : 06 November 2021 #################################
########       Exercice 6        #################################
##################################################################

# Ce code permet d'afficher un dessin horaire dont
# les heures comprises entre 0 et 23
# les minutes comprises entre 0 et 59 

from turtle import*

encodage = [[True, True, True, True, True, True, False],
            [False, False, True, True, False, False, False],
            [False, True, True, False, True, True, True],
            [False, True, True, True, True, False, True],
            [True, False, True, True, False, False, True],
            [True, True, False, True, True, False, True],
            [True, True, False, True, True, True, True],
            [False, True, True, True, False, False, False],
            [True, True, True, True, True, True, True],
            [True, True, True, True, True, False, True]]


def verifierHeure(heure): #Verification ds heures
    if(heure > 23 or heure < 0):
        raise ValueError('les heures doit êtres comprises entre 0 et 23')  

def verifierMinute(minute): #Verification des minutes 
    if(minute > 59 or minute < 0):
        raise ValueError('les minutes doit êtres comprises entre 0 et 59')


#Avancerment de la tortue sans laisserr une trace
def avancerSansDessin(longueur): 
    pu()
    fd(longueur)
    pd()

 #Amener la tortue en arrière sans laisser une trace 
def reculerSansDessin(longueur): 
    pu()
    bk(longueur)
    pd()

#Fonction qui permet de dessiner un rectangle
def dessinerRectangle(longueur, largeur): 
    i = 0
    while i < 2:
        fd(largeur)
        lt(90)
        fd(longueur)
        lt(90)
        i = i + 1


#Fonction qui permet de dessiner des separateurs 
def dessinerSeparateur(longeur):
    reculerSansDessin(longeur/4) #Reculer sans laisser une trace 
    lt(90) #Pivoter à gauche d’un angle 90 degrés
    avancerSansDessin(longeur/4) 
    rt(90) #pivoter à droite d’un angle 90 degrés
    dessinerRectangle(longeur/2, longeur/4)
    rt(90)
    avancerSansDessin(longeur)
    lt(90)
    dessinerRectangle(longeur/2, longeur/4)
    lt(90)
    avancerSansDessin(3*longeur/4) #Avancer sans laisser une trace
    rt(90)
    avancerSansDessin(longeur/4)


#Fonction qui permet de dessiner les chiffres 
def dessinerChiffre(longueur, segments):
    i = 0
    for value in segments:
        if i == 0:
            lt(90)
        elif i != 3:
            rt(90)
        if value:
            fd(longueur)
        else:
            avancerSansDessin(longueur)
        i = i + 1

    pu() #Arrêter de laisser une trace
    bk(longueur) #Reculer d'une distance=longueur
    pd() #Commencer a faire des traces 

#Fonction qui permet de separer entre les chiffres 
def separateurChiffre(chiffre):
    if chiffre < 10 : 
        chiffre = "0" + str(chiffre)
    else :
        chiffre = str(chiffre)
    return chiffre

#Fonction qui permet de dessiner l'heure 
def dessinerHeure(longeur, h, m):
    verifierHeure(h)
    verifierMinute(m)
    h = separateurChiffre(h)
    m = separateurChiffre(m)
    reculerSansDessin(7*longeur/2)
    dessinerChiffre(longeur, segments = encodage[int(h[0])])
    avancerSansDessin(3*longeur/2)
    dessinerChiffre(longeur, segments = encodage[int(h[1])])
    avancerSansDessin(2*longeur)
    dessinerSeparateur(longeur)
    avancerSansDessin(longeur)
    dessinerChiffre(longeur, encodage[int(m[0])])
    avancerSansDessin(3*longeur/2)
    dessinerChiffre(longeur, segments = encodage[int(m[1])])
    reculerSansDessin(5*longeur/2)


    
dessinerHeure(50, 11,13) #Afficher le dessin horaire 
