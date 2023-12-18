if __name__ == "__main__":
    import fltk as fltk
else:
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
        fltk.texte(elem[0], elem[1], button_name[i], couleur='black', tag="Acceuil"[i], ancrage="center")

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
