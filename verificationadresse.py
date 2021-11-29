##################################################################
######## Author : Rania Houimdi  #################################
######## Date : 14 November 2021 #################################
########       Exercice 7       #################################
##################################################################


#Fonction qui verifie une chaine de caractères
#donnés composés que de lettres latines (a-z et A-Z) et de chiffres (0-9) 
def isAlphaNumeric(adresseLocale):
    valid = True
    for char in adresseLocale:
        if ('A'<= char <= 'Z') or ('a'<= char <= 'z') or ('0'<= char <= '9'):
            valid = True
        else:
            return False
    return valid


#Fonction qui verifie une chaine de caractères
#donnés composés que de lettres latines (a-z et A-Z), 
#de chiffres (0-9) et de points (.)
def isDomainValid(domain):
    #séparer une chaîne par un separateur et renvoie une liste de chaînes.
    splitedDomain = domain.split(".")
    valid = False
    #longueur de spliteDomain
    if len(splitedDomain) < 2:
        return False
    for phrase in splitedDomain:
        #longueur de phrase
        if len(phrase)==0:
            return False
        else: 
           if(isAlphaNumeric(phrase)):
              valid = True
           else:
              return False
    return valid


#Une fonction permettant de déterminer si une adresse courriel est valide
def courrielValide(email):
    splittedEmail = email.split("@")
    if len(splittedEmail) != 2:
        return False
    #Appel à la première fonction
    validAdressLocal = isAlphaNumeric(splittedEmail[0])
    #Appel à la deuxième fonction 
    validDomain = isDomainValid(splittedEmail[1])
    return validAdressLocal and validDomain

#Fonction permettant de tester la dernière fonction
def testCourrielValide():
    assert courrielValide("AdaLovelace@iro.umontreal.ca") == True
    assert courrielValide("AdaLovelace@iroumontreal.ca") == True 
    assert courrielValide("AdaLovelace@iro.umontrealca") == True 
    assert courrielValide("AdaLovelace3@iro.umontreal.ca") == True
    assert courrielValide("3AdaLovelace@iro.umontreal.ca") == True
    assert courrielValide("AdaLovelace@3iro.umontreal.ca") == True
    assert courrielValide("AdaLovelace3@iro.umo5ntreal.ca") == True
    assert courrielValide("  AdaLovelace@iro.umontreal.ca") == False
    assert courrielValide("AdaLovelace@iro.umontreal.ca  ") == False
    assert courrielValide("AdaLovelace@iroumontrealca") == False
    assert courrielValide("Ada.Lovelace@iro.umontreal.ca ") == False
    assert courrielValide("AdaLove?lace@iro.umontreal.ca ") == False
    assert courrielValide("AdaLovelace@iro.umontrea\l.ca ") == False
    assert courrielValide("AdaLovelace@iro&umontreal&ca ") == False
    assert courrielValide("AdaLovelace@.iro.umontreal.ca ") == False
    assert courrielValide("AdaLovelaceiro&umontrealca@ ") == False
    assert courrielValide("") == False
    assert courrielValide("   ") == False

testCourrielValide()
print(courrielValide("rania™@umontreal.ca"))