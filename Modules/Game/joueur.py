if __name__ != "__main__":
    import Modules.fltk as fltk

def player_setup(joueur:list, NB_JOUEUR:int):
    player_number = 0
    joueur_name = ["David", "Walid", "Abdel", "Kader", "Rekia", "Stephany"]
    color = ["green", "red", "black", "blue", "yellow", "purple"]
    while player_number < NB_JOUEUR:
        joueur_dic =  {}
        joueur_dic["Prenom"] = joueur_name[player_number]
        joueur_dic['Color'] = color[player_number]
        joueur_dic['Balle'] = 0
        joueur.append(joueur_dic)
        player_number += 1 
    return joueur

def aff_joueur(LARGEUR_windows:int, turn: str, joueur:dict, NB_JOUEUR):
    """
    nb_balle_playeur: nombre de balle au debut du jeu par joueur
    debut_partie: qui nous previens si on est dans
                  la phase de placement des balle
    tour: nombre representant le joueur precedent a avoir jouer
    joueur: association du jour et de son nombre de balle
    fonction qui affiche les joueur sur les coins de l'écran
    et met l'affichage du joueur en couleur et les autres 
    """
    center = LARGEUR_windows/2
    taille = fltk.taille_texte(f" Placer une balle {joueur[turn%NB_JOUEUR]['Prenom']} ")
    fltk.rectangle(center - taille[0]/2, 0, center + taille[0]/2, taille[1], 
                   joueur[turn%NB_JOUEUR]['Color'], remplissage="#6495ED" ,epaisseur=3, tag="turn"
                   )
    fltk.texte(center, taille[1]/2, f"Placer une balle {joueur[turn%NB_JOUEUR]['Prenom']}", ancrage="center", tag="turn")
       
def aff_tour(LARGEUR_windows:int, joueur:list, playerTurn:int):
    """
    nb_balle_playeur: nombre de balle au debut du jeu par joueur
    debut_partie: qui nous previens si on est dans
                  la phase de placement des balle
    tour: nombre representant le joueur precedent a avoir jouer
    joueur: association du jour et de son nombre de balle
    fonction qui affiche les joueur sur les coins de l'écran
    et met l'affichage du joueur en couleur et les autres 
    """
    playerIndex = cherche_tour(playerTurn, joueur)
    center = LARGEUR_windows/2
    taille = fltk.taille_texte(f"Sélectionnez une tirette {joueur[playerIndex]['Prenom']}")
    fltk.rectangle(center - taille[0]/2, 0, center + taille[0]/2, taille[1], 
                   joueur[playerIndex]['Color'], remplissage="#6495ED" ,epaisseur=3, tag="turn"
                   )
    fltk.texte(center, taille[1]/2, f"Sélectionnez une tirette {joueur[playerIndex]['Prenom']}", ancrage="center", tag="turn")
    
def cherche_tour(playerNumber: int , playerlist: list):
    """
    tour: nombre representant le playerlist precedent a avoir jouer
    playerlist: association du jour et de son nombre de balle
    determine le tour du prohai  playerlist
    >>> cherche_tour(0,[{'Prenom': 'David', 'Color': 'green', 'Balle': 0}, {'Prenom': 'Walid', 'Color': 'red', 'Balle': 2}, {'Prenom': 'Abdel', 'Color': 'black', 'Balle': 2}])
    1
    >>> cherche_tour(1,[{'Prenom': 'David', 'Color': 'green', 'Balle': 1}, {'Prenom': 'Walid', 'Color': 'red', 'Balle': 2}, {'Prenom': 'Abdel', 'Color': 'black', 'Balle': 0}])
    1
    """
    if playerNumber == len(playerlist):#si on est a la fin de la liste
        playerNumber = 0
    if playerlist[playerNumber]['Balle'] == 0: #verifie si il a pas une balle en jeu
        playerNumber = cherche_tour(playerNumber + 1, playerlist)#on recherche avec le playerlist suivant
    return playerNumber

def aff_NbBallejoueur(tour: int, joueur: dict, nb_balle_player_max:int):
    """
    joueur_name: liste des noms des joueurs
    nb_balle_playeur: nombre de balle au debut du jeu par joueur
    debut_partie: qui nous previens si on est dans
                  la phase de placement des balle
    tour: nombre representant le joueur precedent a avoir jouer
    joueur: association du jour et de son nombre de balle
    fonction qui affiche les joueur sur les coins de l'écran
    et met l'affichage du joueur en couleur et les autres 
    """ 
    margin_ball = fltk.hauteur_fenetre() * 0.01
    allcoord = []
    sizeText = max([fltk.taille_texte(elem['Prenom']) for elem in joueur])
    for i in range(len(joueur)):
        if i%2 == 0:
            allcoord.append( (0, 0 + (i * (sizeText[1] + margin_ball))) )
        else:
            allcoord.append( (fltk.largeur_fenetre() - sizeText[0], 0 + ((i-1) * (sizeText[1] + margin_ball))) )
    for i, coord in enumerate(allcoord):
        ball_lost = nb_balle_player_max - joueur[i]['Balle']
        colorball_lost = joueur[i]['Color']
        if i == tour:
            playercolor = joueur[i]['Color']
        else:
            playercolor = "grey"    
        fltk.texte(coord[0], coord[1], joueur[i]['Prenom'], playercolor, tag="score")
        for i in range(ball_lost):
            fltk.cercle(coord[0] + margin_ball + (i*margin_ball*2), coord[1] + sizeText[1] + sizeText[1]/2 + margin_ball,
                        margin_ball, colorball_lost, colorball_lost, tag="score"
                        )
        
        

    


if __name__ == "__main__":
    import doctest
    doctest.testmod()