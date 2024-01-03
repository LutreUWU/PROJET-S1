if __name__ != "__main__":
    import Modules.fltk as fltk

def page_settings(coordButton:list, sizeButton:tuple, settings:list,
                  lessButton_coord:list, moreButton_coord:list, ButtonChange_size:tuple):
    """
    La fonction qui affiche la page settings grâce à fltk
    
    Paramètres:
        coordButton: Une liste de tuple avec les coordonnées (x,y) de chaque boutons 
        sizeButton: Un tuple avec la Largeur et la Hauteur du bouton 
        settings: Une liste de int avec les constantes qu'on peu modifier [NB_JOUEUR, NB_CASE, NB_BALLE]
        lessButton_coord: Une liste de tuple avec les coordonnées (x,y) de chaque "-"
        moreButton_coord: Une liste de tuple avec les coordonnées (x,y) de chaque "+"
        ButtonChange_size: Un tuple avec la Largeur et la Hauteur des boutons "-" et "    
    Return:
        fltk
    """
    # On ne peut pas baiser ou augmenter autant de fois certains paramètre    
    if settings[0] < 2: # On veut 2 joueurs minimum
        settings[0] = 2
    elif settings[0] > 6: # On veut 6 joueurs max (car on a une liste de 6 prénoms)
        settings[0] = 6 
    # On a placé un minimum, mais le programme marche même si on est en dessous (Vous pouvez modifier manuellement sur le main et vous verrez) 
    if settings[1] < 5: # On veut au moins 5 cases
        settings[1] = 5
    if settings[2] < 2: # On veut au moins 2 balles par joueur  
        settings[2] = 2
    # On récupère les valeurs de chaque paramètres
    liste_button = [(f'Number of player : {settings[0]}'), 
                    (f'Number of cases : {settings[1]}'), 
                    (f'Balls/Player : {settings[2]}'), 
                    (" save ")]
     # On utilise la fonction pôur trouver la taille de police en fonction de la taille d'un bouton 
    font_size = 1
    taille = fltk.taille_texte(f'Number of player : {settings[0]}', taille=font_size) # Pour que ce soit la même taille on a prit la phrase la plus longue 
    while taille[0] <= sizeButton[0]*0.8: # 80% du bouton pour avoir une marge 
        font_size += 1 
        taille = fltk.taille_texte(f'Number of player : {settings[0]}', taille=font_size)
    # Pour chaque bouton
    for i in range(4): # Car il y a 4 boutons
        if i == 3: # Pour le Bouton Save
            # On recalcule mais cette fois-ci avec "Save"
            font_size = 1
            taille = fltk.taille_texte(' Save ', taille=font_size)
            while taille[0] <= sizeButton[0]*0.8:
                font_size += 1 
                taille = fltk.taille_texte(f'Number of player : {settings[0]}', taille=font_size)
            # Pour éviter de créer d'autres variable on utilise la taille du bouton "+" et "-", et on obtient la dimension du bouton Save 
            fltk.rectangle(coordButton[i][0] - ButtonChange_size[0], coordButton[i][1] - ButtonChange_size[0]/2,
                           coordButton[i][0] + ButtonChange_size[0], coordButton[i][1] + ButtonChange_size[0]/2,
                           remplissage='red', tag='settings')
        else: # Pour les autres boutons 
        # On divise par 2 car on est dans au centre du bouton
            #Le bouton du milieu Milieu
            fltk.rectangle(coordButton[i][0] - sizeButton[0]/2, coordButton[i][1] - sizeButton[1]/2,
                           coordButton[i][0] + sizeButton[0]/2, coordButton[i][1] + sizeButton[1]/2,
                           remplissage='#125cc0', tag='settings')
            #Le bouton pour Diminuer à gauche du bouton du milieu
            fltk.rectangle(lessButton_coord[i][0] - ButtonChange_size[0]/2, lessButton_coord[i][1] - ButtonChange_size[1]/2,
                           lessButton_coord[i][0] + ButtonChange_size[0]/2, lessButton_coord[i][1] + ButtonChange_size[1]/2,
                           remplissage='#125cc0', tag='settings')
            fltk.texte(lessButton_coord[i][0], lessButton_coord[i][1], " - ", couleur='black', ancrage="center", taille=font_size, tag='settings')
            #Le bouton pour Augmenter à droite du bouton du milieu
            fltk.rectangle(moreButton_coord[i][0] - ButtonChange_size[0]/2, moreButton_coord[i][1] - ButtonChange_size[1]/2,
                           moreButton_coord[i][0] + ButtonChange_size[0]/2, moreButton_coord[i][1] + ButtonChange_size[1]/2,
                           remplissage='#125cc0', tag='settings')
            fltk.texte(moreButton_coord[i][0], moreButton_coord[i][1], " + ", couleur='black', ancrage="center", taille=font_size, tag='settings')
        # On affiche le texte prévu dans chacun des boutons du milieu
        fltk.texte(coordButton[i][0], coordButton[i][1], liste_button[i], couleur='black', ancrage="center", taille=font_size, tag='settings')
        

