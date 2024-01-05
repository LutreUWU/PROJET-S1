"""CODE FAIT PAR DAVID, ABDELKADER ET WALID."""

if __name__ != "__main__":
    import Modules.fltk as fltk

def detection_rect(abs:int, ord:int, button_width:int, button_height:int, coordinate_button:list):
    """
    Une fonction qui détecte si on passe sur un bouton, si c'est le cas, alors elle renvoie l'indice du bouton
    qu'on a hover, sinon elle renvoie False
    Paramètres: 
        abscisse : Coordonnée x de la souris
        ordonnee : Coordonnée y de la souris
        button_width : largeur du bouton
        button_height : hauteur du bouton
        coordinate_button : Liste de tuple (x,y) de chaque boutons 
    Return : 
        L'indice du bouton, sinon False
    
    >>> detection_rect(0, 0, 400, 200, [(400, 500), (400, 500), (500, 500)]) 
    False
    >>> detection_rect(420, 510, 400, 200, [(400, 500), (400, 700), (400, 900)]) 
    0
    >>> detection_rect(310, 950, 400, 200, [(400, 400), (400, 700), (400, 900)]) 
    2
    """
    for i, elem in enumerate(coordinate_button): # Pour chaque coordonnées des boutons 
        if elem[0] - button_width/2 < abs < elem[0] + button_width/2: # Est ce que le curseur se trouve entre les coordonnées du bouton en largeur (x)
            if elem[1] - button_height/2 < ord < elem[1] + button_height/2: # Si c'est le cas, Est-il aussi entre les coordonnées du bouton en ordonnée 
                return i # Alors le curseur est sur ce bouton
    return False  


def create_title(center_title, title_width, title_height):
    """
    Une fonction qui va permettre de créer le titre du jeu sur fltk
    Paramètres:
        center_title : Coordonnées x,y du point où on va créer le titre (Au centre de la fenêtre, un peu plus haut)
        title_width_radius : Rayon du rectangle en largeur
        title_height_radius : Rayon du rectangle en hauteur
    
    Return : 
        Le titre du jeu sur fltk
    """
    game_name = 'S T A Y  A L I V E'
    # On utilise la fonction qui permet de trouver la taille de la police en fonction de la largeur d'un bouton;
    font_size = 1
    taille = fltk.taille_texte(game_name, taille=font_size)
    while taille[0] <= (title_width)*0.9: # 0.9 Pour avoir de la marge 
        taille = fltk.taille_texte(game_name, taille=font_size)
        font_size += 1        
    color_radiant = ["#00C7FF", "#00AEFF", "#0098FF", "#007FFF", "#0065FF"]
    fltk.texte(center_title[0], center_title[1], game_name, couleur="#3498db", taille=font_size, ancrage="center", tag="Acceuil")
    # On trace des rectangles de + en + grand avec une couleur légèrement différente pour faire un dégradé de couleur 
    for i in range(5):
        color = color_radiant[i]
        fltk.rectangle(center_title[0] - (title_width/2 + i), center_title[1] - (title_height/2 + i), 
                       center_title[0] + (title_width/2 + i), center_title[1] + (title_height/2 + i), 
                       couleur= color, epaisseur=3, tag="Acceuil")


def create_menu(button_width, button_height, coordinate_button, hover):
    """
    Fonction qui créer la page du jeu sur fltk
    Parametres : 
        button_width, button_height  : Dimensions de la fenêtre
        coordinate_button : Coordonnées du centre de chaque bouton 
        hover : L'indice du bouton qui est hover, si ce n'est pas le cas, renvoie False 
    Return :
        Les boutons sur fltk
    """
    # On utilise la fonction qui permet de trouver la taille de la police en fonction de la largeur d'un bouton;
    button_name = ["Play", "How to play", "Settings"]
    font_size = 1
    taille = fltk.taille_texte("How to play", taille=font_size) # on prend la taille du texte le plus long pour avoir la même taille
    while taille[0] <= button_width*0.7: # 0.7 pour avoir de la marge entre le bouton
        font_size += 1 
        taille = fltk.taille_texte("How to play", taille=font_size)
    # Pour chaque boutons : 
    for i, elem in enumerate(coordinate_button):
        # On regarde si on hover un bouton, et si c'est le même que celui du bouton
        if type(hover) == int and hover == i: 
            color = "#dabd2c" # si c'est la couleur du bouton sera celui quand on hover
        else :
            color = "#125cc0" # Sinon on garde la couleur de base
        # On divise par 2 car on veut le centre
        fltk.rectangle(elem[0] - button_width/2 , elem[1] - button_height/2, 
                       elem[0] + button_width/2 , elem[1] + button_height/2, 
                       remplissage=color, tag="Acceuil")
        fltk.texte(elem[0], elem[1], button_name[i], couleur='black', tag="Acceuil", taille=font_size, ancrage="center")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
   
