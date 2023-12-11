def board_game(tile_hori, tile_verti, boxSize, coordinateNW):
    """
    This fonction will take the dimension of the board and
    will add all the parameters necessary for creating
    the box
    
    Args: The dimensions(tile_hori, tile_verti)
    
    Return:The coordinates of each square center as a module 
    
    Exemple with a 3x2 grid and a margin of 5  
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
                rectangle(quadrillage[i][j][0][0] - longeur[0] // 2 + margin[0], 
                            quadrillage[i][j][0][1] - longeur[1] // 4 + margin[1], 
                            quadrillage[i][j][0][0] + longeur[0] // 2 - margin[0], 
                            quadrillage[i][j][0][1] + longeur[1] // 4 - margin[1],
                            couleur,
                            remplissage=couleur)
                
            if tirette_v[i][j] == False:
                couleur = 'orange'
                rectangle(quadrillage[i][j][0][0] - longeur[0] // 4 + margin[0], 
                            quadrillage[i][j][0][1] - longeur[1] // 2 + margin[1], 
                            quadrillage[i][j][0][0] + longeur[0] // 4 - margin[0], 
                            quadrillage[i][j][0][1] + longeur[1] // 2 - margin[1],
                            couleur,
                            remplissage=couleur)
                
            rectangle(quadrillage[i][j][0][0] - longeur[0] // 2 + margin[0], 
                            quadrillage[i][j][0][1] - longeur[1] // 2 + margin[1], 
                            quadrillage[i][j][0][0] + longeur[0] // 2 - margin[0], 
                            quadrillage[i][j][0][1] + longeur[1] // 2 - margin[1],
                            couleur='black')
