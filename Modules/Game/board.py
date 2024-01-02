if __name__ != "__main__":
    import Modules.fltk as fltk

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
        Une liste où chaque élément represente une ligne de jeu.
        Pour chaque élément on a une liste d'éléments qui représente les cases
        et chaque case à une liste avec ses paramètres suivants :
        - Tuple de coordonnée (x,y)
        - Indicateur pour savoir s'il y a une balle ou non ("0" ou "1")
    
    >>> board_game(2, 2, (50, 50), (10, 10))
    [[[(35.0, 35.0), '0'], [(85.0, 35.0), '0']], [[(35.0, 85.0), '0'], [(85.0, 85.0), '0']]]
    >>> board_game(0, 0, (0,0), (0, 0))
    []
    
    >>> board_game(0, 0, (50, 50), (10, 10))
    []
    """
    x = coordinateNW[0] + boxSize[0]/2
    y = coordinateNW[1] + boxSize[1]/2 
    board_lst = []
    for i in range(tile_verti):
        board_line = []
        x = coordinateNW[0] + boxSize[0]/2
        for p in range(tile_hori):
             board_line.append([(x, y), "0"])
             x += boxSize[0]     
        board_lst.append(board_line)
        y += boxSize[1]
    return board_lst

playerball = {}
def create_board(grid:list, boxDimensions:tuple, margin:tuple, tirette_h:list, tirette_v:list, ball_case, playercolor:str,
                 compteur_tiretteh, compteur_tirettev, playerlist:dict, playerTurn):
    """
    Cette fonction va prendre la liste des cases et créer les cases en fonction des paramètres qui lui sont
    associés (s'il y a une tirette ou non, s'il y a une balle ou non ...) 
    
    Pour l'instant y a pas la balle 
    
    Paramètres:
        grid: La liste crée avec la fonction précedente
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
        margin: Un tuple avec les marge (x,y) entre les cases
        tirette_h: La liste de True et de False pour les tirettes horizontales
        tirette_v: La liste de True et de False pour les tirettes verticales
        ball_case: L'indice x, y de la case qu'on a cliqué pour placer la balle
    Return: 
        La grille de jeu sur fltk
    """
    for y, line in enumerate(grid): # Pour chaque rangée de case ...
        for x, elem in enumerate(line): #Pour chaque case dans la rangée ...
            # On trace la contour de la case
            fltk.rectangle((elem[0][0] - boxDimensions[0]/2 + margin[0]),( elem[0][1] - boxDimensions[1]/2 + margin[1]), 
                           (elem[0][0] + boxDimensions[0]/2 - margin[0]),( elem[0][1] + boxDimensions[1]/2 - margin[1]),
                            "#aed4fb", remplissage="#6495ED" ,epaisseur=3, tag="board"
                          )
            # On appelle la fonction qui vérifie si y a une tirette ou pas
            # Et en fonction de la réponse il dessine l'image approprié 
            if check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) == "Horizontale" :
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 2 + 2, elem[0][1] - boxDimensions[1] / 5 + margin[1], 
                               elem[0][0] + boxDimensions[0] / 2 - 2, elem[0][1] + boxDimensions[1] / 5 - margin[1],
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

            if type(ball_case) != bool and (x == ball_case[0] and y == ball_case[1]): 
                if check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) != True : # Vérifie qu'on clique pas sur un trou
                    if elem[1] == "0": # Vérifier qu'il n'y a pas déja une balle
                        elem[1] = playercolor
            if elem[1] != "0" and type(elem[1]) != int: 
                if check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) != True: # Si on a un trou lorsqu'on déplacé une tirette
                    fltk.cercle(elem[0][0], elem[0][1], margin[0]*2 - boxDimensions[0] / 2.5, 
                                epaisseur=5, couleur=elem[1], remplissage=elem[1], tag=f"{elem[0]}")
                elif check_hole(tirette_h, tirette_v, x, y, compteur_tiretteh, compteur_tirettev) == True :
                    for i in range(len(playerlist)):
                        if playerlist[i]["Color"] == elem[1]:
                            playerlist[i]["Balle"] -= 1
                            fltk.efface(f"{elem[0]}")
                            elem[1] = playerTurn 
           

def compteurTirette(compteur_tiretteh:list, compteur_tirettev:list, grid_lst:list, boxDimensions:tuple):
    """
    Fonction qui permet de créer les tirettes qu'ont doient tirer pour faire bouger la tirette.
    La tirette s'adapte à la fenêtre, hormis pour le texte.
    
    Paramètres : 
        compteur_tiretteh: Liste de dictionnaire avec le compteur gauche et droite de chaque tirette horizontale (1 de chaque côté par défault)
        compteur_tirettev: Liste de dictionnaire avec le compteur haut et bas de chaque tirette verticale (1 de chaque côté par défault)
        grid_lst: Liste de liste crée avec la fonction board_game
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
    
    Returns :
        Les tirettes sur fltk
    """
    radius = boxDimensions[0]//5
    for y, line in enumerate(grid_lst): # Pour chaque rangée de case ...
        if y-1 == -1: # Si on est en haut de la grille, 
                sideY, sizeY, radiusY = "haut", boxDimensions[1]/2, radius
        elif y+1 == len(grid_lst): # Ou en bas 
                sideY, sizeY, radiusY = "bas", -boxDimensions[1]/2, -radius
        if y-1 == -1 or y+1 == len(grid_lst):
            for x, elem in enumerate(line): #Pour chaque case dans la rangée ...                
                if compteur_tirettev[x][sideY] == 0:
                    fltk.cercle(elem[0][0], elem[0][1] - sizeY,
                                radiusY, "#ECF0F1", "#ECF0F1", tag="tirette")
                for i in range(2, compteur_tirettev[x][sideY] + 2):
                    fltk.cercle(elem[0][0], elem[0][1] - sizeY*i + radiusY,
                                radiusY, "#ECF0F1", "#ECF0F1", tag="tirette")
                    fltk.rectangle(elem[0][0] - boxDimensions[0] / 10, elem[0][1], 
                                   elem[0][0] + boxDimensions[0] / 10, elem[0][1] - sizeY*i + radiusY,
                                   "#ECF0F1", "#ECF0F1", tag="tirette")
                for i in range(2, compteur_tirettev[x][sideY] + 2):
                    fltk.texte(elem[0][0], elem[0][1] - sizeY*i + radiusY,
                               i - 1, ancrage="center", tag="tirette")
    
    for y, line in enumerate(grid_lst):
        for x, elem in enumerate(line):
            if x-1 == -1:
                sideX, sizeX, radiusX = "gauche", boxDimensions[1]/2, radius
            elif x+1 == len(line):
                sideX, sizeX, radiusX = "droite", -boxDimensions[1]/2, -radius 
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
                               i - 1, ancrage="center", tag="tirette")

    

def check_hole(tirette_h: list, tirette_v: list, x: int, y: int, compteur_tiretteh, compteur_tirettev):
    """
    Cette fonction va regarder la liste des tirettes verticales et horizontales
    et en fonction de leurs booléenes, elle va revoyer une réponse  
    
    Par exemple si x et y vaut 0, alors on cible la toute première case du jeu (Celle en haut à gauche)
    
    Paramètres:
        tirette_h : Liste des valeurs boolènes horizontale 
        tirette_v : Liste des valeurs boolènes verticale
        x : La case "x" à l'horizontale
        y : La case "y" à la verticale 
        
    Return: 
        Une réponse 
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