def main_settings(settingGame:list, coordButton:list, sizeButton:tuple,
                  lessButton_coord:list, moreButton_coord:list, ButtonChange_size:tuple):
    """
    Fonction principale qui va afficher la page des paramètres où on pourra modifier le nb de joueur, case
    et de balle dans la partie.Ces paramètres seront conservés lorsqu'on va quitter la page setting

    Args:
        settingGame: Une liste de int avec les constantes qu'on peu modifier [NB_JOUEUR, NB_CASE, NB_BALLE]
        coordButton: Une liste de tuple avec les coordonnées (x,y) de chaque boutons 
        sizeButton: Un tuple avec la Largeur et la Hauteur du bouton 
        lessButton_coord: Une liste de tuple avec les coordonnées (x,y) de chaque "-"
        moreButton_coord: Une liste de tuple avec les coordonnées (x,y) de chaque "+"
        ButtonChange_size: Un tuple avec la Largeur et la Hauteur des boutons "-" et "+"
    """
    # On affiche la page avec les paramètres grâce à fltk
    page_settings(coordButton, sizeButton, settingGame,
                  lessButton_coord, moreButton_coord, ButtonChange_size)
    # Boucle qui va nous permettre de modifier les paramètres
    Setting_page = True
    while Setting_page:
        click = fltk.donne_ev()
        type_click = fltk.type_ev(click)
        if type_click == 'Quitte':
            fltk.ferme_fenetre()
        # Chaque fois qu'on clique à gauche on va vérifier si on a touché un des 3 boutons "-" ou "+"
        if type_click == 'ClicGauche':
            abs = fltk.abscisse_souris()
            ord = fltk.ordonnee_souris()
            # Car y a 3 boutons où on peut augmenter et diminuer 
            for i in range(3):
                # Si on clique sur le bouton "-" 
                if lessButton_coord[i][0] - ButtonChange_size[0]/2  < abs < lessButton_coord[i][0] + ButtonChange_size[0]/2: # Comme pour les autres boutons on regarde si l'abscisse est entre une des 3 coordonnées des boutons "-"
                    if lessButton_coord[i][1] - ButtonChange_size[0]/2 < ord < lessButton_coord[i][1] + ButtonChange_size[0]/2: # On regarde l'ordonnée aussi
                        # Si c'est le cas alors on veut faire -1 aux paramètres du bouton où on a cliqué
                        settingGame[i] -= 1
                # Si on clique sur le bouton "+"
                if moreButton_coord[i][0] - ButtonChange_size[0]/2  < abs < moreButton_coord[i][0] + ButtonChange_size[0]/2: # Pareil mais pour les "+"
                    if moreButton_coord[i][1] - ButtonChange_size[0]/2 < ord < moreButton_coord[i][1] + ButtonChange_size[0]/2:
                        # Si c'est le cas alors on veut faire +1 aux paramètres du bouton où on a cliqué
                        settingGame[i] += 1
            # On efface toute la page et on réactualise les nouveaux paramètres
            fltk.efface("settings")
            page_settings(coordButton, sizeButton, settingGame,
                          lessButton_coord, moreButton_coord, ButtonChange_size)
            # On vérifie séparément le bouton Save (Car le bouton n'a pas les même dimensions que les autres)
            if coordButton[3][0] - ButtonChange_size[0] < abs < coordButton[3][0] + ButtonChange_size[0]:
                    if coordButton[3][1] - ButtonChange_size[0]/2 < ord < coordButton[3][1] + ButtonChange_size[0]/2:
                        # Si c'est le cas alors on sauvegarde les paramètres obtenus et on quitte la boucle Setting
                        fltk.efface("settings")
                        Setting_page = False
        fltk.mise_a_jour()

