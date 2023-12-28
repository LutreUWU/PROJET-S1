from random import choice

def size_box(LARGEUR_windows: int, HAUTEUR_windows: int, nbBox:int):
    """
    La fonction calcule la taille d'une case de jeu en fonction
    des dimensions de la fenêtre et du nombre de cases
    
    Paramètres:
        LARGEUR_windows: Largeur de la fenêtre (en px)
        HAUTEUR_windows: Hauteur de la fenêtre (en px)
        nbBox: Nombre de cases
    
    Return: 
        box-size: Taille d'une case
        margin: Marge entre chaque cases
        coordinateNW: Marge pour la fenêtre
    
    >>> size_box(1000, 1000, 7)
    ((100.0, 100.0), (5.0, 5.0), (150.0, 150.0))
    >>> size_box(0, 0, 1000)
    ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0))
    >>> size_box(1000, 1000, 0)
    ((0, 0), (0, 0), (0, 0))
    """
    if nbBox == 0: # Pour éviter un message d'erreur si on met 0 case 
        return ((0,0), (0,0), (0,0))
    # Dans le cas où Largeur /= Hauteur, on appelle la fonction pour centrer le jeu et éviter l'étirement
    margin_center, largeur, hauteur = center_box(LARGEUR_windows, HAUTEUR_windows)    
    # On crée une fenêtre plus petite pour avoir la marge avec la fenêtre
    center_width = largeur * 0.85
    center_height = hauteur * 0.85
    # La marge est égal à 0.05% de la largeur/hauteur 
    margin = (largeur * 0.005, hauteur * 0.005)
    # On calcule les nouvelles dimensions, puis on le divise par le nombre de cases pour avoir la taille d'une case
    coordinateNW, coordinateSE = (largeur - center_width, hauteur - center_height), (center_width, center_height)   
    new_dimension = (coordinateSE[0] - coordinateNW[0], coordinateSE[1] - coordinateNW[1])
    box_size = ((new_dimension[0]) / nbBox), ((new_dimension[1]) / nbBox)
    # On ajoute une petite marge entre la nouvelle fenêtre et les cases
    coordinateNW = (coordinateNW[0] + margin_center[0], coordinateNW[1] + margin_center[1])
    return box_size, margin, coordinateNW


def center_box(LARGEUR_windows: int, HAUTEUR_windows: int):
    """
    Cette fonction permet de centrer le jeu de grille quand
    la largeur et la hauteur de la fenêtre est différente 
    
    Paramètres:
        LARGEUR_windows: Largeur de la fenêtre (en px)
        HAUTEUR_windows: Hauteur de la fenêtre (en px)
    
    Return: 
        Tuple avec la marge (x,y)
        Largeur d'un bouton 
        Hauteur d'un bouton 
    
    >>> center_box(800, 1000)
    ((0, 100.0), 800, 800)
    
    >>> center_box(0, 0)
    ((0, 0), 0, 0)
    
    >>> center_box(1000, 1000)
    ((0, 0), 1000, 1000)
    """
    # Marge qu'on doit ajouter pour centrer
    margin_width, margin_height = 0, 0
    if LARGEUR_windows > HAUTEUR_windows: # Largeur > Hauteur
        # On calcule la marge à ajouté pour centrer correctement
        margin_width = (LARGEUR_windows - HAUTEUR_windows)/2
        # On crée le jeu comme si c'était les mêmes dimensions
        LARGEUR_windows = HAUTEUR_windows
    elif HAUTEUR_windows > LARGEUR_windows: # Hauteur > Largeur
        margin_height = (HAUTEUR_windows - LARGEUR_windows)/2 
        HAUTEUR_windows = LARGEUR_windows
    return (margin_width, margin_height), LARGEUR_windows, HAUTEUR_windows
def create_tirette(nbBox:int):
    """
    This function will automatically create all the tirette
    for the game, by randomly choosing between True and False
    
    Args: number of box
    
    Return: lists of True and False 
    """
    tirette_h = [[choice([True, False]) for _ in range(nbBox) ] for _ in range(nbBox)]
    tirette_v = [[choice([True, False]) for _ in range(nbBox) ] for _ in range(nbBox)]
    return tirette_h,tirette_v


def coordinate_center(LARGEUR_windows:int, HAUTEUR_windows:int):
    """
    Pour le menu on veut que les 3 boutons soient au centre en bas de la fenêtre.
    
    Cette fonction va permettre calculer la taille et 
    les coordonnées des boutons en fonction de la fenêtre.
    Paramètres:
        LARGEUR_windows: Largeur de la fenêtre (en px)
        HAUTEUR_windows: Hauteur de la fenêtre (en px)
        
    Return: 
        Largeur d'un bouton 
        Hauteur d'un bouton 
        Liste de tuple qui contient les coordonnée (x,y) de chaque boutons
    
    >>> coordinate_center(800, 800)
    (400.0, 93.33333333333333, [(400.0, 509.3333333333333), (400.0, 618.6666666666666), (400.0, 728.0)])
    >>> coordinate_center(0, 0)
    (0.0, 0.0, [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0)])
    """
    # La largeur du bouton est égale à 50% de la fenêtre
    button_width = LARGEUR_windows * 0.5
    # Les 3 boutons vont occuper 35% de la fenêtre, comme il y en a 3 on divise par 3
    button_height = (HAUTEUR_windows * 0.35) / 3
    # Marge pour séparer les boutons 
    margin_button = HAUTEUR_windows * 0.02
    
    coordinate_button = []
    for i in range(1,4): # Car y a 3 boutons 
        x = button_width
        # On multiplie par 0.5 pour que ça démarre directement à la moitié de la fenêtre
        y = HAUTEUR_windows * 0.5 + (button_height + margin_button) * i
        coordinate_button.append((x, y))
    return button_width, button_height, coordinate_button

def coordinate_center_title(LARGEUR_windows:int, HAUTEUR_windows:int):
    """
    Pour le menu on veut que le titre soient au centre en haut de la fenêtre.

    Cette fonction va permettre calculer la taille et 
    les coordonnées du Titre de jeu en fonction de la fenêtre
    
    Paramètres:
        LARGEUR_windows: Largeur de la fenêtre (en px)
        HAUTEUR_windows: Hauteur de la fenêtre (en px)
        
    Return: 
        Tuple avec les coordonnées (x,y) du titre
        Largeur du titre 
        Hauteur du titre
    >>> coordinate_center_title(1000, 1000)  
    ((500.0, 250.0), 300.0, 150.0)
    
    >>> coordinate_center_title(0, 0)  
    ((0.0, 0.0), 0.0, 0.0)
    """
    # On veut le centre soient à 25% de la hauteur (i.e en haut au centre de la fenêtre)
    # On divise la hauteur par 4 en 2 fois pour calculer la hauteur du titre
    half_height = HAUTEUR_windows/2 
    center_half_windows = (LARGEUR_windows/2, half_height/2)
    
    title_width_radius = (LARGEUR_windows * 0.6)/2
    title_height_radius = (half_height * 0.6)/2
    return center_half_windows, title_width_radius, title_height_radius
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()