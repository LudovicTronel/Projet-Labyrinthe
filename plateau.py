     # -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *
from random import shuffle


def Plateau(nbJoueurs, nbTresors):
  """
  créer un nouveau plateau contenant nbJoueurs et nbTrésors
  paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
              nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
  resultat: un couple contenant
            - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
              ont été placée de manière aléatoire
            - la carte amovible qui n'a pas été placée sur le plateau
  """
  listeCartes = creerCartesAmovibles(1,nbTresors)
  c={'Matrice': Matrice(7,7),'CarteRestante': listeCartes[-1] }
  
  setVal(c['Matrice'],0,0,Carte(True,False,False,True,None,1))
  setVal(c['Matrice'],0,1,listeCartes[0])
  setVal(c['Matrice'],0,2,Carte(True,False,False,False))
  setVal(c['Matrice'],0,3,listeCartes[1])
  setVal(c['Matrice'],0,4,Carte(True,False,False,False))
  setVal(c['Matrice'],0,5,listeCartes[2])
  if nbJoueurs>=1:
    setVal(c['Matrice'],0,6,Carte(True,True,False,False,None,2))
  else:
    setVal(c['Matrice'],0,6,Carte(True,True,False,False))

  for i in range(len(c['Matrice'][1])):
      setVal(c['Matrice'],1,i,listeCartes[i+3])
  
  setVal(c['Matrice'],2,0,Carte(False,False,False,True))
  setVal(c['Matrice'],2,1,listeCartes[10])
  setVal(c['Matrice'],2,2,Carte(False,False,False,True))
  setVal(c['Matrice'],2,3,listeCartes[11])
  setVal(c['Matrice'],2,4,Carte(True,False,False,False))
  setVal(c['Matrice'],2,5,listeCartes[12])
  setVal(c['Matrice'],2,6,Carte(False,True,False,False))

  for i in range(len(c['Matrice'][3])):
    setVal(c['Matrice'],3,i,listeCartes[i+13])
  
  setVal(c['Matrice'],4,0,Carte(False,False,False,True))
  setVal(c['Matrice'],4,1,listeCartes[14])
  setVal(c['Matrice'],4,2,Carte(False,False,True,False))
  setVal(c['Matrice'],4,3,listeCartes[15])
  setVal(c['Matrice'],4,4,Carte(False,True,False,False))
  setVal(c['Matrice'],4,5,listeCartes[16])
  setVal(c['Matrice'],4,6,Carte(False,True,False,False))

  for i in range(len(c['Matrice'][5])):
    setVal(c['Matrice'],5,i,listeCartes[i+17])
  
  if nbJoueurs>=2:
    setVal(c['Matrice'],6,0,Carte(True,True,False,False,None,3))
  else:
     setVal(c['Matrice'],6,0,Carte(True,True,False,False))
  setVal(c['Matrice'],6,1,listeCartes[18])
  setVal(c['Matrice'],6,2,Carte(False,False,True,False))
  setVal(c['Matrice'],6,3,listeCartes[19])
  setVal(c['Matrice'],6,4,Carte(False,False,True,False))
  setVal(c['Matrice'],6,5,listeCartes[20])
  if nbJoueurs>=3:
    setVal(c['Matrice'],6,6,Carte(True,True,False,False,None,4))
  else:
     setVal(c['Matrice'],6,6,Carte(True,True,False,False))
  
  return c
           
def creerCartesAmovibles(tresorDebut,nbTresors):
  """
  fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
  aléatoirement nbTresor trésors
  la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
  paramètres: tresorDebut: le numéro du premier trésor à créer
              nbTresors: le nombre total de trésor à créer
  résultat: la liste mélangée aléatoirement des cartes amovibles créees
  """
  cartAmov = []

  for i in range(16):
    cartAngl = Carte(True, True, False, False)
    tourneAleatoire(cartAngl)
    cartAmov.append(cartAngl)
  
  for i in range(12):
    cartDroit = Carte(True, False, True, False)
    tourneAleatoire(cartDroit)
    cartAmov.append(cartDroit)

  for i in range(6):
    cartJonc = Carte(True, False, False, False)
    tourneAleatoire(cartJonc)
    cartAmov.append(cartJonc)
  
  random.shuffle(cartAmov)

  for i in range(len(cartAmov)):
    tresAle = random.randint(tresorDebut, nbTresors)
    if getTresor(cartAmov[i]) == 0:
      mettreTresor(cartAmov[i],tresAle)

  random.shuffle(cartAmov)
  return cartAmov

