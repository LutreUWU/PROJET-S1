"""
CODE FAIT PAR DAVID, ABDELKADER ET WALID.
(A LIRE: Il y a 2 fichiers HTML, l'un est rédigé de manière profesionnelle, et l'autre est rédigé de manière "décontracté" avec quelques petites blague. Dans les 2 cas les fichiers renvoient les mêmes informations, ouvez celui que vous voulez en fonction de votre état d'humeur matinale !)

Quelques remarques :
- Dans ce jeu ON TIRE LES TIRETTES, on ne peut pas les pousser, donc par exemple s'il y a une tirette de 2 en bas il faudra cliquer en haut.
- Le jeu s'adapte à la taille de la fenêtre (Police d'écriture, taille de la grille de jeu, taille des boutons ...), c'est le point fort de ce code.
- Les seules constantes qu'on doit modifier dans le programme sont la LARGEUR et la HAUTEUR de le fenêtre, sinon on peut tout modifier sur le jeu.
- NORMALEMENT, toutes les valeurs numériques dans le code sont expliquées. 
- Tous les rectangles crées avec fltk sont basées sur son centre, donc les coordonnées du rectangles sont ceux de son centre (Je trouve que écrire "coordonnée centrale du rectangle" dans tous les doctrings était bizarre), 
  donc lorsque j'écris "coordonnée (x,y)", ça signifie le centre de chaque bouton. Y aura aussi beaucoup de "largeur/2" ou "hauteur/2" car on veut que la moitié pour créer le rectangle. 
- Il y a 3 boucles principales : 1 pour la page d'acceuil (Avec des "sous-boucles", vous allez comprendre pourquoi), 1 pour le placement des balles et 1 pour le jeu. Quand une boucle est active les autres sont inactives, donc dans le programme il y aura toujours que 1 seule boucle actif 
Pour plus d'informations, voir le fichier HTML

Bonne lecture.
"""
import Modules.fltk as fltk
# Ce module permet de faire la majorité des calculs (Centrer le jeu, La taille du jeu, la taille de la police ...)
import Modules.math as calcu
# Le module Game est tous ce qui est en rapport avec le plateau de jeu
import Modules.Game.board as board
import Modules.Game.clique as clique
import Modules.Game.tirette as tirette
import Modules.Game.joueur as player
# Le module Menu est tous ce qui est en rapport avec le menu du jeu, lorsu'on démarre le programme 
import Modules.Menu.Acceuil as acceuil
import Modules.Menu.setting as settings
import Modules.Menu.information as information
# Le module Game.endGame est l'affichaque quand on a finit la partie 
import Modules.Game.endGame as end
# Seul la largeur/hauteur doivent être changer dans le code, sinon on peut les changer dans le jeu
LARGEUR = 1000
HAUTEUR = 1000
# Pour ces 3 là on peut les changer dans la page d'acceuil quand on lance le programme, donc inutile de les changer 
NB_CASE = 7 
NB_BALLE = 2
NB_JOUEUR = 2
settingsGame = [NB_JOUEUR, NB_CASE, NB_BALLE]
# On crée la fenêtre, et on y ajoute un background
fltk.cree_fenetre(LARGEUR, HAUTEUR)
# On divise la LARGEUR/HAUTEUR par 2, et on change le point d'ancrage afin de récupérer le centre de l'image 
# On Multiplie la largeur par 1.77 car l'image est au format 1920 * 1080 donc 1920/1080 = 1.77
fltk.image(LARGEUR/2, HAUTEUR/2, 'res/bg.gif', largeur=int(LARGEUR*1.77), hauteur=HAUTEUR, ancrage='center')
# On récupère les données nécessaires pour construire la page d'acceuil
center_title, title_width, title_height = calcu.coordinate_center_title(LARGEUR, HAUTEUR) # Le centre, la largeur, et la hauteur du titre du jeu
button_width, button_height, coordinate_button = calcu.coordinate_center(LARGEUR, HAUTEUR) # La largeur et hauteur des boutons et les coordonnées (x, y) de chaque boutons 
Game, Information, Setting = False, False, False # Variables pour nous permettre d'être dans la boucle Acceuil 
# Boucle while pour le menu du jeu, tant qu'on ne clique pas sur un bouton les 3 paramètres sont en False 
while not Game and not Information and not Setting : 
    click = fltk.donne_ev()
    type_click = fltk.type_ev(click)
    if type_click == 'Quitte':
        fltk.ferme_fenetre()
    # On regarde si la souris passe sur un bouton si c'est le cas alors hover renvoie l'indice du bouton, sinon elle renvoie False
    hover = acceuil.detection_rect(fltk.abscisse_souris(), fltk.ordonnee_souris(), 
                                   button_width, button_height, coordinate_button)
    if type_click == 'ClicGauche':
        # On vérifie qu'on a cliqué sur un bouton, pour cela on va se servir de hover
        # hover renvoie un int lorsqu'on est sur un bouton, donc on vérifie, et en fonction de la valeur de hover on sait quel bouton on a cliqué 
        if type(hover) == int and hover == 0: # 0 veut dire que c'est le bouton Play
            # Alors Game est True car on a appuyé sur Play
            Game = True 
            # Comme Game est True, alors la boucle du menu d'acceuil s'arrête
        if type(hover) == int and hover == 1: # 1 veut dire que c'est le bouton Information
            Information = True
        if type(hover) == int and hover == 2: # 2 veut dire que c'est le bouton Settings
            # On récupère les données pour créer la page de setting
            coord_settingButton, size_settingButton = calcu.coordinate_center_settings(LARGEUR, HAUTEUR)
            # On récupère les données les boutons "+" et "-" pour chaque boutons settings.
            lessButton_coord, moreButton_coord, ButtonChange_size = calcu.coordinate_changeButton_settings(coord_settingButton, size_settingButton)
            Setting = True
    
    # En fonction de la variable True on va afficher la page correspondante
    if Information:
        fltk.efface("Acceuil") # On efface la page d'acceuil
        # Et on affiche les informations
        information.main_information(LARGEUR, HAUTEUR)
        # On a une boucle dans le main_information, donc quand on sera ici, alors on aura fermé la page information 
        Information = False 
    # Même chose pour les settings 
    if Setting:
        fltk.efface("Acceuil")
        settings.main_settings(settingsGame, coord_settingButton, size_settingButton,
                               lessButton_coord, moreButton_coord, ButtonChange_size)
        # On associe les nouvelles valeurs sauvegardées à nos Constantes
        NB_JOUEUR, NB_CASE, NB_BALLE = settingsGame[0], settingsGame[1], settingsGame[2]
        Setting = False
    # Donc on réactualise la page pour afficher la page d'acceuil 
    fltk.efface("Acceuil") 
    # On affiche le titre et les boutons du jeu
    acceuil.create_title(center_title, title_width, title_height)
    acceuil.create_menu(button_width, button_height, coordinate_button, hover)
    fltk.mise_a_jour() 

