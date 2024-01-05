"""CODE FAIT PAR DAVID, ABDELKADER ET WALID."""


if __name__ != "__main__":
    import Modules.fltk as fltk

import time
def verif_nombre_place(NB_BALLE:int, NB_JOUEUR:int, tirette_h:list, tirette_v:list):
    """
    Fonction qui va verifier si le nombre de balle que les joueurs
    doivent place est possible sur le plateau généré
    
    Paramètres:
        NB_BALLE : Nombre de balle par joueur
        NB_JOUEUR : Nombre de joueur
        tirette_h: La liste de True et de False pour les tirettes horizontales
        tirette_v: La liste de True et de False pour les tirettes verticales
    Return:
        Le nombre de balle par joueur, modifié par le code afin qu'on puisse jouer au jeu
    
    Les doctest marchent si on retire les fltk (Il y a un problème pour importer fltk car il est pas dans le même dossier)
    >>> verif_nombre_place(1, 3, [[False, True], [False, False]], [[False, True], [False, False]])
    
    >>> verif_nombre_place(2, 3, [[False, True], [False, False]], [[False, True], [False, False]])
    1
    >>> verif_nombre_place(100, 3, [[False, True], [False, False]], [[False, True], [False, False]])
    1
    """
    nb_case = len(tirette_h) # Pour éviter d'ajouter le paramètre NB_CASE
    nb_balle_dispo = 0
    # On regarde chaque case, et s'il y a une tirette alors on ajoute +1 au nombre de balle possible
    for i in range(nb_case):
        for j in range(nb_case):
            if (not tirette_h[i][j]) or (not tirette_v[i][j]):
                nb_balle_dispo += 1
    # Si le nombre de balle possible est inférieur au nombre de balle qu'on doit placer au total
    if nb_balle_dispo <= NB_BALLE*NB_JOUEUR:
        # Alors on affiche un texte qui nous informe que la valeur a été réduite
        HAUTEUR = fltk.hauteur_fenetre()
        LARGEUR = fltk.largeur_fenetre()
        chaine = f"Le nombre de balle par joueur a été réduit à {nb_balle_dispo // NB_JOUEUR} "
        # On utilise la fonction qui permet de trouver la taille de la police en fonction de la largeur d'un bouton;
        font_size = 1
        taille = fltk.taille_texte(chaine, taille=font_size) # on prend la taille du texte le plus long pour avoir la même taille
        while taille[0] <= LARGEUR*0.8: # 0.7 pour avoir de la marge entre le bouton
            font_size += 1 
            taille = fltk.taille_texte(chaine, taille=font_size)
        
        fltk.texte(LARGEUR / 2, HAUTEUR / 2, chaine, "black", taille=font_size, ancrage="center", tag="warning")
        fltk.mise_a_jour()
        time.sleep(2)
        fltk.efface("warning")
        # Et on return la nouvelle valeur pour jouer au jeu
        return nb_balle_dispo // NB_JOUEUR
    return NB_BALLE
        


def board_game(tile_hori:int, tile_verti:int, boxSize:tuple, coordinateNW:tuple):
    """
    Cette fonction qui va créer la liste nécessaire pour créer
    la grille de jeu
    
    Paramètres:
        tile_hori :  Nombre de case horizontale 
        tile_verti : Nombre de case verticale
        boxSize : Dimensions (x,y) d'une case
        coordinateNW : Coordonnées (x,y) de la fenêtre qu'on a crée (pour faire la marge avec la fenêtre windows) 
    
    Return:
        Une liste où chaque éléments sont des listes où chaque éléménts sont des listes avec son tuple de coordonnées (x,y) et une variable pour savoir si y a une balle ou non
        
    >>> board_game(2, 2, (50, 50), (10, 10))
    [[[(35.0, 35.0), '0'], [(85.0, 35.0), '0']], [[(35.0, 85.0), '0'], [(85.0, 85.0), '0']]]
    >>> board_game(0, 0, (0,0), (0, 0))
    []
    
    >>> board_game(0, 0, (50, 50), (10, 10))
    []
    """
    # Coordonnée de la première case (On divise par 2 car on veut le centre)
    x = coordinateNW[0] + boxSize[0]/2
    y = coordinateNW[1] + boxSize[1]/2 
    board_lst = []  # 1er liste 
    for i in range(tile_verti):
        board_line = [] # 2ème liste
        x = coordinateNW[0] + boxSize[0]/2
        for p in range(tile_hori):
             board_line.append([(x, y), "0"]) # 3ème liste 
             x += boxSize[0]     
        board_lst.append(board_line)
        y += boxSize[1]
    return board_lst

