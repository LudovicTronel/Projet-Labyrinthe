# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module joueur
   ~~~~~~~~~~~~~
   
   Ce module gère un joueur. 
"""

def Joueur(nom):
    """creer un nouveau joueur portant le nom passé en paramètre. Ce joueur possède une liste de trésors à trouver vide
    paramètre: nom une chaine de caractères
    retourne le joueur ainsi créé"""
    return (nom, [])
    
def ajouterTresor(joueur,tresor):
    """
    ajoute un trésor à trouver à un joueur (ce trésor sera ajouter en fin de liste) Si le trésor est déjà dans la liste des trésors à trouver la fonction ne fait rien
    paramètres:
        joueur le joueur à modifier
        tresor un entier strictement positif
    la fonction ne retourne rien mais modifie le joueur"""
    if tresor not in joueur[1]:
        joueur[1].append(tresor)
        
def prochainTresor(joueur):
    """
    retourne le prochain trésor à trouver d'un joueur, retourne None si aucun trésor n'est à trouver
    paramètre:
        joueur le joueur
    résultat un entier représentant le trésor ou None
    """
    if joueur[1]==[]:
        return None
    else:
        return joueur[1][0]
        
def tresorTrouve(joueur):
    """ 
    enlève le premier trésor à trouver car le joueur l'a trouvé
    paramètre:
        joueur le joueur
    la fonction ne retourne rien mais modifie le joueur
    """
    del joueur[1][0]
    
def getNbTresorsRestants(joueur):
    """
    retourne le nombre de trésors qu'il reste à trouver
    paramètre: joueur le joueur
    résultat: le nombre de trésors attribués au joueur
    """
    return len(joueur[1])
    
def getNom(joueur):
    """
    retourne le nom du joueur
    paramètre: joueur le joueur
    résultat: le nom du joueur 
    """
    return joueur[0]

if __name__=='__main__':
  j1 = Joueur('Ludovic')
  print('Nouveau Joueur:',j1)
  ajouterTresor(j1, 1)
  print('Ajout d un premier trésor:', j1)
  ajouterTresor(j1, 2)
  print('Ajout d un deuxieme trésor:',j1)
  print('Le prochain trésor à trouver porte le n°', prochainTresor(j1))
  print('Liste des trésors avant découverte:',j1)
  tresorTrouve(j1)
  print('Liste des trésors après découverte:',j1)
  print('Il reste',getNbTresorsRestants(j1), 'trésor à trouver')
  print('Le joueur est',getNom(j1))