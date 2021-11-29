#Rania Houimdi 24-09-2021
#Ce code permet à calculer la valeur pi jusqu'à une limite permise
#Ce code a eu la permission d'utiliser la boucle "while" pour enchaîner les informations du code 
import math
LE = 5e-6 #Une limitation de l'erreur
E = 0 #Initialisation de l'erreur
A = True #L'alternance du calcul
D = 1 # Les Diviseur
S = 0 #La somme
T = 0 #Les nombres de termes 
LT = 10**6 #Une limitation des termes
abandon = False #Il donne une affectation true pour abandonner quand le programme eu une condition pour quitter
puissance = 0 #Les puissances pour gérer le calcul et le code 

while abandon == False:
    if A == True:
        S += 4/D
        D += 2
        A = False
    else:
        S -= 4/D
        D += 2
        A = True
    
    E = abs(S - math.pi)
    
    if (E < LE):
        print("la somme a atteint l'erreur tolérable de " + (str)(T - 1) + ' à ' + (str)(T) + ' termes ')
        abandon = True
    T += 1
    
    if puissance == 6:
        abandon = True
        print("La somme n'a pas atteint l'erreur tolérable de " + (str)(T - 1) + ' à ' + (str)(T) + ' termes ')
    else:
            if (T % 10**puissance) == 0:
                print('à ' + (str)(10**puissance) + ' termes la somme est égale à ' + (str)(S))
                puissance += 1