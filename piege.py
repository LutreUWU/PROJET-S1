from PIL import Image
import Modules.fltk as fltk
# On importe les fcts pour créer et faire fonctionner le jeu
import Modules.Game.math as calcu
import Modules.Game.board as board
import Modules.Game.clique as clique
import Modules.Game.tirette as tirette
# On importe les fcts pour l'acceuil
import Modules.Menu.Acceuil as acceuil
import Modules.Game.joueur as player


# Normalement vous changez les constantes et ça s'adapte automatiquement
LARGEUR = 1000
HAUTEUR = 1000
NB_CASE = 7 # On a autant de case vertical et horizontale
NB_BALLE = 2
NB_JOUEUR = 6



fltk.cree_fenetre(LARGEUR, HAUTEUR)
# On Multiplie la largeur par 1.77 car l'image est au format 1920 * 1080 donc 1920/1080 = 1.77
fltk.image(LARGEUR/2, HAUTEUR/2, 'res/bg.gif', largeur=int(LARGEUR*1.77), hauteur=HAUTEUR, ancrage='center')
center_title, title_width_radius, title_height_radius = calcu.coordinate_center_title(LARGEUR, HAUTEUR)
button_width, button_height, coordinate_button = calcu.coordinate_center(LARGEUR, HAUTEUR)
Play = False
# Boucle while pour le menu du jeu, tant qu'on ne clique par sur "Play"
while not Play: 
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
playerlist = player.player_setup([], NB_JOUEUR)
grid_lst = board.board_game(NB_CASE, NB_CASE, boxDimensions, coordinateNW)
board.compteurTirette(compteur_tiretteh, compteur_tirettev, grid_lst, boxDimensions)
board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v, False, None, compteur_tiretteh, compteur_tirettev, playerlist, 0)
player.aff_joueur(LARGEUR, 0, playerlist, NB_JOUEUR)
fltk.mise_a_jour()
# Boucle while pour le fonctionnement du jeu
old_click = None
ball_place = 0 # Nombre de balle placer sur le jeu 
Setup_balls = False
while not Setup_balls:
    ev = fltk.attend_ev()
    tev = fltk.type_ev(ev)
    #print(tev) if ev != None else None
    if tev == 'Quitte':
        break
    if tev == 'ClicGauche' and ball_place < NB_BALLE * NB_JOUEUR: #pour poser les balle au debut du jeu
            ball_case = clique.detect_click(fltk.abscisse_souris(), fltk.ordonnee_souris(),
                                            NB_CASE, margin, boxDimensions, coordinateNW)
            if old_click != ball_case:
                old_click = ball_case
                if type(ball_case) == tuple:
                    if grid_lst[ball_case[1]][ball_case[0]][1] == "0": # Vérifier si y a pas déja une balle sur la case
                        if board.check_hole(tirette_h, tirette_v, ball_case[0], ball_case[1], compteur_tiretteh, compteur_tirettev) != True:
                            fltk.efface("board")
                            board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v, ball_case, playerlist[ball_place%NB_JOUEUR]["Color"], compteur_tiretteh, compteur_tirettev, playerlist, 0)
                            playerlist[ball_place%NB_JOUEUR]["Balle"] += 1
                            ball_place += 1
                            fltk.efface("turn")
                            player.aff_joueur(LARGEUR, ball_place, playerlist, NB_JOUEUR)

    fltk.mise_a_jour() # On actualise le jeu
    if ball_place == NB_BALLE * NB_JOUEUR:
        Setup_balls = True

forbidden_click = None
playerTurn = 0
Gameplay = True
while Gameplay:
    fltk.efface("turn")
    playerTurn = player.cherche_tour(playerTurn, playerlist) #Vérifier si le jouer à
    player.aff_tour(LARGEUR, playerlist, playerTurn)
    player.aff_NbBallejoueur(playerTurn, playerlist, NB_BALLE)
    ev = fltk.attend_ev()
    tev = fltk.type_ev(ev)
    if tev == 'Quitte':
        break
    if tev == 'ClicGauche' and ball_place > 0:
        click_tirette = clique.detect_click(fltk.abscisse_souris(), fltk.ordonnee_souris(),
                                            NB_CASE, margin, boxDimensions, coordinateNW)
        if type(click_tirette) == list and click_tirette != forbidden_click:
            if click_tirette[0] < 0 and compteur_tiretteh[click_tirette[1]]["gauche"] <= -click_tirette[0]:
                if click_tirette[0] == -1 and compteur_tiretteh[click_tirette[1]]["gauche"] < 2 :
                    compteur_tiretteh[click_tirette[1]]["gauche"] += 1
                    compteur_tiretteh[click_tirette[1]]["droite"] -= 1
                    forbidden_click = [abs(click_tirette[0] - NB_CASE), click_tirette[1]]
            elif click_tirette[0] > NB_CASE and compteur_tiretteh[click_tirette[1]]["droite"] <= click_tirette[0]:
                if click_tirette[0] == NB_CASE + 1 and compteur_tiretteh[click_tirette[1]]["droite"] < 2 :
                    compteur_tiretteh[click_tirette[1]]["gauche"] -= 1
                    compteur_tiretteh[click_tirette[1]]["droite"] += 1
                    forbidden_click = [-(click_tirette[0] - NB_CASE), click_tirette[1]]
            elif click_tirette[1] < 0 and compteur_tirettev[click_tirette[0]]["haut"] <= -click_tirette[1]:
                if click_tirette[1] == -1 and compteur_tirettev[click_tirette[0]]["haut"] < 2 :
                    compteur_tirettev[click_tirette[0]]["haut"] += 1
                    compteur_tirettev[click_tirette[0]]["bas"] -= 1
                    forbidden_click = [click_tirette[0], abs(click_tirette[1] - NB_CASE)]

            elif click_tirette[1] > NB_CASE and compteur_tirettev[click_tirette[0]]["bas"] <= click_tirette[1]:
                if click_tirette[1] == NB_CASE + 1 and compteur_tirettev[click_tirette[0]]["bas"] < 2 :
                    compteur_tirettev[click_tirette[0]]["haut"] -= 1
                    compteur_tirettev[click_tirette[0]]["bas"] += 1
                    forbidden_click = [click_tirette[0], -(click_tirette[1] - NB_CASE)]
 
            
            fltk.efface("tirette")
            board.compteurTirette(compteur_tiretteh, compteur_tirettev, grid_lst, boxDimensions)
            board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v, ball_case, playerlist[ball_place%NB_JOUEUR]["Color"], compteur_tiretteh, compteur_tirettev, playerlist, playerTurn)
            playerTurn += 1
        # On recompte combien de balle il reste en parcourant le dictionnaire 
        ball_place = 0
        for i in range(len(playerlist)):
            ball_place += playerlist[i]["Balle"]
        for elem in playerlist:
            if ball_place in elem.values():
                Gameplay == False
        else:
            fltk.mise_a_jour() # On actualise le jeu
fltk.attend_ev()
fltk.ferme_fenetre()

