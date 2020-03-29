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
    
    #créer la matrice
    m=Matrice(7,7)
    m={nbJoueurs,nbTresors}

    #creer et placer les 16 cartes fixes du plateau:
    setVal(matrice,0,0,Carte(True,False,False,True)) #coins 1er joueur(pas de trésor)
    setVal(matrice,0,3,Carte(True,False,False,False))
    setVal(matrice,0,5,Carte(True,False,False,False))
    setVal(matrice,0,7,Carte(True,True,False,False)) #coins 2e joueur(pas de trésor)

    setVal(matrice,3,0,Carte(False,False,False,True))
    setVal(matrice,3,3,Carte(False,False,False,True))
    setVal(matrice,3,5,Carte(True,False,False,False))
    setVal(matrice,3,7,Carte(False,True,False,False))

    setVal(matrice,5,0,Carte(False,False,False,True))
    setVal(matrice,5,3,Carte(False,False,True,False))
    setVal(matrice,5,5,Carte(False,True,False,False))
    setVal(matrice,5,7,Carte(False,True,False,False))

    setVal(matrice,7,0,Carte(False,False,True,True)) #coins 3e joueur(pas de trésor)
    setVal(matrice,7,3,Carte(False,False,True,False))
    setVal(matrice,7,5,Carte(False,False,True,False))
    setVal(matrice(7,7,Carte(False,True,True,False)) #coins 4e joueur(pas de trésor)

           #manque initier carte amovible en dehors du plateau
    return m 
           
def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    CarteAmovible=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33] #liste des cartes amovibles (49-16 cartes fixes -1 carte en de hors du plateau)
    nbTresors=[]
    i=0
    #manque tresorDebut??
           
    for elem in (CarteAmovible):
           CarteAmovible[i]=nbTresors #pour chaque indice de la liste, y ajouter un tresor ??
           random.shuffle(CarteAmovible)#mélanger aléatoirement la liste
           
    return CarteAmovible

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
           
    if numTresor in plateau['numTresor'[lig][col]]:
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
           
           
    if numTresor in plateau['numTresor'[lig][col]]:
           return lig,col
    else:
           return None 
           

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    if numJoueur in plateau['numJoueur'[lig][col]]:
           return lig,col
    else:
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
    pion = plateau[numJoueur[lig][col]] 
    

def poserPionPlateau(plateau,lig,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lig: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    plateau['pion']=plateau[numJoueur[lig][col]]

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
    "Essayer avec la récursivité"

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
    pass  