def prendreTresorPlateau(plateau,lig,col,numTresor):
  """
  prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
  retourne True si l'opération s'est bien passée (le trésor était vraiment sur
  la carte
  paramètres: plateau: le plateau considéré
              lig: la ligne où se trouve la carte
              col: la colonne où se trouve la carte
              numTresor: le numéro du trésor à prendre sur la carte
  resultat: un booléen indiquant si le trésor était bien sur la carte considérée
  """

  if getTresor(plateau['Matrice'][lig][col]) == numTresor:
    prendreTresor(plateau['Matrice'][lig][col])
    return True
  else:
    return False
           
def getCoordonneesTresor(plateau,numTresor):
  """
  retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
  paramètres: plateau: le plateau considéré
              numTresor: le numéro du trésor à trouver
  resultat: un couple d'entier donnant les coordonnées du trésor ou None si
            le trésor n'est pas sur le plateau
  """
  
  for i in range(getNbLignes(plateau['Matrice'])):
    for j in range(getNbColonnes(plateau['Matrice'])):
      if getTresor(plateau['Matrice'][i][j]) == numTresor:
        return i, j
  return None

def getCoordonneesJoueur(plateau,numJoueur):
  """
  retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
  paramètres: plateau: le plateau considéré
              numJoueur: le numéro du joueur à trouver
  resultat: un couple d'entier donnant les coordonnées du joueur ou None si
            le joueur n'est pas sur le plateau
  """
  for i in range(getNbLignes(plateau['Matrice'])):
    for j in range(getNbColonnes(plateau['Matrice'])):
      if getListePions(plateau['Matrice'][i][j]) == numJoueur:
        return i, j
  return None
    

def prendrePionPlateau(plateau,lig,col,numJoueur):
  """
  prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
  paramètres: plateau:le plateau considéré
              lig: numéro de la ligne où se trouve le pion
              col: numéro de la colonne où se trouve le pion
              numJoueur: le numéro du joueur qui correspond au pion
  Cette fonction ne retourne rien mais elle modifie le plateau
  """
  if getNbPions(plateau['Matrice'][lig][col]) == numJoueur:
    prendrePion(plateau['Matrice'][lig][col], numJoueur)
    

def poserPionPlateau(plateau,lig,col,numJoueur):
  """
  met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
  paramètres: plateau:le plateau considéré
              lig: numéro de la ligne où se trouve le pion
              col: numéro de la colonne où se trouve le pion
              numJoueur: le numéro du joueur qui correspond au pion
  Cette fonction ne retourne rien mais elle modifie le plateau
  """
  poserPion(plateau['Matrice'][lig][col], numJoueur)

def accessible(plateau,ligD,colD,ligA,colA):
  """
  indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
  paramètres: plateau: le plateau considéré
              ligD: la ligne de la case de départ
              colD: la colonne de la case de départ
              ligA: la ligne de la case d'arrivée
              colA: la colonne de la case d'arrivée
  résultat: un boolean indiquant s'il existe un chemin entre la case de départ
            et la case d'arrivée
  """ 
  cartAccessibles = [[ligD,colD]]
  
  for i in range(getNbLignes(plateau['Matrice'])*getNbColonnes(plateau['Matrice'])):
    if i==(len(cartAccessibles)):
      return False

    elif cartAccessibles[i][0]>=1:
      if passageNord(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]-1][cartAccessibles[i][1]]) and [cartAccessibles[i][0]-1,cartAccessibles[i][1]] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0]-1,cartAccessibles[i][1]])
    
    if cartAccessibles[i][0]<=5:
      if passageSud(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]+1][cartAccessibles[i][1]]) and [cartAccessibles[i][0]+1,cartAccessibles[i]  [1]] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0]+1,cartAccessibles[i][1]])
    
    if cartAccessibles[i][1]<=5:
      if passageEst(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]+1]) and [cartAccessibles[i][0],cartAccessibles[i]  [1]+1] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0],cartAccessibles[i][1]+1])
    
    if cartAccessibles[i][1]>=1:
      if passageOuest(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]-1]) and [cartAccessibles[i][0],cartAccessibles[i][1]-1] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0],cartAccessibles[i][1]-1])
    
    if [ligA, colA] in cartAccessibles:
      return True

