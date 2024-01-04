"""ATTETION IL Y A UN DOCTEST QUI NE MARCHE PAS JE SAIS PAS POURQUOI (La fonction coordinate_changeButton_settings)"""
"""DONC ENLEVER LE DOCTEST DANS CETTE FONCTION POUR TESTER LES AUTRES FONCTIONS"""

def coordinate_center_title(LARGEUR_windows:int, HAUTEUR_windows:int):
    """
    Pour le menu on veut que le titre soient au centre en haut de la fenêtre.

    Cette fonction va permettre de calculer la taille et 
    les coordonnées du Titre de jeu en fonction de la fenêtre
    
    Paramètres:
        LARGEUR_windows: Largeur de la fenêtre (en px)
        HAUTEUR_windows: Hauteur de la fenêtre (en px)
        
    Return: 
        Tuple avec les coordonnées (x,y) du titre
        Largeur du titre 
        Hauteur du titre
    >>> coordinate_center_title(1000, 1000)  
    ((500.0, 250.0), 600.0, 300.0)
    
    >>> coordinate_center_title(0, 0)  
    ((0.0, 0.0), 0.0, 0.0)
    """
    # On veut le centre soient à environ 25% de la hauteur (i.e en haut, au centre de la fenêtre)
    # On divise la hauteur par 4 en 2 fois, car on en aura besoin pour calculer la hauteur du titre
    half_height = HAUTEUR_windows/2 
    center_half_windows = (LARGEUR_windows/2, half_height/2) # Le centre du rectangle est la moitié de la largeur(= 50%) et le quart de la hauteur (= 25%) 
    title_width = (LARGEUR_windows * 0.6) # La largeur sera égale à 60% de la largeur de la fenêtre
    title_height = (half_height * 0.6) # La hauteur sera égale à 60% de la moitié de la hauteur de la fenêtre 
    return center_half_windows, title_width, title_height

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
    # Marge de 2% de la hauteur, pour séparer les boutons 
    margin_button = HAUTEUR_windows * 0.02 
    
    coordinate_button = []
    for i in range(1,4): # Car y a 3 boutons 
        x = button_width
        # On veut que les boutons soient en bas de la fenêtre
        # Donc on multiplie par 0.5 pour que ça démarre directement à la moitié de la fenêtre
        y = HAUTEUR_windows * 0.5 + (button_height + margin_button) * i # Le i va nous permettre de séparer les 3 boutons 
        coordinate_button.append((x, y))
    return button_width, button_height, coordinate_button

def coordinate_center_settings(LARGEUR_windows:int, HAUTEUR_windows:int):
    """
        Pour les paramètres on veut que les 3 boutons soient au centre de le fenêtre
        Cette fonction va permettre de calculer la taille et les coordonnées des boutons
        en fonction de la fenêtre.
        Il y a aussi un 4ème bouton qui sera tout en bas de la fenêtre, qui permet de sauvegarder les paramètres
        et de retourner à l'acceuil.
        Paramètres:
            LARGEUR_windows: Largeur de la fenêtre (en px)
            HAUTEUR_windows: Hauteur de la fenêtre (en px)
        Return: 
            Liste de tuple avec les coordonnées (x,y) de chaque boutons
            tuple avec la largeur et la hauteur de chaque boutons 
            
        >>> coordinate_center_settings(800, 800)
        ([(400.0, 240.0), (400.0, 400.0), (400.0, 560.0), (400.0, 740.0)], (400.0, 120.0))
        """
    button_settings_height = HAUTEUR_windows * 0.15 # La hauteur du bouton est égale à 15% de la hauteur de la fenêtre
    button_settings_width = LARGEUR_windows * 0.5 # La largeur du bouton est égale à 50% de la largeur de la fenêtre
    center_windows = (LARGEUR_windows/2, HAUTEUR_windows/2) # Les coordonnées (x,y) du centre sont égales à la moitié de la largeur et de la hauteur de la fenêtre
    margin_button = HAUTEUR_windows * 0.05 # Marge pour séparer les boutons 
    # On veut centrer les 3 boutons sur la fenêtre, donc le 2ème boutons sera le centre de la fenêtre 
    First_button = (center_windows[0], center_windows[1] - button_settings_height - margin_button) # Donc le premier bouton aura pour coordonnée (y) celle du centre moins la hauteur d'un bouton et sa marge 
    Second_button = center_windows # Comme dit au-dessus, c'est égale aux centre de la fenêtre
    Third_button = (center_windows[0], center_windows[1] + button_settings_height + margin_button) # Et le troisième bouton aura pour coordonnée (y) celle du centre plus la hauteur d'un bouton et sa marge 
    Save_button = (center_windows[0], HAUTEUR_windows - button_settings_height/2) # On ne veut pas centrer le dernier bouton, il sera tout en bas de la fenêtre, on divise par 2 car on veut le centre
    return [First_button, Second_button, Third_button, Save_button], (button_settings_width, button_settings_height)