# Si on arrive ici ça veut dire qu'on a cliqué sur Play
# Donc on efface la page d'acceuil
fltk.efface("Acceuil")
# Tous les paramètres pour créer le jeu 
boxDimensions, margin, coordinateNW = calcu.size_box(LARGEUR, HAUTEUR, NB_CASE) # Dimensions d'une cases, marge entre les cases, et les coordonnées NW de la grille de jeu
tirette_h, tirette_v = tirette.creation_tirette(NB_CASE) # tirette_h et tirevve_v sont des listes de listes de booléenne
compteur_tiretteh, compteur_tirettev = tirette.create_CompteurTirette(tirette_h, tirette_v) # Liste de dictionnaire où chaque dictionnaire est le compteur d'une tirette 
NB_BALLE = board.verif_nombre_place(NB_BALLE, NB_JOUEUR, tirette_h, tirette_v)
playerlist = player.player_setup([], NB_JOUEUR) # Liste où chaque élément est un dictionnaire avec les paramètres de chaque joueurs
grid_lst = board.board_game(NB_CASE, NB_CASE, boxDimensions, coordinateNW) # Liste de liste de liste de 2 éléments (Un tuple (x,y) et une variable "0")
# Une fois tous les paramètres obtenus on peut créer le jeu  
board.compteurTirette(compteur_tiretteh, compteur_tirettev, grid_lst, boxDimensions) # Création des compteurs de tirettes 
board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v, False, None, compteur_tiretteh, compteur_tirettev, playerlist, 0) # Création du plateau de jeu 
player.aff_joueur(LARGEUR, 0, playerlist, NB_JOUEUR) # Création des joueurs (Le tour de qui, et Le nombre de balle qu'il a perdu)
fltk.mise_a_jour()
# Boucle while pour le placement des balles 
old_click = None # Pour nous permettre d'éviter qu'on place plusieurs balles sur la même case
ball_place = 0 # Nombre de balle placer sur le jeu 
# Tant que le setup des balls n'est pas terminé : 
Setup_balls = False
while not Setup_balls:
    ev = fltk.attend_ev()
    tev = fltk.type_ev(ev)
    if tev == 'Quitte':
        fltk.ferme_fenetre()
    # Si on a cliqué et que le nombre de balle placé est inférieur à la somme des balles de tous les joueurs 
    if tev == 'ClicGauche' and ball_place < NB_BALLE * NB_JOUEUR:
            # On appelle la fonction pour détecter sur quoi on clique
            # ball_case aura pour valeur un tuple avec l'indice de la case ou une liste avec l'indice du compteur, 
            ball_case = clique.detect_click(fltk.abscisse_souris(), fltk.ordonnee_souris(),
                                            NB_CASE, margin, boxDimensions, coordinateNW)
            # On vérifier qu'on a pas cliqué sur la même case plusieurs fois 
            if old_click != ball_case:
                old_click = ball_case
                # Si c'est un tuple alors on a cliqué sur une case (Car on a une liste quand on clique sur un compteur.)
                if type(ball_case) == tuple:
                    # On vérifie qu'il n'y a rien sur la case 
                    if grid_lst[ball_case[1]][ball_case[0]][1] == "0":
                        # On vérifie si la case qu'on a cliqué n'est pas un trou 
                        if board.check_hole(tirette_h, tirette_v, ball_case[0], ball_case[1], compteur_tiretteh, compteur_tirettev) != True:
                            # Si ce n'est pas le cas alors on place la balle sur cette case là
                            fltk.efface("board")
                            board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v, ball_case, playerlist[ball_place%NB_JOUEUR]["Color"], compteur_tiretteh, compteur_tirettev, playerlist, 0)
                            # Et on actualise les paramètres du joueur qui a placé la balle 
                            playerlist[ball_place%NB_JOUEUR]["Balle"] += 1
                            ball_place += 1
                            # Et on passe au tour du prochain joueur.
                            fltk.efface("turn")
                            player.aff_joueur(LARGEUR, ball_place, playerlist, NB_JOUEUR)
    fltk.mise_a_jour() # On actualise le jeu
    # Lorsqu'on a placer toutes les balles, on arrête la boucle while pour la placement des balles
    if ball_place == NB_BALLE * NB_JOUEUR:
        Setup_balls = True
