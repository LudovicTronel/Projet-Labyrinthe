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
    m={nbJoueurs,nbTresors}
    c={'Matrice': Matrice(7,7),'Carte': Carte(False,False,False,False)}
		
	setVal(c['Matrice'],0,0,toChar(Carte(True,False,False,True)))
	setVal(c['Matrice'],0,2,toChar(Carte(True,False,False,False)))
	setVal(c['Matrice'],0,4,toChar(Carte(True,False,False,False)))
	setVal(c['Matrice'],0,6,toChar(Carte(True,True,False,False)))

	setVal(c['Matrice'],2,0,toChar(Carte(False,False,False,True)))
	setVal(c['Matrice'],2,2,toChar(Carte(False,False,False,True)))
	setVal(c['Matrice'],2,4,toChar(Carte(True,False,False,False)))
	setVal(c['Matrice'],2,6,toChar(Carte(False,True,False,False)))

	setVal(c['Matrice'],4,0,toChar(Carte(False,False,False,True)))
	setVal(c['Matrice'],4,2,toChar(Carte(False,False,True,False)))
	setVal(c['Matrice'],4,4,toChar(Carte(False,True,False,False)))
	setVal(c['Matrice'],4,6,toChar(Carte(False,True,False,False)))

	setVal(c['Matrice'],6,0,toChar(Carte(False,False,True,True)))
	setVal(c['Matrice'],6,2,toChar(Carte(False,False,True,False)))
	setVal(c['Matrice'],6,4,toChar(Carte(False,False,True,False)))
	setVal(c['Matrice'],6,6,toChar(Carte(False,True,True,False)))

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
   	#création Cartes Amovibles Angles x16
	cA1={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)} #mettre tresor aléatoire 
	cA2={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)} #enlever matrice(7,7)??? 
	cA3={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA4={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA5={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA6={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA7={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA8={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA9={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA10={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA11={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA12={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA13={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA14={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA15={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cA16={'Matrice':Matrice(7,7), 'Carte':Carte(True,False,False,True)}
	cAngle=[cA1,cA2,cA3,cA4,cA5,cA6,cA7,cA8,cA9,cA10,cA11,cA12,cA13,cA14,cA15,cA16]

	#création Cartes Amovibles Jonctions x6
	cJ1={'Matrice':Matrice(7,7), 'Carte':Carte(False,False,False,True)}
	cJ2={'Matrice':Matrice(7,7), 'Carte':Carte(False,False,False,True)}
	cJ3={'Matrice':Matrice(7,7), 'Carte':Carte(False,False,False,True)}
	cJ4={'Matrice':Matrice(7,7), 'Carte':Carte(False,False,False,True)}
	cJ5={'Matrice':Matrice(7,7), 'Carte':Carte(False,False,False,True)}
	cJ6={'Matrice':Matrice(7,7), 'Carte':Carte(False,False,False,True)}
	cJonction=[cJ1,cJ2,cJ3,cJ4,cJ5,cJ6]

	#création Cartes Amovibles ToutDroits x12
	cDT1={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT2={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT3={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT4={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT5={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT6={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT7={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT8={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT9={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT10={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT11={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cDT12={'Matrice':Matrice(7,7),'Carte':Carte(False,True,False,True)}
	cToutDroit=[cDT1,cDT2,cDT3,cDT4,cDT5,cDT6,cDT7,cDT8,cDT9,cDT10,cDT11,cDT12]

	ListeCarte=cAngle+cJonction+cToutDroit
	random.shuffle(ListeCarte)
	return ListeCarte
	print(ListeCarte)

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
