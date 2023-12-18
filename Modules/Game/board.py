if __name__ == "__main__":
    import fltk as fltk
else:
    import Modules.fltk as fltk

def board_game(tile_hori, tile_verti, boxSize, coordinateNW):
    """
    Cette fonction qui va créer la liste nécessaire pour créer
    la grille de jeu
    
    Paramètres:
        tile_hori / tile_verti : Nombre de case horizontale et verticale
        boxSite : Taille d'une case
        coordinateNW : Coordonnées North West de la grille  
    
    Return:
        Une liste de liste de coordonnée
    
    >>> board_game(2, 2, (50, 50), (10, 10))
    [[[(35.0, 35.0)], [(85.0, 35.0)]], [[(35.0, 85.0)], [(85.0, 85.0)]]]    
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



def afficher_trou(tirette_h, tirette_v, quadrillage, longeur, margin):
    """
    une fonction qui en entrée la tirette et affiche les trous qui sont dans la tirette
    parametres:
        tirette : list de list
        quadrillage : list de list
        longeur : int
        couleur : str
    
    return :
        il affiche les trous grace à fltk
    """
    for i in range(len(tirette_h)): # parcourir la matrice
        for j in range(len(tirette_h[i])):
            if tirette_h[i][j] == False:
                couleur = 'blue'
                fltk.rectangle(quadrillage[i][j][0][0] - longeur[0] // 2 + margin[0], 
                            quadrillage[i][j][0][1] - longeur[1] // 4 + margin[1], 
                            quadrillage[i][j][0][0] + longeur[0] // 2 - margin[0], 
                            quadrillage[i][j][0][1] + longeur[1] // 4 - margin[1],
                            couleur,
                            remplissage=couleur)
                
            if tirette_v[i][j] == False:
                couleur = 'orange'
                fltk.rectangle(quadrillage[i][j][0][0] - longeur[0] // 4 + margin[0], 
                            quadrillage[i][j][0][1] - longeur[1] // 2 + margin[1], 
                            quadrillage[i][j][0][0] + longeur[0] // 4 - margin[0], 
                            quadrillage[i][j][0][1] + longeur[1] // 2 - margin[1],
                            couleur,
                            remplissage=couleur)
                
            fltk.rectangle(quadrillage[i][j][0][0] - longeur[0] // 2 + margin[0], 
                            quadrillage[i][j][0][1] - longeur[1] // 2 + margin[1], 
                            quadrillage[i][j][0][0] + longeur[0] // 2 - margin[0], 
                            quadrillage[i][j][0][1] + longeur[1] // 2 - margin[1],
                            couleur='black')

def create_board(grid, boxDimensions, margin, tirette_h, tirette_v):
    """
    This function will take the grid list and will create the center of each case
    on fltk.
    And with the center, the function will create the type of "tirette", and the square around the circle, 
    
    Arg: The grid list
    
    Return: Squares on fltk 
    """
    for y, line in enumerate(grid):
        for x, elem in enumerate(line): 
            fltk.rectangle((elem[0][0] - boxDimensions[0]/2 + margin[0]),( elem[0][1] - boxDimensions[1]/2 + margin[1]), 
                           (elem[0][0] + boxDimensions[0]/2 - margin[0]),( elem[0][1] + boxDimensions[1]/2 - margin[1]),
                            "#aed4fb", remplissage="#6495ED" ,epaisseur=2
                          )
            if create_hole(tirette_h, tirette_v, x, y) == "Horizontale" :
                fltk.image(elem[0][0], elem[0][1], "res/tirette_h.png", ancrage="center", 
                           largeur=int(boxDimensions[0]*1.1), # 1.1 comme ça l'image dépasse la case et s'assemble avec les autres 
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
def create_hole(tirette_h, tirette_v, x, y):
    """
    This function will check each "tirette" to know if there's a hole,
    and depending of the answer, he will return something
    
    Arg: tiretteX / tiretteY list, and index of the tirette
    
    Return: Type of box 
    """
    if (tirette_v[x][y] == True) and (tirette_h[y][x] == True) :
        return True
    if (tirette_v[x][y] == True) and (tirette_h[y][x] == False) :
        return "Horizontale" 
    if (tirette_v[x][y] == False) and (tirette_h[y][x] == True) :
        return "Verticale"
    if (tirette_v[x][y] == False) and (tirette_h[y][x] == False) :
        return "Hori_et_Verti"
        
