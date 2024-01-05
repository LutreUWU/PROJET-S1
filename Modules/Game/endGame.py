"""CODE FAIT PAR DAVID, ABDELKADER ET WALID."""


if __name__ != "__main__":
    import Modules.fltk as fltk

def end_page(player:str, LARGEUR:int, HAUTEUR:int, color:str, ball:int):
    """
    Une fonction qui affiche juste le vainqueur de la page
    
    Parametres : 
      player: Le nom du gagnant
      LARGEUR_windows: Largeur de la fenêtre (en px)
      HAUTEUR_windows: Hauteur de la fenêtre (en px)
      color : Couleur du gagnant
      ball : le nombre de balle qui lui reste
    Return :
      fltk
    """
    # On a fltk.efface_tout(), donc on remet l'image de fond
    fltk.image(LARGEUR/2, HAUTEUR/2, 'res/bg.gif', largeur=int(LARGEUR*1.77), hauteur=HAUTEUR, ancrage='center')
    winner = "Winner is " + player + f" with {ball} balls."
    end = "V A I N Q U E U R"
    # On utilise la fonction qui permet de trouver la taille de la police en fonction de la Largeur de la fenêtre
    font_size = 1
    taille = fltk.taille_texte(winner, taille=font_size)
    while taille[0] <= LARGEUR*0.8: # 0.8 pour avoir de la marge avec la fenêtre
        font_size += 1 
        taille = fltk.taille_texte(winner, taille=font_size)
    
    fltk.texte(LARGEUR / 2 , HAUTEUR / 4, end, couleur="black", ancrage="center", taille=font_size)
    fltk.texte(LARGEUR / 2, 3 * HAUTEUR / 4, winner, couleur=color, ancrage='center', taille=font_size)



