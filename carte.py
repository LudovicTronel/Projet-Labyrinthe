# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']

def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)"""
    carte = {'Nord': nord, 'Est': est, 'Sud': sud, 'Ouest': ouest, 'Tresor': tresor, 'Pions': pions}
    return carte

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    mur = 0
    if c['Nord'] == True:
        mur = mur+1
    if c['Est'] == True:
        mur = mur+1
    if c['Sud'] == True:
        mur = mur+1
    if c['Ouest'] == True:
        mur = mur+1
    if mur<=2:
        return True
    else:
        return False
        
def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c['Nord']

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c['Sud']

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c['Est']

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c['Ouest']

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c['Pions']

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c['Pions'] = listePions

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c['Pions'])

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    if pion in c['Pions']:
        return True
    else:
        return False

def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c['Tresor']

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    tres = c['Tresor']
    c['Tresor'] = 0
    return tres

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    tres = c['Tresor']
    c['Tresor'] = tresor
    return tres

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    for i in range(getNbPions(c)):
      if c['Pions'][i]==pion:
        supp = i
    del c['Pions'][supp]
    
def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c['Pions']:
        c['Pions'].append(pion)
        
def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    a = c['Nord']
    c['Nord'] = c['Ouest']
    c['Ouest'] = c['Sud']
    c['Sud'] = c['Est']
    c['Est'] = a

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    a = c['Nord']
    c['Nord'] = c['Est']
    c['Est'] = c['Sud']
    c['Sud'] = c['Ouest']
    c['Ouest'] = a
    
def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    tour = random.randint(0, 4)
    for i in range(tour):
        tournerHoraire(c)
    
def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    bN = bE = bS = bO = 0
    for i in range(len(c)):
        if c['Nord'] == True:
            bN = 1
        if c['Est'] == True:
            bE = 1
        if c['Sud'] == True:
            bS = 1
        if c['Ouest'] == True:
            bO = 1
    return int((bN*2**0)+(bE*2**1)+(bS*2**2)+(bO*2**3))

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
    unite = code %10
    dizaine = ((code - unite) / 10) %10
    centaine = ((code - unite - 10 * dizaine) / 100) %10
    millier = ((code - unite - 10 * dizaine - 100 * centaine) / 1000)
    c['Nord'] = c['Est'] = c['Sud'] = c['Ouest'] = False
    for i in range(len(c)-2):
        if unite == 1:
            c['Nord'] = True
        if dizaine == 1:
            c['Est'] = True
        if centaine == 1:
            c['Sud'] = True
        if millier == 1:
            c['Ouest'] = True
    
def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    return listeCartes[coderMurs(c)]
    
def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['Nord'] == False and carte2['Sud'] == False:
        return True
    else: 
        return  False

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['Sud'] == False and carte2['Nord'] == False:
        return True
    else: 
        return  False
    
def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['Ouest'] == False and carte2['Est'] == False:
        return True
    else: 
        return  False
        
def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    if carte1['Est'] == False and carte2['Ouest'] == False:
        return True
    else: 
        return  False

if __name__=='__main__':
    c = Carte(False, True, True, False, 1)
    c1 = Carte(False, False, True, False)
    c2 = Carte(False, False, False, True)
    print('Paramètres de la carte:',c)
    print('La carte est-elle valide ?', estValide(c))
    print('La carte possède un mur au Nord ?', murNord(c))
    print('La carte possède un mur au Est ?', murEst(c))
    print('La carte possède un mur au Sud ?', murSud(c))
    print('La carte possède un mur au Ouest ?', murOuest(c))
    print('La liste des pions sur la carte est: ',getListePions(c))
    print('La carte contient ', getNbPions(c), ' pion(s)')
    setListePions(c, [1,3])
    print('Nouveaux paramètres de la carte: ',c)
    print('La carte contient-elle le pion demandé ?', possedePion(c,2))
    print('La carte renferme le trésor n° ', getTresor(c))
    print('Le tresor n°', prendreTresor(c),' va être enlevé')
    print('L ancien trésor était le n°', mettreTresor(c, 1))
    prendrePion(c, 3)
    print('Verification de la suppresion du pion', c)
    poserPion(c, 2)
    print('Verification de l ajout du pion', c)
    tournerHoraire(c)
    print('Verification de la rotation horaite', c)
    tournerAntiHoraire(c)
    print('Verification de la rotation antihoraire', c)
    tourneAleatoire(c)
    print('Verification de la rotation aléatoire', c)
    print('Verification du code des murs de la carte est:', coderMurs(c))
    decoderMurs(c, 1000)
    print('Verification pour le decodage des murs:', c) 
    print('Le caractère semi-graphique de la carte est:',toChar(c))
    print('Passage au Nord possible: ',passageNord(c1, c2))
    print('Passage à l Est possible: ',passageEst(c1, c2))
    print('Passage au Sud possible: ',passageSud(c1, c2))
    print('Passage à l Ouest possible: ',passageOuest(c1, c2))
