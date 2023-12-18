import fltk 

def detection_save(x, y, p, c, b, l, h, margin, color, coordoonees_save):
    """
    a function change the color of the save button when the mouse is in there
    """
    if color == 'red':
        if (coordoonees_save[0][0][0] <= x and x <= coordoonees_save[0][1][0] and 
                coordoonees_save[0][0][1] <= y and y <= coordoonees_save[0][1][1]):
            fltk.efface_tout()
            p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings(l, h, margin, 'yellow', p, c, b)
    else:
        if (coordoonees_save[0][0][0] <= x and x <= coordoonees_save[0][1][0] and 
                coordoonees_save[0][0][1] <= y and y <= coordoonees_save[0][1][1]):
            pass
        else:
            fltk.efface_tout()
            p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings(l, h, margin, 'red', p, c, b)
    return color        

def page_settings(l, h, margin, color, p = 2, c = 7, b = 7):
    """
    a function who create a new page where we display settings

    """
    fltk.image(l / 2, h / 2, "res/bg.gif", 
                largeur=int(l * 1.77), hauteur=h, ancrage='center')
    marg = 20 # marge bettween rectangle
    l_case = l - 2 * margin[0]  # width of recatangle
    h_case = (h -  margin[1] - 2 * marg) / 5 # height of rectangle
    player_number = 'Number of player : '
    case_number = 'Number of cases : '
    bille_number = 'Number of billes : '
    if p < 2:
        number_player = 2
    else:
        number_player = p
    if c < 5:
        number_case = 5
    else:
        number_case = c
    if b < 4:
        number_bille = 4
    else:
        number_bille = b
    chaine = ''
    chainne = ''
    y_min = margin[1] / 4
    x_min = margin[0]
    for i in range(3):
        if i == 0:
            chaine = player_number
            chainne = number_player
        elif i == 1:
            chaine = case_number
            chainne = number_case
        else:
            chaine = bille_number
            chainne = number_bille
        cool = 'blue'
        fltk.rectangle(x_min, y_min, x_min + l_case, y_min + h_case, 
                       remplissage=cool, epaisseur=2)
        taille = fltk.taille_texte(chaine, taille=30)

        x = (2 * x_min + l_case - taille[0]) / 2 + 20
        y = (2 * y_min + h_case - taille[1]) / 2
        fltk.texte(x, y, chaine, couleur='black')
        fltk.texte(x + l_case / 3, y + 50, str(chainne))
        y_min += h_case + marg
    x_min = margin[0] - 20 - h_case
    x_max = l - margin[0] + 20
    y = margin[1] / 4
    liste_rectanglesupplimentaire = []
    for i in range(3):
        fltk.rectangle(x_min, y, x_min + h_case, y + h_case, 
                       epaisseur=2)
        fltk.rectangle(x_max, y, x_max + h_case, y + h_case, 
                        epaisseur=2)
        liste_rectanglesupplimentaire.append([x_min, x_max, y])
        y += h_case + marg
    cordonnees_save = []
    save_text = "save"
    taille_save = fltk.taille_texte(save_text, taille=30)
    fltk.rectangle(x_min, y, x_max + h_case, y + h_case, couleur=color, remplissage=color)
    fltk.texte((l - taille_save[0])/ 2, y + taille_save[1], save_text, taille=30)
    cordonnees_save.append([(x_min,  y), (x_max, y + h_case)])
    return number_player, number_case, number_bille, liste_rectanglesupplimentaire, h_case, cordonnees_save, l_case, color


def main_settings(l, h, margin,p = 2, c = 4, b = 4):
    p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings(l, h, margin, 'red', p, c, b)
    while True:
        click = fltk.donne_ev()
        type_clic = fltk.type_ev(click)
        if type_clic == 'Quitte':
            fltk.ferme_fenetre()
        if type_clic == 'ClicGauche':
            x = fltk.abscisse(click)
            y = fltk.ordonnee(click)
            for i in range(len(liste_bouton)):
                if i == 0:
                    if (liste_bouton[i][0] <= x <= liste_bouton[i][0] + h_case and 
                        liste_bouton[i][2] <= y <= liste_bouton[i][2] + h_case):
                        fltk.efface_tout()
                        p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings( 
                                                                    l, h, margin, 'red', p - 1, c, b)
                    elif (liste_bouton[i][1] <= x <= liste_bouton[i][1] + h_case and 
                        liste_bouton[i][2] <= y <= liste_bouton[i][2] + h_case):
                        fltk.efface_tout()
                        p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings( 
                                                                    l, h, margin, 'red', p + 1, c, b)
                elif i == 1:
                    if (liste_bouton[i][0] <= x <= liste_bouton[i][0] + h_case and 
                        liste_bouton[i][2] <= y <= liste_bouton[i][2] + h_case):
                        fltk.efface_tout()
                        p, c, b, liste_bouton, h_case, coordoonees_save,l_case, color = page_settings( 
                                                                   l, h, margin, 'red', p, c - 1, b)
                    elif (liste_bouton[i][1] <= x <= liste_bouton[i][1] + h_case and 
                        liste_bouton[i][2] <= y <= liste_bouton[i][2] + h_case):
                        fltk.efface_tout()
                        p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings(
                            l, h, margin, 'red', p, c + 1, b)
                elif i == 2:
                    if (liste_bouton[i][0] <= x <= liste_bouton[i][0] + h_case and 
                        liste_bouton[i][2] <= y <= liste_bouton[i][2] + h_case):
                        fltk.efface_tout()
                        p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings( 
                                                                   l, h, margin, 'red', p, c, b - 1)
                    elif (liste_bouton[i][1] <= x <= liste_bouton[i][1] + h_case and 
                        liste_bouton[i][2] <= y <= liste_bouton[i][2] + h_case):
                        fltk.efface_tout()
                        p, c, b, liste_bouton, h_case, coordoonees_save, l_case, color = page_settings(l, 
                                                                h, margin, 'red', p, c, b + 1)
            if (coordoonees_save[0][0][0] <= x and x <= coordoonees_save[0][1][0] and 
                coordoonees_save[0][0][1] <= y and y <= coordoonees_save[0][1][1]):
                fltk.efface_tout()
                from page_principale import main_page_principale
                main_page_principale(l, h, p, c, b)

        x_souris = fltk.abscisse_souris()
        y_souris = fltk.ordonnee_souris()
        color = detection_save(x_souris, y_souris, p, c, b, l, h, margin, color, coordoonees_save)

        fltk.mise_a_jour()
    fltk.ferme_fenetre()


