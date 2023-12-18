from PIL import Image
import Modules.fltk as fltk
# On importe les fcts pour créer et faire fonctionner le jeu
import Modules.Game.math as calcu
import Modules.Game.board as board
import Modules.Game.tirette as tirette
# On importe les fcts pour l'acceuil
import Modules.Menu.Acceuil as acceuil


# Normalement vous changez les constantes et ça s'adapte automatiquement
LARGEUR = 1000
HAUTEUR = 1000
NB_CASE = 7 # On doit avoir autant de case vertical et horizontale

fltk.cree_fenetre(LARGEUR, HAUTEUR)
# On Multiplie la largeur par 1.77 car l'image est au format 1920 * 1080 donc 1920/1080 = 1.77
fltk.image(LARGEUR/2, HAUTEUR/2, 'res/bg.gif', largeur=int(LARGEUR*1.77), hauteur=HAUTEUR, ancrage='center')
button_width, button_height, coordinate_button = calcu.coordinate_center(LARGEUR, HAUTEUR)

while True:
    click = fltk.donne_ev()
    type_click = fltk.type_ev(click)
    if type_click == 'Quitte':
        fltk.ferme_fenetre()
    hover = acceuil.detection_rect(fltk.abscisse_souris(), fltk.ordonnee_souris(), 
                                   button_width, button_height, coordinate_button)
    fltk.efface("Acceuil")
    acceuil.create_menu(button_width, button_height, coordinate_button, hover)
    fltk.mise_a_jour()
        



"""boxDimensions, margin, coordinateNW = calcu.size_box(LARGEUR, HAUTEUR, NB_CASE)
tirette_h, tirette_v = calcu.create_tirette(NB_CASE)

grid_lst = board.board_game(NB_CASE, NB_CASE, boxDimensions, coordinateNW)
board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v)"""



                  

fltk.attend_ev()
fltk.ferme_fenetre()
