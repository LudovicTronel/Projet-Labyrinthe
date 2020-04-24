# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module labyrinthe
   ~~~~~~~~~~~~~~~~~
   
   Ce module gère sur le jeu du labyrinthe (observation et mise à jour du jeu).
"""

from listeJoueurs import *
from plateau import *


def Labyrinthe(nomsJoueurs=["joueur1","joueurs2"],nbTresors=24, nbTresorsMax=0):
    """
    permet de créer un labyrinthe avec nbJoueurs joueurs, nbTresors trésors
    chacun des joueurs aura au plus nbTresorMax à trouver
    si ce dernier paramètre est à 0, on distribuera le maximum de trésors possible 
    à chaque joueur en restant équitable
    un joueur courant est choisi et la phase est initialisée
    paramètres: nomsJoueurs est la liste des noms des joueurs participant à la partie (entre 1 et 4)
                nbTresors le nombre de trésors différents il en faut au moins 12 et au plus 49
                nbTresorMax le nombre de trésors maximum distribué à chaque joueur
    résultat: le labyrinthe crée
    """
    lab = {'Joueurs': ListeJoueurs(nomsJoueurs), 'nbJoueurs': 0, 'nbTresors': nbTresors, 'nbTresorsMax': nbTresorsMax, 'Plateau': Plateau(len(nomsJoueurs), nbTresors), 'Phase': 1, 'CoupInterdit': ('O', 0)}
    lab['nbJoueurs'] = getNbJoueurs(lab['Joueurs'])
    initAleatoireJoueurCourant(lab['Joueurs'])
    distribuerTresors(lab['Joueurs'],nbTresors, nbTresorsMax)
    return lab

def getPlateau(labyrinthe):
    """
    retourne la matrice représentant le plateau de jeu
    paramètre: labyrinthe le labyrinthe considéré
    résultat: la matrice représentant le plateau de ce labyrinthe
    """
    return labyrinthe['Plateau']

def getNbParticipants(labyrinthe):
    """
    retourne le nombre de joueurs engagés dans la partie
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de joueurs de la partie
    """
    return labyrinthe['nbJoueurs']

def getNomJoueurCourant(labyrinthe):
    """
    retourne le nom du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nom du joueurs courant
    """
    return nomJoueurCourant(labyrinthe['Joueurs'])

def getNumJoueurCourant(labyrinthe):
    """
    retourne le numero du joueur courant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numero du joueurs courant
    """
    return numJoueurCourant(labyrinthe['Joueurs'])

def getPhase(labyrinthe):
    """
    retourne la phase du jeu courante
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le numéro de la phase de jeu courante
    """   
    return labyrinthe['Phase']

def changerPhase(labyrinthe):
    """
    change de phase de jeu en passant la suivante
    paramètre: labyrinthe le labyrinthe considéré
    la fonction ne retourne rien mais modifie le labyrinthe
    """    
    labyrinthe['Phase']+=1

def getNbTresors(labyrinthe):
    """
    retourne le nombre de trésors qu'il reste sur le labyrinthe
    paramètre: labyrinthe le labyrinthe considéré
    résultat: le nombre de trésors sur le plateau
    """    
    totres = 0
    for i in range(getNbParticipants(labyrinthe)):
      totres += nbTresorsRestantsJoueur(labyrinthe['Joueurs'],i)
    return totres
    
def getListeJoueurs(labyrinthe):
    """
    retourne la liste joueur structures qui gèrent les joueurs et leurs trésors
    paramètre: labyrinthe le labyrinthe considéré
    résultat: les joueurs sous la forme de la structure implémentée dans listeJoueurs.py    
    """
    return labyrinthe['Joueurs']

def enleverTresor(labyrinthe,lig,col,numTresor):
    """
    enleve le trésor numTresor du plateau du labyrinthe. 
    Si l'opération s'est bien passée le nombre total de trésors dans le labyrinthe
    est diminué de 1
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    la fonction ne retourne rien mais modifie le labyrinthe
    """
    prendreTresorPlateau(getPlateau(labyrinthe),lig,col,numTresor)
    
def prendreJoueurCourant(labyrinthe,lig,col):
    """
    enlève le joueur courant de la carte qui se trouve sur la case lin,col du plateau
    si le joueur ne s'y trouve pas la fonction ne fait rien
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe    
    """
    if getCoordonneesJoueur(getPlateau(labyrinthe), getNumJoueurCourant(labyrinthe)) == (lig, col):
      prendrePionPlateau(get, lig, col, getNumJoueurCourant(labyrinthe)+1)

def poserJoueurCourant(labyrinthe,lig,col):
    """
    pose le joueur courant sur la case lin,col du plateau
    paramètres: labyrinthe: le labyrinthe considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
    la fonction ne retourne rien mais modifie le labyrinthe     
    """
    poserPionPlateau(getPlateau(labyrinthe), lig, col, getNumJoueurCourant(labyrinthe)+1)

def getCarteAJouer(labyrinthe):
    """
    donne la carte à jouer
    paramètre: labyrinthe: le labyrinthe considéré
    résultat: la carte à jouer    
    """    
    return labyrinthe['Plateau'][1]

def coupInterdit(labyrinthe,direction,rangee):
    """ 
    retourne True si le coup proposé correspond au coup interdit
    elle retourne False sinon
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    résultat: un booléen indiquant si le coup est interdit ou non
    """
    if direction in ('O', 'E') and labyrinthe['CoupInterdit'][0] in ('O', 'E') and direction != labyrinthe['CoupInterdit'][0] and rangee == labyrinthe['CoupInterdit'][1]:
      return True
    elif direction in ('N', 'S') and labyrinthe['CoupInterdit'][0] in ('N', 'S') and direction != labyrinthe['CoupInterdit'][0] and rangee == labyrinthe['CoupInterdit'][1]:
      return True
    else:
      return False

def jouerCarte(labyrinthe,direction,rangee):
    """
    fonction qui joue la carte amovible dans la direction et sur la rangée passées 
    en paramètres. Cette fonction
       - met à jour le plateau du labyrinthe
       - met à jour la carte à jouer
       - met à jour la nouvelle direction interdite
    paramètres: labyrinthe: le labyrinthe considéré
                direction: un caractère qui indique la direction choisie ('N','S','E','O')
                rangee: le numéro de la ligne ou de la colonne choisie
    Cette fonction ne retourne pas de résultat mais met à jour le labyrinthe
    """
    if direction == 'N':
        carte = decalageColonneEnBas(getPlateau(labyrinthe)[0], rangee, getCarteAJouer(labyrinthe))
    elif direction == 'S':
        carte = decalageColonneEnHaut(getPlateau(labyrinthe)[0], rangee, getCarteAJouer(labyrinthe))
    elif direction == 'E':
        carte = decalageLigneAGauche(getPlateau(labyrinthe)[0], rangee, getCarteAJouer(labyrinthe))
    elif direction == 'O':
        carte = decalageLigneADroite(getPlateau(labyrinthe)[0], rangee, getCarteAJouer(labyrinthe))
    
    labyrinthe['CoupInterdit'] = (direction, rangee)

def tournerCarte(labyrinthe,sens='H'):
    """
    tourne la carte à jouer dans le sens indiqué en paramètre (H horaire A antihoraire)
    paramètres: labyrinthe: le labyrinthe considéré
                sens: un caractère indiquant le sens dans lequel tourner la carte
     Cette fonction ne retourne pas de résultat mais met à jour le labyrinthe    
    """
    if sens=='H':
      tournerHoraire(getCarteAJouer(labyrinthe))
    elif sens=='A':
      tournerAntiHoraire(getCarteAJouer(labyrinthe))

def getTresorCourant(labyrinthe):
    """
    retourne le numéro du trésor que doit cherche le joueur courant
    paramètre: labyrinthe: le labyrinthe considéré 
    resultat: le numéro du trésor recherché par le joueur courant
    """
    return prochainTresorJoueur(labyrinthe['Joueurs'],getNumJoueurCourant(labyrinthe))

def getCoordonneesTresorCourant(labyrinthe):
    """
    donne les coordonnées du trésor que le joueur courant doit trouver
    paramètre: labyrinthe: le labyrinthe considéré 
    resultat: les coordonnées du trésor à chercher ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesTresor(getPlateau(labyrinthe), getTresorCourant(labyrinthe))