def accessibleDist(plateau,ligD,colD,ligA,colA):
  """
  indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
  mais la valeur de retour est None s'il n'y a pas de chemin, 
  sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
  de coordonées (couple de (lig,col))
  paramètres: plateau: le plateau considéré
              ligD: la ligne de la case de départ
              colD: la colonne de la case de départ
              ligA: la ligne de la case d'arrivée
              colA: la colonne de la case d'arrivée
  résultat: une liste de coordonées indiquant un chemin possible entre la case
            de départ et la case d'arrivée
  """
  cartAccessibles = [[ligD,colD]]
  route = None
  chemin = []
  
  for i in range(getNbLignes(plateau['Matrice'])*getNbColonnes(plateau['Matrice'])):
    if i==(len(cartAccessibles)):
      return route

    elif cartAccessibles[i][0]>=1:
      if passageNord(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]-1][cartAccessibles[i][1]]) and [cartAccessibles[i][0]-1,cartAccessibles[i][1]] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0]-1,cartAccessibles[i][1]])
      if [ligA, colA] in cartAccessibles:
        route = cartAccessibles
    
    if cartAccessibles[i][0]<=5:
      if passageSud(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]+1][cartAccessibles[i][1]]) and [cartAccessibles[i][0]+1,cartAccessibles[i]  [1]] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0]+1,cartAccessibles[i][1]])
      if [ligA, colA] in cartAccessibles:
        route = cartAccessibles
    
    if cartAccessibles[i][1]<=5:
      if passageEst(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]+1]) and [cartAccessibles[i][0],cartAccessibles[i]  [1]+1] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0],cartAccessibles[i][1]+1])
      if [ligA, colA] in cartAccessibles:
        route = cartAccessibles
    
    if cartAccessibles[i][1]>=1:
      if passageOuest(plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]],plat['Matrice'][cartAccessibles[i][0]][cartAccessibles[i][1]-1]) and [cartAccessibles[i][0],cartAccessibles[i][1]-1] not in cartAccessibles:
        cartAccessibles.append([cartAccessibles[i][0],cartAccessibles[i][1]-1])
      if [ligA, colA] in cartAccessibles:
        route = cartAccessibles

  for i in range(len(route)):
    for j in range(len(route)-1,0,-1):
      if route[i+1][0]==route[i][0]+1 or route[i+1][0]==route[i][0]-1:
        chemin.append(route[i])
      if route[j+1][0]==route[i][0]+1 or route[j+1][0]==route[i][0]-1:
        chemin.append(route[j])
  
  return chemin

'''if __name__ == '__main__':
  plat = Plateau(4, 5)
  print('Vérification création du plateau:',plat)
  print('Vérification création cartes amovibles:',creerCartesAmovibles(1,5))
  print('Vérification suppression du trésor:', prendreTresorPlateau(plat,0,0,1))
  print('Vérification coordonnées trésor:', getCoordonneesTresor(plat,2))
  print('Vérification coordonnées joueur:', getCoordonneesJoueur(plat, 1))
  prendrePionPlateau(plat,0,1,3)
  print('Vérification suppresion pion en lig,col:', plat)
  poserPionPlateau(plat,0,1,4)
  print('Vérification pose pion en lig,col:', plat)
  print('Verification accessibilité chemin:', accessible(plat,6,6,5,5))
  print('Verification chemin:', accessibleDist(plat,6,6,5,5))'''