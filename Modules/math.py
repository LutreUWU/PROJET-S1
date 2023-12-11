from random import choice

def size_box(LARGEUR_windows, HAUTEUR_windows, nbBox):
    """
    This function will automatically calculate the size of
    the box depending of the windows size.
    It will also give the margin between box.
    
    Args: width / height of the windows / number of box
    
    Return: box size, margin, new center box-size
    
    >>> size_box(1000, 1000, 7)
    ((114.28571428571429, 114.28571428571429), (5.0, 5.0), (100.0, 100.0)) 
    """
    margin_center, largeur, hauteur = center_box(LARGEUR_windows, HAUTEUR_windows)    
    center_width = largeur * 0.9
    center_height = hauteur * 0.9
    margin = (largeur * 0.005, hauteur * 0.005)
    coordinateNW, coordinateSE = (largeur - center_width, hauteur - center_height), (center_width, center_height)   
    new_dimension = (coordinateSE[0] - coordinateNW[0], coordinateSE[1] - coordinateNW[1])
    box_size = ((new_dimension[0]) / nbBox), ((new_dimension[1]) / nbBox)
    coordinateNW = (coordinateNW[0] + margin_center[0], coordinateNW[1] + margin_center[1])
    return box_size, margin, coordinateNW

def center_box(LARGEUR, HAUTEUR):
    """
    This function is usefull when the width and height of
    the windows is different.
    It will add the marge necessary to center the box 
    
    Args: LARGEUR, HAUTEUR
    
    Return: Margin, and LARGEUR, HAUTEUR
    
    >>> center_box(800, 1000)
    ((0, 100.0), 800, 800)
    """
    margin_width, margin_height = 0, 0
    if LARGEUR > HAUTEUR:
        margin_width = (LARGEUR - HAUTEUR)/2
        LARGEUR = HAUTEUR
    elif HAUTEUR > LARGEUR:
        margin_height = (HAUTEUR - LARGEUR)/2 
        HAUTEUR = LARGEUR
    return (margin_width, margin_height), LARGEUR, HAUTEUR
    
def create_tirette(nbBox):
    """
    This function will automatically create all the tirette
    for the game, by randomly choosing between True and False
    
    Args: number of box
    
    Return: lists of True and False 
    """
    tirette_h = [[choice([True, False]) for _ in range(nbBox) ] for _ in range(nbBox)]
    tirette_v = [[choice([True, False]) for _ in range(nbBox) ] for _ in range(nbBox)]
    return tirette_h,tirette_v