playerball = {}
def create_board(grid:list, boxDimensions:tuple, margin:tuple, tirette_h:list, tirette_v:list, ball_case, playercolor:str,
                 compteur_tiretteh:list, compteur_tirettev:list, playerlist:list, playerTurn:int):
    """
    Cette fonction va prendre la liste des cases et créer les cases en fonction des paramètres qui lui sont
    associés (s'il y a une tirette ou non, s'il y a une balle ou non ...).
    Elle va aussi permettre d'enlever les balles en fonction des mouvements de la tirette, elle va stocker la couleur du joueur qui
    l'a faite tomber.
    On crée la grille de jeu, puis on regarde la position des balles et s'il y a un trou sur la balle 
    Paramètres:
        grid: La liste crée avec la fonction précedente
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
        margin: Un tuple avec les marge (x,y) entre les cases
        tirette_h: La liste de True et de False pour les tirettes horizontales
        tirette_v: La liste de True et de False pour les tirettes verticales
        ball_case: L'indice x, y de la case qu'on a cliqué pour placer la balle
        playercolor: Couleur du joueur où c'est son tour
        compteur_tiretteh: Liste de dictionnaire avec le compteur gauche et droite de chaque tirette horizontale (1 de chaque côté par défault)
        compteur_tirettev: Liste de dictionnaire avec le compteur haut et bas de chaque tirette verticale (1 de chaque côté par défault)
        playerlist: Liste où chaque élément est un dictionnaire avec les paramètres de chaques joueurs
        playerTurn: int qui réprésente l'index du joueur qui joue dans la "playerlist"
    Return: 
        La grille de jeu sur fltk
    """
    # Création de la grille de jeu
    for y, line in enumerate(grid): # Pour chaque rangée de case ...
        for x, elem in enumerate(line): #Pour chaque case dans la rangée ...
            # On trace la contour de la case
            fltk.rectangle((elem[0][0] - boxDimensions[0]/2 + margin[0]),( elem[0][1] - boxDimensions[1]/2 + margin[1]), 
                           (elem[0][0] + boxDimensions[0]/2 - margin[0]),( elem[0][1] + boxDimensions[1]/2 - margin[1]),
                            "#aed4fb", remplissage="#6495ED" ,epaisseur=3, tag="board"
                          )
            # On appelle la fonction qui vérifie si y a une tirette ou pas dans la case
            # Et en fonction de la réponse il dessine l'image approprié. 
            if check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) == "Horizontale" :
                # On divise par 2 car on veut le rayon, et on divise par 5 car pour faire une tirette horizontale on veut que la largeur soit plus grande que la hauteur.
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 2 + margin[0] + 2, elem[0][1] - boxDimensions[1] / 5 + margin[1], # On fait +2 et -2 partour car il y a l'épaisseur de la case à retirer (épaisser=2)
                               elem[0][0] + boxDimensions[0] / 2 - margin[0] - 2, elem[0][1] + boxDimensions[1] / 5 - margin[1],
                               couleur="#D7BDE2", remplissage="#D7BDE2", tag="board")
            elif check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) == "Verticale" :
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 5 + margin[0], elem[0][1] - boxDimensions[1] / 2 + margin[1] + 2, 
                               elem[0][0] + boxDimensions[0] / 5 - margin[0], elem[0][1] + boxDimensions[1] / 2 - margin[1] - 2,
                               couleur="#ECF0F1", remplissage="#ECF0F1", tag="board")
            elif check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) == "Hori_et_Verti" :
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 2 + margin[0] + 2, elem[0][1] - boxDimensions[1] /  5 + margin[1], 
                               elem[0][0] + boxDimensions[0] / 2 - margin[0] - 2, elem[0][1] + boxDimensions[1] / 5 - margin[1],
                               couleur="#D7BDE2", remplissage="#D7BDE2", tag="board")
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 5 + margin[0], elem[0][1] - boxDimensions[1] / 2 + margin[1] + 2, 
                               elem[0][0] + boxDimensions[0] / 5 - margin[0], elem[0][1] + boxDimensions[1] / 2 - margin[1] - 2,
                               couleur="#ECF0F1", remplissage="#ECF0F1", tag="board")    
            # C'est là que la variable "0" dans chaque case va nous être utile pour détecter si on a une balle ou pas
            # ball_case renvoie l'indice (x,y) de la case qu'on a cliqué pour mettre la balle
            # Donc on vérifier d'abord qu'on a cliqué sur une case (elle renvoie False si on a cliqué sur autre choses que la case)
            if type(ball_case) != bool and (x == ball_case[0] and y == ball_case[1]): # Et on regarde si les coordonnées de la cases sont les mêmes
                if check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) != True : # On vérifie qu'on clique pas sur un trou
                    if elem[1] == "0": # Vérifier qu'il n'y a pas déja une balle
                        elem[1] = playercolor #  La variable devient la couleur du joueur qui a posé sa balle
            # Si c'est différent de "0" alors ça veut dire qu'il y a une balle sur la case  
            if elem[1] != "0" and type(elem[1]) != int: # != int car lorsqu'on fait tombé une balle, la case conserve l'indice du joueur qui l'a fait tombé
                # Si la case n'a toujours pas de trou après qu'on ai déplacé une tirette 
                if check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) != True:
                    # Alors on trace la balle comme convenu 
                    fltk.cercle(elem[0][0], elem[0][1], margin[0]*2 - boxDimensions[0] / 2.5, 
                                epaisseur=5, couleur=elem[1], remplissage=elem[1], tag=f"{elem[0]}")
                # Si la case à un trou après le déplacement d'une tirette 
                elif check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) == True :
                    for i in range(len(playerlist)): #On parcoure la liste des joueurs
                        if playerlist[i]["Color"] == elem[1]: # Et si une couleur est la même que celle de la balle 
                            playerlist[i]["Balle"] -= 1 # Alors le joueur dont la couleur est associé perd une balle
                            # On efface la balle du coup
                            fltk.efface(f"{elem[0]}")
                            # La variable devient l'index du joueur qui l'a fait tombé 
                            elem[1] = playerTurn # D'où la raison pour laquelle au début on voulait que l'élément soit != int
           

