if __name__ != "__main__":
    import Modules.fltk as fltk

def end_page(player, LARGEUR, HAUTEUR, color, ball):
    """
    a function who display the winner and end the game
    parametres : 
      player: the winner str
      l : width of the window
      h : height of he window
      color : color of the player's name str
    """
    winner = "winner is " + player + f" avec {ball} balles."
    end = "V A I N Q U E U R"
    fltk.image(LARGEUR/2, HAUTEUR/2, 'res/bg.gif', largeur=int(LARGEUR*1.77), hauteur=HAUTEUR, ancrage='center')
    fltk.texte(LARGEUR / 2 , HAUTEUR / 4, end, couleur="black", ancrage="center", taille=50)
    fltk.texte(LARGEUR / 2, 3 * HAUTEUR / 4, winner, couleur=color, ancrage='center', taille=50)



