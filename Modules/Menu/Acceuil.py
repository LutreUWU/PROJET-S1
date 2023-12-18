import Modules.fltk as fltk
def create_menu(button_width, button_height, coordinate_button, hover):
    """
    fonction qui genere la page_principale du jeu
    parametres : 
        l : float width of the window
        h : float height of the window
        margin : tuple margin above and left
    return :
        dimension_rectangle : list contains dimension of rectangles
        l_case : float width of a rectangle
        h_case : float height of rectangle
    """
    button_name = ["Play", "How to play", "Settings"]
    for i, elem in enumerate(coordinate_button):
        if (hover != False) and (hover == i):
            color = "#dabd2c"
        else :
            color = "#125cc0"          
        fltk.rectangle(elem[0] - button_width/2 , elem[1] - button_height/2, 
                       elem[0] + button_width/2 , elem[1] + button_height/2, 
                       remplissage=color, tag="Acceuil")
        fltk.texte(elem[0], elem[1], button_name[i], couleur='black', tag="Acceuil"[i], ancrage="center")

def detection_rect(abs, ord, button_width, button_height, coordinate_button):
    """
    a function to detect if the mouse is in the rectangles , she takes in entry the list of dimension of the rectangles , 
    mouse_abscisse, mouse_ordonnée and width and height of a rectangle and j who is a hint to see if we update the page or not
    parametres : 
        lst : list
        x, y, l_case, h_case : float
        j : int
    
    return : 
        j : int
    """
    for i, elem in enumerate(coordinate_button):
        if abs > elem[0] - button_width/2 and abs < elem[0] + button_width/2: 
            if ord > elem[1] - button_height/2 and ord < elem[1] + button_height/2:
                return i 
    return False  
