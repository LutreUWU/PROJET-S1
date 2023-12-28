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
NB_CASE = 7 # On a autant de case vertical et horizontale
NB_BALLE = 3
fltk.cree_fenetre(LARGEUR, HAUTEUR)
# On Multiplie la largeur par 1.77 car l'image est au format 1920 * 1080 donc 1920/1080 = 1.77
fltk.image(LARGEUR/2, HAUTEUR/2, 'res/bg.gif', largeur=int(LARGEUR*1.77), hauteur=HAUTEUR, ancrage='center')
center_title, title_width_radius, title_height_radius = calcu.coordinate_center_title(LARGEUR, HAUTEUR)
button_width, button_height, coordinate_button = calcu.coordinate_center(LARGEUR, HAUTEUR)

Play = False
# Boucle while pour le menu du jeu, tant qu'on ne clique par sur "Play"
while Play == False: 
    click = fltk.donne_ev()
    type_click = fltk.type_ev(click)
    if type_click == 'Quitte':
        fltk.ferme_fenetre()
    # On regarde si la souris passe sur un bouton si c'est le cas alors hover renvoie l'indice du bouton, sinon elle renvoie False
    hover = acceuil.detection_rect(fltk.abscisse_souris(), fltk.ordonnee_souris(), 
                                   button_width, button_height, coordinate_button)
    if type_click == 'ClicGauche':
        if type(hover) == int and hover == 0: # Si on clique gauche et que hover == 0 veut dire que le curseur est sur le bouton "Play"
            Play = True # On arrête la boucle
    fltk.efface("Acceuil") # On efface tout pour actualiser la page
    # On affiche le titre du jeu
    acceuil.create_title(center_title, title_width_radius, title_height_radius)
    # On affiche les boutons en fonctions de la réponse de hover
    acceuil.create_menu(button_width, button_height, coordinate_button, hover)
    fltk.mise_a_jour() # On actualise le jeu

# On supprime le menu et on crée le plateau de jeu  
fltk.efface("Acceuil")
boxDimensions, margin, coordinateNW = calcu.size_box(LARGEUR, HAUTEUR, NB_CASE)
tirette_h, tirette_v = tirette.creation_tirette(NB_CASE)
compteur_tiretteh, compteur_tirettev = tirette.create_CompteurTirette(tirette_h, tirette_v)
grid_lst = board.board_game(NB_CASE, NB_CASE, boxDimensions, coordinateNW)
board.create_compteurTirette(compteur_tiretteh, compteur_tirettev, grid_lst, boxDimensions)
board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v)
fltk.mise_a_jour()
# Boucle while pour le fonctionnement du jeu
Setup_balls = False 
while not Setup_balls:
        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        #print(tev) if ev != None else None
        if tev == 'Quitte':
            break
        if tev == 'ClicGauche' and NB_BALLE > 0: #pour poser les balle au debut du jeu
           board.detect_click_case(fltk.abscisse_souris(), fltk.ordonnee_souris(),
                                   NB_CASE, margin, boxDimensions, coordinateNW
                                  )
        fltk.mise_a_jour() # On actualise le jeu
        
        
"""La boucle est infini pour l'instant, normalement quand on aura finis de placer la balle la boucle s'arrête"""


fltk.attend_ev()
fltk.ferme_fenetre()
