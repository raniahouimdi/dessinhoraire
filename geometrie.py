# Fichier : geometrie.py
# Auteur : Marc Feeley
# Date : 2021-11-29

# Ce module défini la procédure trianglePlein qui fait l'affichage
# dans la fenêtre de dessin d'un triangle équilatéral plein centré sur
# la position de la tortue et orienté dans la même direction. L'unique
# paramètre de la procédure est un nombre positif qui indique la longueur
# des côtés du triangle en pixels. La procédure trianglePlein ne change
# pas la position et orientation de la tortue.
from turtle import*
import math
def trianglePlein(cote):

    sqrt3 = math.sqrt(3)

    # La procédure remplir fait le remplissage d'un des 3 côtés du
    # triangle équilatéral. Son unique paramètre est un nombre positif
    # indiquant la longueur des côtés du triangle en pixels.

    def remplir(cote):

        # La procédure bande fait le remplissage d'une zone rectangulaire
        # d'un des 3 cotés du triangle équilatéral. Le premier
        # paramètre est un nombre positif indiquant la longueur des
        # côtés du triangle en pixels. Le deuxième est un nombre
        # positif indiquant la position de la zone rectangulaire par
        # rapport au côté du triangle. Le troisième paramètre est un
        # nombre positif indiquant la portion du coté remplie
        # jusqu'à date.

        def bande(cote, pos, fait):
            pensize(cote - pos*2/sqrt3)  # longueur de la bande rectangulaire
            bk(fait/2)                   # superposer pour éviter des "trous"
            fd(pos - fait/2)             # remplir la bande

        apotheme = cote/(2*sqrt3)  # calculer le rayon du cercle inscrit

        pu(); bk(apotheme); pd()   # positionner la tortue sur le côté

        # remplir des bandes progressivement de plus en plus larges

        largeur = 1  # commencer avec une bande de largeur 1 pixel
        fait = 0     # rien rempli jusqu'à date

        while largeur < apotheme:
            bande(cote, largeur, fait)
            fait = largeur
            largeur *= 2

        # compléter le remplissage jusqu'au centre du triangle

        bande(cote, apotheme, fait)

    # remplir les 3 côtés du triangle

    for _ in range(3):
        lt(120)
        remplir(cote)
