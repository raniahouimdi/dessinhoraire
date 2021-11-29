##################################################################
######## Author : Rania Houimdi  #################################
######## Date : 22 November 2021 #################################
########       Exercice 8        #################################
##################################################################

# Ce code permmet d'afficher la fiche de paie 
# des employés sous forme d'un rapport.txt
# sachant que les informations d'heures et de salaires
# de chaque travailleur sont indiquées dans deux fichiers separés
# en format *csv


# Comme indiqué au cours cette fonction permet 
# de diviser un texte en lignes contenues dans un fichier
def decouperEnLignes(contenu):
    lignes = contenu.split('\n')
    if lignes[-1] == '':
        lignes.pop()
    return lignes

#  Comme indiqué au cours cette fonction permet 
# de lire le contenu du fichier CSV dans un tableau des rangées  
def lireCSV(path):
    lignes = decouperEnLignes(readFile(path))
    resultat = []
    for ligne in lignes:
        resultat.append(ligne.split(','))        
    return resultat

# Cette fonction va nous permettre d'afficher le rapport sous 
# forme d'un fichier.txt
def ecrireRapport():
    tableSalaires = lireCSV("salaires.csv")
    tableHeures =   lireCSV("heures.csv")
    salary = ""    
    for i in range(len(tableSalaires)):
        nePasTravailler = True  
        for j in range(len(tableHeures)):
            if tableSalaires[i][0] == tableHeures[j][0]:
                salary += (tableSalaires[i][0] + ": "+ " payer " 
                +str(int(tableSalaires[i][1])*int(tableHeures[j][1]))+"$"+"\n")
                nePasTravailler = False 
        if nePasTravailler:
            salary += (tableSalaires[i][0] + ": "+ " payer " + "0" +"$" + "\n")
                                       
    # Permet de créer le fichier path et remplace
    # son contenu par le deuxième argument
    writeFile("rapport.txt",salary)
    
    
#Fonction permattant de tester la fonction decouperEnLignes
def testdecouperEnLignes():
    assert ('Rania Houimdi,20') == ['Rania Houimdi,20']
    assert ('Rania Houimdi,20', 'Fahd Houimdi,30', 
    'Adam Houimdi,10') == ['Rania Houimdi,20', 'Fahd Houimdi',
                            'Adam Houimdi,10']
    assert not ('Rania Houimdi,20') == 'Rania Houimdi,20''\n'
    assert not ('Rania Houimdi,20', 'Fahd Houimdi,30', 
    'Adam Houimdi,10') == 'Rania Houimdi,20''\n''Fahd Houimdi''\n'
    'Adam Houimdi,10'
    

    
    
ecrireRapport()