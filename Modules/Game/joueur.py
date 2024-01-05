"""CODE FAIT PAR DAVID, ABDELKADER ET WALID."""

if __name__ != "__main__":
    import Modules.fltk as fltk

def player_setup(joueur:list, NB_JOUEUR:int):
    """
    Fonction qui va mettre en place les paramaètres de chaque joueurs sous forme de
    dictionnaire, chaque joueur a comme paramètres : "Prenom", "Color" et "Balle" (= NB de balle qu'il possède)
    
    Args:
        joueur (list): Liste de joueurs qu'on va renvoyer, initialement elle est vide.
        NB_JOUEUR (int): NB de joueurs qu'on a dans le jeu

    Returns:
        Liste où chaque élément est un dictionnaire avec les paramètres de chaques joueurs
    
    >>> player_setup([], 3)
    [{'Prenom': 'David', 'Color': 'green', 'Balle': 0}, {'Prenom': 'Walid', 'Color': 'red', 'Balle': 0}, {'Prenom': 'Abdel', 'Color': 'black', 'Balle': 0}]
    >>> player_setup([], 1)
    [{'Prenom': 'David', 'Color': 'green', 'Balle': 0}]
    >>> player_setup([], 0)
    []
    """
    # Variable pour savoir le nombre de joueur qu'on a crée dans la liste
    player_number = 0
    # On a 6 joueurs max car on a inscrit que 6 prénoms et couleurs. 
    joueur_name = ["David", "Walid", "Abdel", "Kader", "Rekia", "Stephany"]
    color = ["green", "red", "black", "blue", "yellow", "purple"]
    # Tant que le nombre de joueurs n'est pas égale au nombre de joueur prévu
    while player_number < NB_JOUEUR:
        joueur_dic =  {} # On crée un dictionnaire avec tous les paramètres 
        joueur_dic['Prenom'] = joueur_name[player_number]
        joueur_dic['Color'] = color[player_number]
        joueur_dic['Balle'] = 0
        joueur.append(joueur_dic)
        player_number += 1 
    return joueur

def aff_joueur(LARGEUR_windows:int, ball_place: int,  playerlist:int, NB_JOUEUR:int):
    """
    Fonction qui va afficher au-dessus du jeu, un rectangle qui monbtre 
    à quel joueur c'est au tour de jouer, le rectangle a la couleur du joueur 
    Paramètres:
        LARGEUR_windows (int): Largeur de la fenêtre (en px)
        ball_place (int): indice qui va permettre de connaître c'est le tour de qui
        playerList (dict): Liste où chaque élément est un dictionnaire avec les paramètres d'un joueur
        NB_JOUEUR (int): Nombre de joueur
    Return:
    fltk
    """
    # On affiche le bouton au centre
    center = LARGEUR_windows/2
    # La taille du rectangle est en fonction de la taille du texte
    # On fait une division euclidienne pour savoir c'est au tour de quelle joueur de placer une balle
    taille = fltk.taille_texte(f" Placer une balle {playerlist[ball_place%NB_JOUEUR]['Prenom']} ")
    # On divise par 2 car on veut le rayon
    fltk.rectangle(center - taille[0]/2, 0, center + taille[0]/2, taille[1], 
                   playerlist[ball_place%NB_JOUEUR]['Color'], remplissage="#6495ED" ,epaisseur=3, tag="turn"
                   )
    fltk.texte(center, taille[1]/2, f"Placer une balle {playerlist[ball_place%NB_JOUEUR]['Prenom']}", ancrage="center", tag="turn")
       
def aff_tour(LARGEUR_windows:int,  playerlist:list, playerTurn:int):
    """
    Fonction qui va afficher au même endroit où on a montré c'était au tour de qui de placer la balle,
    un rectangle qui va indiquer quel joueur doit tirer la tirette 

    Paramètres:
        LARGEUR_windows (int): Largeur de la fenêtre (en px)
        playerlist (_list_): Liste où chaque élément est un dictionnaire avec les paramètres d'un joueur
        playerTurn (int): Indice qui représente le tour du joueur (0 pour le 1er joueur, 1 pour le 2ème joueur ...)
    
    Return:
        fltk
    """
    # On veut que le rectangle soit au centre
    center = LARGEUR_windows/2
    # On calcule la taille du rectangle en fonction de la taille de la police 
    taille = fltk.taille_texte(f"Sélectionnez une tirette {playerlist[playerTurn]['Prenom']}")
    # On divise par 2 car on veut le rayon 
    fltk.rectangle(center - taille[0]/2, 0, center + taille[0]/2, taille[1], 
                   playerlist[playerTurn]['Color'], remplissage="#6495ED" ,epaisseur=3, tag="turn"
                   )
    # On divise par 2 car on veut que le point d'ancrage soit le centre du rectangle 
    fltk.texte(center, taille[1]/2, f"Sélectionnez une tirette {playerlist[playerTurn]['Prenom']}", ancrage="center", tag="turn")
    