if __name__ != "__main__":
    import Modules.fltk as fltk
else:
    import fltk as fltk

def coordinate_changeButton_settings(coord_settingButton:list, size_settingButton:tuple):
    """
        Pour chacun des paramètres (Sauf le dernier bouton "Save") on veut pouvoir ajouter ou soustraire 1 pour modifier les paramètres.
        Le bouton "-" est à gauche, le bouton "+" est à droite
        Grâce aux coordonnées obtenu avec la fonction précédente on va obtenir la taille et les coordonnées (x,y) de chaque boutons "+" et "-"
        en fonction de la fenêtre.
        Paramètres:
            coord_settingButton: Liste de tuple avec les coordonnées de chaque boutons
            size_settingButton: Tuple avec la Largeur et Hauteur de chaque bouton
        Return: 
            Liste de tuple avec les coordonnées de chaque boutons "-"
            Liste de tuple avec les coordonnées de chaque boutons "+"
            Tuple avec la largeur et la hauteur des boutons "-" et "+"
            
        Le doctest ne marche pas car il y a une erreur que je ne comprends pas,
        >>> coordinate_changeButton_settings([(400.0, 240.0), (400.0, 400.0), (400.0, 560.0), (400.0, 740.0)], (400.0, 120.0))
        """
        
    less_ButtonCoord, more_ButtonCoord = [], []
    for i in range(3): # Car on veut ajouter les "+" et "-" seulement pour les 3 premiers boutons
         # Pour aller à gauche, on va soustraire la taille du SettingButton (= size_settingButton[0]/2) et 1/4 de la taille du SettingButton(= size_settingButton[0]/4)) pour que le bouton ne soit pas coller avec le SettingButton 
         less_ButtonCoord.append((coord_settingButton[i][0] - (size_settingButton[0]/2 + size_settingButton[0]/4), coord_settingButton[i][1]))
         # Pareil mais on additionne car on veut aller à droite
         more_ButtonCoord.append((coord_settingButton[i][0] + (size_settingButton[0]/2 + size_settingButton[0]/4), coord_settingButton[i][1])) 
    
    # Cette fonction-là, on la verra beaucoup, elle va nous permettre de calculer la taille de la police afin qu'elle soit toujours dans le rectangle
    # Le but est de commencer avec une police petite, et grâce à fltk.taille_texte, on va vérifier à chaque fois si le texte est dans le bouton, si c'est le cas alors on ajoute +1 à la police jusqu'à qu'elle dépasse le bouton
    font_size = 1
    taille = fltk.taille_texte(" + ", taille=font_size) # On se base sur le "+" comme ça les 2 boutons ont la même taille
    while taille[1] <= size_settingButton[1]: # Tant que la taille du texte est à l'intérieur du bouton
        taille = fltk.taille_texte("+", taille=font_size)
        font_size += 1 # On augmente la police de +1 
    ButtonChange_size = (taille[1], taille[1]) # Pour avoir un carré on met 2 fois la même taille
    return less_ButtonCoord, more_ButtonCoord, ButtonChange_size

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
    ((85.71428571428571, 85.71428571428571), (5.0, 5.0), (200.0, 200.0))
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
    center_width = largeur * 0.80 # 80% de la Largeur
    center_height = hauteur * 0.80 # 80% de la Hauteur
    # La marge (x,y) est égale à 0.05% de la largeur/hauteur 
    margin = (largeur * 0.005, hauteur * 0.005)
    # On calcule les nouvelles dimensions, puis on les divises par le nombre de cases pour avoir la taille d'une case
    coordinateNW, coordinateSE = (largeur - center_width, hauteur - center_height), (center_width, center_height) # On récupère le point NW et SE, de la fenêtre qu'on a crée   
    new_dimension = (coordinateSE[0] - coordinateNW[0], coordinateSE[1] - coordinateNW[1]) # On fait la soustraction pour obtenir la largeur et la hauteur de la fenêtre
    box_size = ((new_dimension[0]) / nbBox), ((new_dimension[1]) / nbBox) # Puis on le divise par le nombre de case pour obtenir la taille d'une case 
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()