# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    liste = {'Joueurs': nomsJoueurs, 'JoueurCourant': 0}
    for i in range(len(nomsJoueurs)):
      nomsJoueurs[i] = Joueur(nomsJoueurs[i])
    return liste

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs une liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    
    joueurs['Joueurs'].append(joueur)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs['JoueurCourant'] = random.randint(0, len(joueurs['Joueurs'])-1)

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if nbTresorMax==0:
      nbTresorMax = nbTresors
    for j in range(len(joueurs['Joueurs'])):
      while len(joueurs['Joueurs'][j][1]) != nbTresorMax:
        nombraleatoire = random.randint(1, nbTresors)
        ajouterTresor(joueurs['Joueurs'][j], nombraleatoire)
    
def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    
    joueurs['JoueurCourant'] += 1
    if joueurs['JoueurCourant'] == len(joueurs['Joueurs']):
      joueurs['JoueurCourant'] = 0

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs['Joueurs'])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs['Joueurs'][joueurs['JoueurCourant']]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresorTrouve(getJoueurCourant(joueurs)) 

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return len(joueurs['Joueurs'][numJoueur-1][1])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs['JoueurCourant']+1

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return getNom(getJoueurCourant(joueurs))

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return getNom(joueurs['Joueurs'][numJoueur-1])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return prochainTresor(joueurs['Joueurs'][numJoueur-1])

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return prochainTresor(getJoueurCourant(joueurs))

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    return nbTresorsRestantsJoueur(joueurs,joueurs['JoueurCourant']) == 0

if __name__=='__main__':
  listenoms = ListeJoueurs(['Ludovic', 'Océanne', 'Damien'])
  print('Liste des joueurs:',listenoms)
  ajouterJoueur(listenoms, Joueur('Hector'))
  print('Ajout d un joueur:',listenoms)
  initAleatoireJoueurCourant(listenoms)
  print('Changement de joueur courant:',listenoms)
  print('Le joueur courant a-t-il fini ?', joueurCourantAFini(listenoms))
  distribuerTresors(listenoms,12, 4)
  print('Distribution des trésors:',listenoms)
  changerJoueurCourant(listenoms)
  print('Joueur courant suivant:',listenoms)
  print('Il y a',getNbJoueurs(listenoms),'joueur(s) dans la partie')
  print('Le joueur courant est',getJoueurCourant(listenoms))
  joueurCourantTrouveTresor(listenoms)
  print('Le joueur courant a trouvé un trésor:',listenoms)
  print('Il reste',nbTresorsRestantsJoueur(listenoms,0),'trésor(s) à trouver pour le joueur')
  print('Le joueur courant porte le n°', numJoueurCourant(listenoms))
  print('Le joueur courant se somme', nomJoueurCourant(listenoms))
  print('Le joueur s appelle',nomJoueur(listenoms, 2))
  print('Le prochain trésor à trouver pour', nomJoueur(listenoms, 1),'porte le n°',prochainTresorJoueur(listenoms,1))
  print('Le prochain trésor à trouver pour le joueur courant porte le n°', tresorCourant(listenoms))
  print('Le joueur courant a-t-il fini ?', joueurCourantAFini(listenoms))