def getCoordonneesJoueurCourant(labyrinthe):
    """
    donne les coordonnées du joueur courant sur le plateau
    paramètre: labyrinthe: le labyrinthe considéré 
    resultat: les coordonnées du joueur courant ou None si celui-ci 
              n'est pas sur le plateau
    """
    return getCoordonneesJoueur(getPlateau(labyrinthe), getNumJoueurCourant(labyrinthe))

def executerActionPhase1(labyrinthe,action,rangee):
    """
    exécute une action de jeu de la phase 1
    paramètres: labyrinthe: le labyrinthe considéré
                action: un caractère indiquant l'action à effecter
                        si action vaut 'T' => faire tourner la carte à jouer
                        si action est une des lettres N E S O et rangee est un des chiffre 1,3,5 
                        => insèrer la carte à jouer à la direction action sur la rangée rangee
                           et faire le nécessaire pour passer en phase 2
    résultat: un entier qui vaut
              0 si l'action demandée était valide et demandait de tourner la carte
              1 si l'action demandée était valide et demandait d'insérer la carte
              2 si l'action est interdite car l'opposée de l'action précédente
              3 si action et rangee sont des entiers positifs
              4 dans tous les autres cas
    """
    if action == 'T':
      tournerCarte(labyrinthe)
      return 0
    elif action in ('N', 'E', 'S', 'O') and rangee in (1, 3, 5):
      if coupInterdit(labyrinthe,action,rangee):
        return 2
      else:
        jouerCarte(labyrinthe,action,rangee)
        changerPhase(labyrinthe)
        return 1
    elif int(action) and int(rangee):
      return 3
    else: 
      return 4
      