def cherche_tour(playerTurn: int, playerlist: list):
    """
    Fonction qui va chercher c'est le tour de quel joueurs, si le
    joueur n'a plus de balle, alors il va vérfier le joueur suivant
    
    Paramètres:
        playerTurn (int): Indice qui représente le tour du joueur (0 pour le 1er joueur, 1 pour le 2ème joueur ...)
        playerlist (_list_): Liste où chaque élément est un dictionnaire avec les paramètres d'un joueur
    Return
        L'indice du joueur
    >>> cherche_tour(0,[{'Prenom': 'David', 'Color': 'green', 'Balle': 0}, {'Prenom': 'Walid', 'Color': 'red', 'Balle': 2}, {'Prenom': 'Abdel', 'Color': 'black', 'Balle': 2}])
    1
    >>> cherche_tour(1,[{'Prenom': 'David', 'Color': 'green', 'Balle': 1}, {'Prenom': 'Walid', 'Color': 'red', 'Balle': 2}, {'Prenom': 'Abdel', 'Color': 'black', 'Balle': 0}])
    1
    """
    if playerTurn == len(playerlist):# Si on est a la fin de la liste
        playerTurn = 0
    if playerlist[playerTurn]['Balle'] == 0: # Verifie s'il a pas de balle en jeu
        playerTurn = cherche_tour(playerTurn + 1, playerlist)# Si c'est le cas alors on recherche avec le joueur suivant
    return playerTurn

def aff_NbBallejoueur(tour: int, playerlist: dict, nb_balle_player_max:int):
    """
    Fonction qui va afficher les joueurs à gauche et droite de le fenêtre.
    Le joueur 1 sera à gauche, le joueur 2 à droite, le joueur 3 à gauche ...
    Donc les joueurs impairs à gauche et les joueurs pairs à droite 
    
    Elle va aussi afficher en dessous de chaque joueurs leurs nombre de balles qu'ils ont perdus 
    
    Paramètres:
        tour (int): Indice qui représente le tour du joueur (0 pour le 1er joueur, 1 pour le 2ème joueur ...)
        playerTurn (int): Indice qui représente le tour du joueur (0 pour le 1er joueur, 1 pour le 2ème joueur ...)
        nb_balle_player_max (int): Le nombre de balle max par joueur.
    
    Return
        fltk
    """ 
    # Marge qui va permettre de séparer les balles 
    margin_ball = fltk.hauteur_fenetre() * 0.01
    allcoord = []
    # La taille du texte sera égale à la taille du prénom le plus long dans la liste des prénoms 
    sizeText = max([fltk.taille_texte(elem['Prenom']) for elem in playerlist])
    # On calcule les coordonnées (x,y) de chaque joueur 
    for i in range(len(playerlist)):
        # On regarde si c'est pair ou impair 
        if i%2 == 0:
            allcoord.append( (0, 0 + (i * (sizeText[1] + margin_ball))) ) # Chaque joueur sont séparés par i fois la taille du texte + la marge de la balle
        else:
            allcoord.append( (fltk.largeur_fenetre() - sizeText[0], 0 + ((i-1) * (sizeText[1] + margin_ball))) ) # On fait -1 car le 2ème joueur est le 1er à gauche  
    # Puis on écrit le texte sur fltk
    for i, coord in enumerate(allcoord):
        # Pour calculer le nombre de balle qu'il a perdu on soustrait le nombre de balle max par le nombre de balle qu'il a actuellement
        ball_lost = nb_balle_player_max - playerlist[i]['Balle']
        colorball_lost = playerlist[i]['Color']
        if i == tour: # Si c'est le tour du joueur alors la couleur du pseudo est égale à sa couleur
            playercolor = playerlist[i]['Color']
        else:
            playercolor = "grey" # Sinon elle est grise
        # On place le texte à ses coordonnées respectives 
        fltk.texte(coord[0], coord[1], playerlist[i]['Prenom'], playercolor, tag="score")
        # Puis pour chaque balle perdu, on dessine un cercle espacé par le nombre de balle perdu
        for i in range(ball_lost):
            fltk.cercle(coord[0] + margin_ball + (i*margin_ball*2), coord[1] + sizeText[1] + sizeText[1]/2 + margin_ball,
                        margin_ball, colorball_lost, colorball_lost, tag="score")
        
        

    


if __name__ == "__main__":
    import doctest
    doctest.testmod()