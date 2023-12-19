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
    [[[(35.0, 35.0)], [(85.0, 35.0)]], [[(35.0, 85.0)], [(85.0, 85.0)]]]
    
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
                            "#aed4fb", remplissage="#6495ED" ,epaisseur=2
                          )
            # On appelle la fonction qui vérifie si y a une tirette ou pas
            # Et en fonction de la réponse il dessine l'image approprié 
            if create_hole(tirette_h, tirette_v, x, y) == "Horizontale" :
                fltk.image(elem[0][0], elem[0][1], "res/tirette_h.png", ancrage="center", 
                           largeur=int(boxDimensions[0]*1.1), # 1.1 comme ça l'image dépasse la case et s'assemble avec les autres cases
                           hauteur=int(boxDimensions[1] * 0.5)) # Pour éviter de faire toutes la case
            elif create_hole(tirette_h, tirette_v, x, y) == "Verticale" :
                fltk.image(elem[0][0], elem[0][1], "res/tirette_v.png", ancrage="center", 
                           largeur=int(boxDimensions[0] * 0.5), 
                           hauteur=int(boxDimensions[1]*1.1))
            elif create_hole(tirette_h, tirette_v, x, y) == "Hori_et_Verti" :
                fltk.image(elem[0][0], elem[0][1], "res/tirette_h.png", ancrage="center", 
                           largeur=int(boxDimensions[0]*1.1), 
                           hauteur=int(boxDimensions[1] * 0.5))
                fltk.image(elem[0][0], elem[0][1], "res/tirette_v.png", ancrage="center", 
                           largeur=int(boxDimensions[0] * 0.5 ), 
                           hauteur=int(boxDimensions[1]*1.1))
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
        
