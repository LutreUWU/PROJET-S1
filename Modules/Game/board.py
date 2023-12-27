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

def create_board(grid:list, boxDimensions:tuple, margin:tuple, tirette_h:list, tirette_v:list):
    """
    Cette fonction va prendre la liste des cases et créer les cases en fonction des paramètres qui lui sont
    associés (s'il y a une tirette ou non, s'il y a une balle ou non ...) 
    
    Paramètres:
        grid: La liste crée avec la fonction précedente
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
        margin: Un tuple avec les marge (x,y) entre les cases
        tirette_h: La liste de True et de False pour les tirettes horizontales
        tirette_v: La liste de True et de False pour les tirettes verticales
    
    Return: 
        La grille de jeu sur fltk
    """
    for y, line in enumerate(grid): # Pour chaque rangée de case ... 
        for x, elem in enumerate(line): #Pour chaque case dans la rangée ...
            # On trace la contour de la case
            fltk.rectangle((elem[0][0] - boxDimensions[0]/2 + margin[0]),( elem[0][1] - boxDimensions[1]/2 + margin[1]), 
                           (elem[0][0] + boxDimensions[0]/2 - margin[0]),( elem[0][1] + boxDimensions[1]/2 - margin[1]),
                            "#aed4fb", remplissage="#6495ED" ,epaisseur=3
                          )
            # On appelle la fonction qui vérifie si y a une tirette ou pas
            # Et en fonction de la réponse il dessine l'image approprié 
            if create_hole(tirette_h, tirette_v, x, y) == "Horizontale" :
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 2 + margin[0] + 2, elem[0][1] - boxDimensions[1] /  5 + margin[1], 
                               elem[0][0] + boxDimensions[0] / 2 - margin[0] - 2, elem[0][1] + boxDimensions[1] / 5 - margin[1],
                               tag ="plateau", couleur="#D7BDE2", remplissage="#D7BDE2")
            elif create_hole(tirette_h, tirette_v, x, y) == "Verticale" :
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 5 + margin[0], elem[0][1] - boxDimensions[1] / 2 + margin[1] + 2, 
                               elem[0][0] + boxDimensions[0] / 5 - margin[0], elem[0][1] + boxDimensions[1] / 2 - margin[1] - 2,
                               tag ="plateau", couleur="#ECF0F1", remplissage="#ECF0F1")
            elif create_hole(tirette_h, tirette_v, x, y) == "Hori_et_Verti" :
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 2 + margin[0] + 2, elem[0][1] - boxDimensions[1] /  5 + margin[1], 
                               elem[0][0] + boxDimensions[0] / 2 - margin[0] - 2, elem[0][1] + boxDimensions[1] / 5 - margin[1],
                               tag ="plateau", couleur="#D7BDE2", remplissage="#D7BDE2")
                fltk.rectangle(elem[0][0] - boxDimensions[0] / 5 + margin[0], elem[0][1] - boxDimensions[1] / 2 + margin[1] + 2, 
                               elem[0][0] + boxDimensions[0] / 5 - margin[0], elem[0][1] + boxDimensions[1] / 2 - margin[1] - 2,
                               tag ="plateau", couleur="#ECF0F1", remplissage="#ECF0F1")

def create_hole(tirette_h: list, tirette_v: list, x: int, y: int):
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
    if (tirette_v[x][y] == True) and (tirette_h[y][x] == True) :
        return True
    if (tirette_v[x][y] == True) and (tirette_h[y][x] == False) :
        return "Horizontale" 
    if (tirette_v[x][y] == False) and (tirette_h[y][x] == True) :
        return "Verticale"
    if (tirette_v[x][y] == False) and (tirette_h[y][x] == False) :
        return "Hori_et_Verti"

def detect_click_case(abs, ord, margin:tuple, boxDimensions:tuple, coordinateNW:tuple):
    """
    Fonction qui va permettre de détecter si on clique sur une case ou non, si c'est le cas,
    elle va renvoyer l'indice de la case.
    
    Le problème majeur était de vérifier qu'on ne clique pas entre les cases.
    La solution est de vérifier 1 par 1 chaque case en les parcourants chacune   
    
    Paramètres:
        abs: Coordonnée X de la souris
        ord: Coordonnée Y de la souris
        margin: Un tuple avec les marge (x,y) entre les cases
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
        coordinateNW : Coordonnées (x,y) de la fenêtre qu'on a crée (pour faire la marge avec la fenêtre windows) 
    Returns:
        Les indices X et Y, de la cases 
    
    >>> detect_click_case(20, 20,(5, 5), (50, 50), (10, 10))
    (0, 0)
    """
    # On cherche comme si il n'y avait pas de marge entre les cases 
    # On va soustraite l'abscisse par le point d'origine, puis son va diviser par la taille d'une case, pour connaître c'est quelle cases qu'on clique
    nb_case_x = int((abs - coordinateNW[0]) // boxDimensions[0])
    nb_case_y = int((ord - coordinateNW[1]) // boxDimensions[1])
    # Variable pour vérifier si on a cliqué entre les cases ou pas 
    positionX, positionY = coordinateNW[0], coordinateNW[1] # Origine des points
    checkX, checkY = False, False # Si les 2 sont True alors on n'a pas cliqué entre les cases
    # On commmence tout d'abord avec l'abscisse  
    for i in range(nb_case_x + 1 ): # +1 car si on commence à 0, comme la 1er case a pour indice 0, le for ne va pas s'activer.
        # A la première case on ajoute la marge 1 fois
        if i == 0: 
            left_positionX = positionX + margin[0]
        # Puis pour le reste on ajoute 2 fois la marge 
        else: 
            left_positionX = positionX + margin[0]*2
        # Puis on avance la position originale de la taille de la case
        positionX = left_positionX + (boxDimensions[0] - 2*margin[0])
        if left_positionX <= abs <= positionX: # Puis on vérifier si l'abs est entre les 2 points 
             checkX = True # Si c'est le cas alors on est sur une case X
             # A effacer en dessous, c'est pour mieux visualiser     
             """print("a l'intérieur X")
             fltk.cercle(left_positionX, ord,
                         3, couleur="black")
             fltk.cercle(positionX, ord,
                         3, couleur="black")"""
    # Pareil pour l'ordonnée
    for i in range(nb_case_y + 1 ):
        if i == 0:
            left_positionY = positionY + margin[1]
        else:
            left_positionY = positionY + margin[1]*2
        positionY = left_positionY + (boxDimensions[1] - 2*margin[1])
        if left_positionY <= ord <= positionY: 
             checkY = True # Si c'est le cas alors on est sur une case Y
             # A effacer en dessous, c'est pour mieux visualiser          
             """print("a l'intérieur Y")
             fltk.cercle(abs, left_positionY,
                         3, couleur="blue")
             fltk.cercle(abs, positionY,
                         3, couleur="blue")"""
    if checkX and checkY:
        return nb_case_x, nb_case_y
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()