def compteurTirette(compteur_tiretteh:list, compteur_tirettev:list, grid_lst:list, boxDimensions:tuple):
    """
    Fonction qui permet de créer les tirettes qu'ont doient tirer pour faire bouger la tirette.
    Elle va récupérer dans chaque dictionnaires, les clés "gauche", "droite", "haut" et "bas",
    puis en fonction de la valeurs elle va crée les compteurs nécessaires.
    
    Paramètres : 
        compteur_tiretteh: Liste de dictionnaire avec le compteur gauche et droite de chaque tirette horizontale (1 de chaque côté par défault)
        compteur_tirettev: Liste de dictionnaire avec le compteur haut et bas de chaque tirette verticale (1 de chaque côté par défault)
        grid_lst: Liste de liste crée avec la fonction board_game
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
    
    Returns :
        Les tirettes sur fltk, où chaque cran est représenté par un petit cercle avec la valeur (1 s'il y a un cran, 2 s'il y a 2 cran)
    """
    # Rayon du petit cercle du cran
    radius = boxDimensions[0]//5
    # On utilise la fonction pour trouver la taille de la police en foncton de la taille du petit cercle 
    font_size = 0
    taille = fltk.taille_texte("2", taille=font_size)
    # Cette fois-ci on s'arrête si on a dépasser la largeur OU la hauteur du petit cercle
    while taille[0] <= (radius*2)*0.8 and taille[1] <= (radius*2)*0.8: # 0.8 pour avoir une marge avec le petit cercle 
        taille = fltk.taille_texte("2", taille=font_size)
        font_size += 1
    # Création des compteurs tirettes en haut et en bas
    for y, line in enumerate(grid_lst): # Pour chaque rangée de case ...
        # Si on dans la première rangée de case alors on est en haut, 
        if y-1 == -1: # Donc si on soustrait -1 on est sur la 1er ligne de case
                sideY, sizeY, radiusY = "haut", boxDimensions[1]/2, radius # Donc on fixe les paramètres pour créer les compteurs de tirettes "haut"
        # Si on dans la dernière rangée de case alors on est en bas, 
        elif y+1 == len(grid_lst): # Donc si on additionne +1 on retrouve le nombre de cases verticales 
                sideY, sizeY, radiusY = "bas", -boxDimensions[1]/2, -radius # Donc on fixe les paramètres pour créer les compteurs de tirettes "bas"
        # Si on se trouve dans 1 des 2 cas, alors on doit créer le compteur des tirettes.
        if y-1 == -1 or y+1 == len(grid_lst):
            # On crée les compteurs de tirettes "haut" et "bah"
            for x, elem in enumerate(line): #Pour chaque case dans la rangée ...                
                if compteur_tirettev[x][sideY] == 0: # Si la clé dans le compteur de la tirette est égale 0, alors on ne peut plus tirer du côté opposé (Ex: Si "haut" = 0 alors "bas" = 2) 
                    # On dessine un demi-cercle pour montrer que le compteur est à 0 
                    fltk.cercle(elem[0][0], elem[0][1] - sizeY,
                                radiusY, "#ECF0F1", "#ECF0F1", tag="tirette")
                # Dans le cas où la clé est > 0, on va tracer les rectangles et les cercles qui représentent le compteur:
                # Pour être au-dessus des cases, on va utiliser le rayon d'une case qu'on va soustraire
                # On commence à 2, car on veut que le premier cran soit au dessus de la case  
                for i in range(2, compteur_tirettev[x][sideY] + 2): # Max = range(4)
                    fltk.cercle(elem[0][0], elem[0][1] - sizeY*i + radiusY, # Quand i = 2 alors il y a 1 cran, si i = 3 alors il y a 2 crans 
                                radiusY, "#ECF0F1", "#ECF0F1", tag="tirette")
                    # On divise par 10 car on veut que sa taille horizontale soit plus petite pour différencier les tirettes verticales dans la grille de jeu 
                    fltk.rectangle(elem[0][0] - boxDimensions[0] / 10, elem[0][1], 
                                   elem[0][0] + boxDimensions[0] / 10, elem[0][1] - sizeY*i + radiusY,
                                   "#ECF0F1", "#ECF0F1", tag="tirette")
                # Pareil pour écrire le texte 
                for i in range(2, compteur_tirettev[x][sideY] + 2):
                    fltk.texte(elem[0][0], elem[0][1] - sizeY*i + radiusY,
                               i - 1, taille=font_size, ancrage="center", tag="tirette")
    # Création des compteurs tirettes à gauche et à droite
    for y, line in enumerate(grid_lst):
        for x, elem in enumerate(line):
            # On est à gauche si on soustrait -1
            if x-1 == -1:
                sideX, sizeX, radiusX = "gauche", boxDimensions[1]/2, radius
            # On est à droite si on additionne +1
            elif x+1 == len(line): 
                sideX, sizeX, radiusX = "droite", -boxDimensions[1]/2, -radius 
            # Si on se trouve dans 1 des 2 cas, alors on doit créer le compteur des tirettes.
            # Comme pour les compteurs en haut et en bas 
            if x-1 == -1 or x+1 == len(line):
                if compteur_tiretteh[y][sideX] == 0:
                    fltk.cercle(elem[0][0] - sizeX, elem[0][1],
                                radiusX, "#D7BDE2", "#D7BDE2", tag="tirette")
                for i in range(2, compteur_tiretteh[y][sideX] + 2):
                    fltk.rectangle(elem[0][0], elem[0][1] - boxDimensions[0] / 10, 
                                   elem[0][0] - sizeX*i + radiusX, elem[0][1] + boxDimensions[1] / 10 ,
                                   "#D7BDE2", "#D7BDE2", tag="tirette")
                    fltk.cercle(elem[0][0] - sizeX*i + radiusX, elem[0][1],
                                radiusX, "#D7BDE2", "#D7BDE2", tag="tirette")
                for i in range(2, compteur_tiretteh[y][sideX] + 2):
                    fltk.texte(elem[0][0] - sizeX*i + radiusX, elem[0][1], 
                               i - 1, taille=font_size, ancrage="center", tag="tirette")

    

