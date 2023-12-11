import Modules.fltk as fltk
import Modules.board as board
import Modules.math as calcu
from PIL import Image
# Normalement vous changez les constantes et ça s'adapte automatiquement
LARGEUR = 1000
HAUTEUR = 1000
NB_CASE = 7 # On doit avoir autant de case vertical et horizontale

fltk.cree_fenetre(LARGEUR, HAUTEUR)
fltk.image(LARGEUR/2, HAUTEUR/2, 'res/bg.gif', largeur=int(LARGEUR*1.77), hauteur=HAUTEUR, ancrage='center')

boxDimensions, margin, coordinateNW = calcu.size_box(LARGEUR, HAUTEUR, NB_CASE)

grid_lst = board.board_game(NB_CASE, NB_CASE, boxDimensions, coordinateNW)
tirette_h, tirette_v = calcu.create_tirette(NB_CASE)

def create_board(grid):
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
            #fltk.cercle(elem[0][0], elem[0][1], boxDimensions[0]/2 - margin[0])
            #print(int(boxDimensions[0] - 2*margin[0]))
            #print((boxDimensions[0]/2 - margin[0])*2)
            create_hole(x, y, elem)

def create_hole(tiretteX, tiretteY, coordinateBox):
    """
    This function will check each "tirette" to know if there's a hole,
    and depending of the answer, the fonction will display the right
    image on it.
    
    Arg: tiretteX / tiretteY list, coordinate of the center of each box
    
    Return: image on fltk depending of the answer 
    """
    if (tirette_v[tiretteX][tiretteY] == True) and (tirette_h[tiretteY][tiretteX] == True) :
         fltk.image(coordinateBox[0][0], coordinateBox[0][1], "res/hole.png", ancrage="center", 
                        largeur=int(boxDimensions[0]*0.7), 
                        hauteur=int(boxDimensions[1]*0.8))
    if (tirette_v[tiretteX][tiretteY] == True) and (tirette_h[tiretteY][tiretteX] == False) :
        fltk.image(coordinateBox[0][0], coordinateBox[0][1], "res/tirette_h.png", ancrage="center", 
                        largeur=int(boxDimensions[0]*1.1), 
                        hauteur=int(boxDimensions[1]*0.5 - 2*margin[1]))
    if (tirette_v[tiretteX][tiretteY] == False) and (tirette_h[tiretteY][tiretteX] == True) :
       fltk.image(coordinateBox[0][0], coordinateBox[0][1], "res/tirette_v.png", ancrage="center", 
                        largeur=int(boxDimensions[0]*0.5 - 2*margin[1]), 
                        hauteur=int(boxDimensions[1]*1.1))
    if (tirette_v[tiretteX][tiretteY] == False) and (tirette_h[tiretteY][tiretteX] == False) :
        fltk.image(coordinateBox[0][0], coordinateBox[0][1], "res/tirette_h.png", ancrage="center", 
                    largeur=int(boxDimensions[0]*1.1), 
                    hauteur=int(boxDimensions[1]*0.5 - 2*margin[1]))
        fltk.image(coordinateBox[0][0], coordinateBox[0][1], "res/tirette_v.png", ancrage="center", 
                        largeur=int(boxDimensions[0]*0.5 - 2*margin[1]), 
                        hauteur=int(boxDimensions[1]*1.1))

                  
create_board(grid_lst)

fltk.attend_ev()
fltk.ferme_fenetre()