# Début de la boucle qui permet de faire en sorte que les tirettes bougent, et que les balles tombent
forbidden_click = None # Va nous permettre de ne pas cliquer à l'opposé de la tirette où on a cliqué
playerTurn = 0 # Nous permettre de connaître quel joueur va jouer
# Tant qu'on joue au jeu
Gameplay = True
while Gameplay:
    fltk.efface("turn")
    # D'abord on vérifie si le joueur a toujours des balles dans le jeu 
    playerTurn = player.cherche_tour(playerTurn, playerlist) # Si c'est le cas on renvoie l'indice du joueur 
    # On affiche le tour du joueur correspond, et le nombre de balle que chaque joueur a perdu
    player.aff_tour(LARGEUR, playerlist, playerTurn)
    player.aff_NbBallejoueur(playerTurn, playerlist, NB_BALLE)
    # Début de la détection quand on clique sur la tirette
    ev = fltk.attend_ev()
    tev = fltk.type_ev(ev)
    if tev == 'Quitte':
        fltk.ferme_fenetre()
    if tev == 'ClicGauche' and ball_place > 0:
        # On re-appelle la fonction pour détecter le clique
        click_tirette = clique.detect_click(fltk.abscisse_souris(), fltk.ordonnee_souris(),
                                            NB_CASE, margin, boxDimensions, coordinateNW)
        # Puis on appelle la fonction qui vérifie si on a cliqué sur le compteur 
        forbidden_click, playerTurn = tirette.working_compteurTirette(click_tirette, compteur_tiretteh, compteur_tirettev, NB_CASE, playerTurn, forbidden_click)
        # On actualise les tirettes après avoir cliqué sur un compteur tirette 
        fltk.efface("tirette")
        board.compteurTirette(compteur_tiretteh, compteur_tirettev, grid_lst, boxDimensions)
        board.create_board(grid_lst, boxDimensions, margin, tirette_h, tirette_v, ball_case, playerlist[ball_place%NB_JOUEUR]["Color"], compteur_tiretteh, compteur_tirettev, playerlist, playerTurn)
        # On recompte combien de balle il reste en parcourant le dictionnaire 
        ball_place = 0
        for i in range(len(playerlist)):
            ball_place += playerlist[i]["Balle"] # On additionne les balles restantes de tout les joueurs
        for elem in playerlist:
            winner = None
            # Si un joueur possède toutes les balles restantes, alors on arrête la partie
            if ball_place in elem.values(): 
                # Si c'est le cas alors on arrête la boucle et on affiche le vainqueur
                winner = elem
                Gameplay = False
                fltk.efface_tout()
                # On affiche la page du vainqueur
                end.end_page(winner["Prenom"], LARGEUR, HAUTEUR, winner["Color"], winner["Balle"] )
    fltk.mise_a_jour() # On actualise le jeu
            
fltk.attend_ev()
fltk.ferme_fenetre()