def check_hole(tirette_h: list, tirette_v: list, x: int, y: int, compteur_tiretteh:list, compteur_tirettev:list):
    """
    Cette fonction va regarder la liste des tirettes verticales et horizontales
    et en fonction de leurs booléenes, elle va revoyer une réponse  
    On a des tirettes de longueur (NB_cASE + 2) car il y a 2 tirettes cachés. De base on a crée les tirettes dans le jeu
    en commencant par le 2ème élément de chaque tirette (car "gauche" et "haut" sont égales à 2). Donc on a juste besoin de regarder
    la valeur de "haut" et "gauche" pour déduire la valeur de "bas" et "droite 
    
    Paramètres:
        tirette_h : Liste des valeurs boolènes horizontale 
        tirette_v : Liste des valeurs boolènes verticale
        x : La case "x" à l'horizontale
        y : La case "y" à la verticale 
        
    Return: 
        Une réponse
    >>> print(check_hole([[False, False, True, False], [False, True, False, True]], [[False, False, False, True], [False, True, True, False]], 0, 0, [{'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}], [{'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}] ))
    Verticale
    >>> print(check_hole([[False, False, True, False], [False, True, False, True]], [[False, False, True, True], [False, True, True, False]], 0, 0, [{'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}], [{'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}] ))
    True
    """
    if (tirette_v[x][y + compteur_tirettev[x]["haut"]] == True) and (tirette_h[y][x + compteur_tiretteh[y]["gauche"]] == True) :
        return True
    if (tirette_v[x][y + compteur_tirettev[x]["haut"]] == True) and (tirette_h[y][x + compteur_tiretteh[y]["gauche"]] == False) :
        return "Horizontale" 
    if (tirette_v[x][y + compteur_tirettev[x]["haut"]] == False) and (tirette_h[y][x + compteur_tiretteh[y]["gauche"]] == True) :
        return "Verticale"
    if (tirette_v[x][y + compteur_tirettev[x]["haut"]] == False) and (tirette_h[y][x + compteur_tiretteh[y]["gauche"]] == False) :
        return "Hori_et_Verti"
if __name__ == "__main__":
    import doctest
    doctest.testmod()