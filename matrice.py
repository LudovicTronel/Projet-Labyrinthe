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
  """
  crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
  valeurParDefaut dans chacune des cases
  paramètres: 
    nbLignes un entier strictement positif qui indique le nombre de lignes
    nbColonnes un entier strictement positif qui indique le nombre de colonnes
    valeurParDefaut la valeur par défaut
  résultat la matrice ayant les bonnes propriétés
  """
  matrice=[]
  for i in range(nbLignes):
    matrice.append([])
    for j in range(nbColonnes):
      matrice[i].append(valeurParDefaut)
      
  return matrice 

def getNbLignes(matrice):
  """
  retourne le nombre de lignes de la matrice
  paramètre: matrice la matrice considérée
  """
  return len(matrice)
	

def getNbColonnes(matrice):
  """
  retourne le nombre de colonnes de la matrice
  paramètre: matrice la matrice considérée
  """
  res = 0
  for i in range(len(matrice)):
    res+=1
  return res


def getVal(matrice,ligne,colonne):
  """
  retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
  paramètres: matrice la matrice considérée
              ligne le numéro de la ligne (en commençant par 0)
              colonne le numéro de la colonne (en commençant par 0)
  """
  return matrice[ligne][colonne]

def setVal(matrice,ligne,colonne,valeur):
  """
  met la valeur dans la case se trouve en (ligne,colonne) de la matrice
  paramètres: matrice la matrice considérée
              ligne le numéro de la ligne (en commençant par 0)
              colonne le numéro de la colonne (en commençant par 0)
              valeur la valeur à stocker dans la matrice
  cette fonction ne retourne rien mais modifie la matrice
  """
  matrice[ligne][colonne]=valeur

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
  matrice[numLig].append(nouvelleValeur)
  valeur=matrice[numLig].pop(0)
  return valeur

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
  """
  decale la ligne numLig d'une case vers la droite en insérant une nouvelle
  valeur pour remplacer la premiere case à gauche de cette ligne
  paramèteres: matrice la matrice considérée
               numLig le numéro de la ligne à décaler
               nouvelleValeur la valeur à placer
  résultat: la valeur de la case "ejectée" par le décalage
  """
  matrice[numLig].insert(0,nouvelleValeur)
  valeur=matrice[numLig].pop(-1)
  return valeur 

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
  """
  decale la colonne numCol d'une case vers le haut en insérant une nouvelle
  valeur pour remplacer la premiere case en bas de cette ligne
  paramèteres: matrice la matrice considérée
               numCol le numéro de la colonne à décaler
               nouvelleValeur la valeur à placer
  résultat: la valeur de la case "ejectée" par le décalage
  """
  valeur = matrice[0][numCol]
  for i in range(len(matrice)-1):
    matrice[i][numCol] = matrice[i+1][numCol]
  matrice[len(matrice)-1][numCol] = nouvelleValeur
  return valeur
	

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
  """
  decale la colonne numCol d'une case vers le bas en insérant une nouvelle
  valeur pour remplacer la premiere case en haut de cette ligne
  paramèteres: matrice la matrice considérée
               numCol le numéro de la colonne à décaler
               nouvelleValeur la valeur à placer
  résultat: la valeur de la case "ejectée" par le décalage
  """
  valeur = matrice[len(matrice)-1][numCol]
  for i in range(len(matrice)-1,0,-1):
    matrice[i][numCol] = matrice[i-1][numCol]
  matrice[0][numCol] = nouvelleValeur
  return valeur

if __name__=='__main__':
  m=Matrice(7,7)
  print('Vérification création matrice:    ', m)
  print('Vérification nombre lignes:', getNbLignes(m))
  print('Vérification nombre colonne:', getNbColonnes(m))
  print('Vérification récupéreration valeur:', getVal(m,2,2))
  setVal(m,2,0,1)
  print('Initialisation décalage à gauche: ',m)
  print('Vérification valeur éjectée:',decalageLigneAGauche(m,2,2))
  print('Vérification décalage à gauche:   ', m)
  print('Initialisation décalage à droite: ',m)
  print('Vérification valeur éjectée:',decalageLigneADroite(m,2,3))
  print('Vérification décalage à droite    ', m)
  setVal(m,0,0,4)
  print('Initialisation décalage en haut:  ',m)
  print('Vérification valeur éjectée:', decalageColonneEnHaut(m,0,5))
  print('Vérification décalage en haut:    ', m)
  print('Vérification valeur éjectée:', decalageColonneEnBas(m,0,6))
  print('Vérification décalage en bas:     ',m)