def accessibleDistJoueurCourant(labyrinthe, ligA,colA):
    """
    verifie si le joueur courant peut accéder la case ligA,colA
    si c'est le cas la fonction retourne une liste représentant un chemin possible
    sinon ce n'est pas le cas, la fonction retourne None
    paramètres: labyrinthe le labyrinthe considéré
                ligA la ligne de la case d'arrivée
                colA la colonne de la case d'arrivée
    résultat: une liste de couples d'entier représentant un chemin que le joueur
              courant atteigne la case d'arrivée s'il existe None si pas de chemin
    """
    coordJC = getCoordonneesJoueurCourant(labyrinthe)
    return accessibleDist(getPlateau(labyrinthe), coordJC[0], coordJC[1], ligA, colA)

def finirTour(labyrinthe):
    """
    vérifie si le joueur courant vient de trouver un trésor (si oui fait le nécessaire)
    vérifie si la partie est terminée, si ce n'est pas le cas passe au joueur suivant
    paramètre: labyrinthe le labyrinthe considéré
    résultat: un entier qui vaut
              0 si le joueur courant n'a pas trouvé de trésor
              1 si le joueur courant a trouvé un trésor mais la partie n'est pas terminée
              2 si le joueur courant a trouvé son dernier trésor (la partie est donc terminée)
    """
    coordJC = getCoordonneesJoueurCourant(labyrinthe)
    coordTC = getCoordonneesTresorCourant(labyrinthe)
    if coordJC == coordTC:
      enleverTresor(labyrinthe, coordTC[0], coordTC[1], getTresorCourant(labyrinthe))
      joueurCourantTrouveTresor(labyrinthe['Joueurs'])
      if joueurCourantAFini(labyrinthe['Joueurs']):
        return 2
      else:
        changerJoueurCourant(labyrinthe['Joueurs'])
        return 1
    return 0

if __name__=='__main__':
  lab = Labyrinthe(nomsJoueurs=["Ludovic","Océanne"],nbTresors=12, nbTresorsMax=0)
  print('L initialisation du labyrinthe est:',lab)
  print('Le plateau du labyrinthe est:',getPlateau(lab))
  print('Il y a',getNbParticipants(lab),'participant(s) dans la partie.')
  print('Le joueur courant est:',getNomJoueurCourant(lab))
  print('Le numéro du joueur courant est:',getNumJoueurCourant(lab))
  print('La phase',getPhase(lab), 'est en cours.')
  changerPhase(lab)
  print('Verification du changement de phase, la phase', getPhase(lab), 'est désormais engagée.')
  print('Il reste',getNbTresors(lab), 'trésor(s) dans le labyrinthe.')
  print('La liste des joueurs est:', getListeJoueurs(lab))
  enleverTresor(lab,4,6,3)
  print('Verification de la suppression du trésor:', getNbTresors(lab))
  prendreJoueurCourant(lab,4,5)
  print('Verification de l enlèvement du joueur courant:', lab)
  poserJoueurCourant(lab,6,5)
  print('Verification du placement joueur courant:', lab)                                             #Fonction marche mais ajoute le pion à toutes les cartes 
  print('Verification carte à jouer:', getCarteAJouer(lab))
  print('Verification de la possibilité du coup proposé: ',coupInterdit(lab,'E',1))
  jouerCarte(lab,'N',3)
  print('Verification de la mise en jeu de la carte:', lab)
  tournerCarte(lab,sens='H')
  print('Verification de la rotation de la carte à jouer: ', lab)
  print('Le prochain trésor à trouver pour le joueur courant porte le n°',getTresorCourant(lab))
  print('Le tresor que le joueur courant doit trouvé a pour coordonnées:', getCoordonneesTresorCourant(lab))
  print('Le joueur courant a pour coordonnées:', getCoordonneesJoueurCourant(lab))
  print('Verification de l execution de la phase 1:',executerActionPhase1(lab,88,3))
  print('Verification de l acces depuis la case du joueur courant à la case demandée', accessibleDistJoueurCourant(lab, 5, 4))
  print('Verification de la fin du tour:', finirTour(lab))