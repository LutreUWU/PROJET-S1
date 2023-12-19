if __name__ != "__main__":
    import Modules.fltk as fltk

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
    button_name = ["Play", "How to play", "Settings"]
    for i, elem in enumerate(coordinate_button):
        if type(hover) == int and hover == i:
            color = "#dabd2c"
        else :
            color = "#125cc0"          
        fltk.rectangle(elem[0] - button_width/2 , elem[1] - button_height/2, 
                       elem[0] + button_width/2 , elem[1] + button_height/2, 
                       remplissage=color, tag="Acceuil")
        fltk.texte(elem[0], elem[1], button_name[i], couleur='black', tag="Acceuil", ancrage="center")

def detection_rect(abs, ord, button_width, button_height, coordinate_button):
    """
    Une fonction qui détecte si on passe sur un bouton, si c'est le cas, alors on change la couleur du bouton
    Paramètres: 
        abscisse : Coordonnée x de la souris
        ordonnee : Coordonnée y de la souris
        button_width : largeur du bouton
        button_height : longueur du bouton
        coordinate_button : les coordonnées (x,y) du boutons
    
    Return : 
        L'indice du bouton, sinon False 
    """
    for i, elem in enumerate(coordinate_button):
        if abs > elem[0] - button_width/2 and abs < elem[0] + button_width/2: 
            if ord > elem[1] - button_height/2 and ord < elem[1] + button_height/2:
                return i 
    return False  


def create_title(center_title, title_width_radius, title_height_radius):
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
    color_radiant = ["#00C7FF", "#00AEFF", "#0098FF", "#007FFF", "#0065FF"]
    fltk.texte(center_title[0], center_title[1], game_name, couleur="#3498db", taille=50, ancrage="center", tag="Acceuil")
    #On trace des rectangles de + en + grand avec une couleur légèrement différente pour faire un dégradé de couleur 
    for i in range(5):
        color = color_radiant[i]
        fltk.rectangle(center_title[0] - (title_width_radius + i), center_title[1] - (title_height_radius + i), 
                       center_title[0] + (title_width_radius + i), center_title[1] + (title_height_radius + i), 
                       couleur= color, epaisseur=2, tag="Acceuil")


    
   
