if __name__ != "__main__":
    import Modules.fltk as fltk

def page_settings(coordButton, sizeButton, settings,
                  lessButton_coord, moreButton_coord, ButtonChange_size):
    """
    a function who create a new page where we display settings

    """    
    if settings[0] < 2:
        settings[0] = 2
    elif settings[0] > 6:
        settings[0] = 6
    if settings[1] < 5:
        settings[1] = 5
    if settings[2] < 2:
        settings[2] = 2
 
    liste_button = [(f'Number of player : {settings[0]}'), 
                    (f'Number of cases : {settings[1]}'), 
                    (f'Balls/Player : {settings[2]}'), 
                    (" save ")]
    
    font_size = 1
    taille = fltk.taille_texte(f'Number of player : {settings[0]}', taille=font_size)
    while taille[0] <= sizeButton[0]*0.8:
        font_size += 1 
        taille = fltk.taille_texte(f'Number of player : {settings[0]}', taille=font_size)
    
    for i in range(4):
        if i == 3: # Bouton Save
            font_size = 1
            taille = fltk.taille_texte(' Save ', taille=font_size)
            while taille[0] <= sizeButton[0]*0.8:
                font_size += 1 
                taille = fltk.taille_texte(f'Number of player : {settings[0]}', taille=font_size)
            fltk.rectangle(coordButton[i][0] - ButtonChange_size[0], coordButton[i][1] - ButtonChange_size[0]/2,
                           coordButton[i][0] + ButtonChange_size[0], coordButton[i][1] + ButtonChange_size[0]/2,
                           remplissage='red', tag='settings')
        else:
            #Milieu
            fltk.rectangle(coordButton[i][0] - sizeButton[0]/2, coordButton[i][1] - sizeButton[1]/2,
                           coordButton[i][0] + sizeButton[0]/2, coordButton[i][1] + sizeButton[1]/2,
                           remplissage='#125cc0', tag='settings')
            # Diminuer
            fltk.rectangle(lessButton_coord[i][0] - ButtonChange_size[0]/2, lessButton_coord[i][1] - ButtonChange_size[1]/2,
                           lessButton_coord[i][0] + ButtonChange_size[0]/2, lessButton_coord[i][1] + ButtonChange_size[1]/2,
                           remplissage='#125cc0', tag='settings')
            fltk.texte(lessButton_coord[i][0], lessButton_coord[i][1], " - ", couleur='black', ancrage="center", taille=font_size, tag='settings')
            # Augmenter
            fltk.rectangle(moreButton_coord[i][0] - ButtonChange_size[0]/2, moreButton_coord[i][1] - ButtonChange_size[1]/2,
                           moreButton_coord[i][0] + ButtonChange_size[0]/2, moreButton_coord[i][1] + ButtonChange_size[1]/2,
                           remplissage='#125cc0', tag='settings')
            fltk.texte(moreButton_coord[i][0], moreButton_coord[i][1], " + ", couleur='black', ancrage="center", taille=font_size, tag='settings')

        fltk.texte(coordButton[i][0], coordButton[i][1], liste_button[i], couleur='black', ancrage="center", taille=font_size, tag='settings')
        

def main_settings(settingGame:list, coordButton:list, sizeButton:tuple,
                  lessButton_coord:list, moreButton_coord:list, ButtonChange_size:tuple):
    """
    Fonction qui va afficher la page des paramètres où on pourra modifier le nb de joueur, case
    et de balle dans la partie.Ces paramètres seront conservés lorsqu'on va quitter la page setting

    Args:
        settingGame (_type_): _description_
        coordButton (list): _description_
        sizeButton (tuple): _description_
        lessButton_coord (_type_): _description_
        moreButton_coord (_type_): _description_
        ButtonChange_size (_type_): _description_
    """
    page_settings(coordButton, sizeButton, settingGame,
                  lessButton_coord, moreButton_coord, ButtonChange_size)
    Setting_page = True
    while Setting_page:
        click = fltk.donne_ev()
        type_click = fltk.type_ev(click)
        if type_click == 'Quitte':
            fltk.ferme_fenetre()
        if type_click == 'ClicGauche':
            add = 0
            abs = fltk.abscisse_souris()
            ord = fltk.ordonnee_souris()
            # Car y a 3 boutons où on peut augmenter et diminuer 
            for i in range(3):
                # Si on clique sur le bouton "-" 
                if lessButton_coord[i][0] - ButtonChange_size[0]/2  < abs < lessButton_coord[i][0] + ButtonChange_size[0]/2:
                    if lessButton_coord[i][1] - ButtonChange_size[0]/2 < ord < lessButton_coord[i][1] + ButtonChange_size[0]/2:
                        add = -1
                        settingGame[i] += add

                if moreButton_coord[i][0] - ButtonChange_size[0]/2  < abs < moreButton_coord[i][0] + ButtonChange_size[0]/2:
                    if moreButton_coord[i][1] - ButtonChange_size[0]/2 < ord < moreButton_coord[i][1] + ButtonChange_size[0]/2:
                        add = 1
                        settingGame[i] += add
            fltk.efface("settings")
            page_settings(coordButton, sizeButton, settingGame,
                          lessButton_coord, moreButton_coord, ButtonChange_size)
            
            taille = fltk.taille_texte(" save ")
            if coordButton[3][0] - ButtonChange_size[0] < abs < coordButton[3][0] + ButtonChange_size[0]:
                    if coordButton[3][1] - ButtonChange_size[0]/2 < ord < coordButton[3][1] + ButtonChange_size[0]/2:
                        fltk.efface("settings")
                        Setting_page = False
        fltk.mise_a_jour()

