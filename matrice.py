# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes, nbColonnes, valeurParDefaut=0):
    if nbLignes<0 or nbColonnes<0:
        return('Veuillez entrer des chiffres positifs pour la création du plateau')
    else :
        for i in range(nbColonnes):
            print(([valeurParDefaut for i in range(nbLignes)]))


def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    ligne=()
    nbLignes=()
    i=0
        for i in range(ligne):
            while i<len(liste):
                i=i+1
                if i==len(ligne):
                    nbLignes.append(1)
            return nbLignes
        return nbLignes
    

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    colonne=()
    nbColonnes=()
    i=0
        for i in range(colonne):
            while i<len(colonne):
                i=i+1
                if i==len(colonne):
                    nbColonnes.append(1)
            return nbColonnes
        return nbColonnes
    return nbColonnes

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    val=""
    for ligne in matrice:
      for collonne in ligne:
          for val in colonne:
            return val

def setVal(matrice,ligne,colonne,val):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    val=""
    for ligne in colonne:
        matrice.append(val) 
    
    
   


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    numLig=[]
    M=Matrice 
    for i in range(numLig):
        numLig.append(M[-1])
    return nouvelleValeur

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    
    numLig=[]
    M=matrice
    for i in range(numLig):
        numLig.append(M[+1])
    return nouvelleValeur

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
   
    numCol=[]
    M=matrice
    for i in range(numCol):
        numCol.append(M[-1])
    return nouvelleValeur

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    numCol=[]
    M=matrice
    for i in range(numCol):
        numCol.append(M[+1])
    return nouvelleValeur


"""if __name__=='__main__':

    m=Matrice(10,8,0)
    print('verification créatison matrice:', Matrice(10,8,0))
    print(' verif retourne nombre de ligne exact:', getNbLignes(Matrice))"""
