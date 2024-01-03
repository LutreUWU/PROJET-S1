if __name__ != "__main__":
    import Modules.fltk as fltk

def main_information(LARGEUR_windows, HAUTEUR_windows):
    """
    Une fonction qui affiche les informations sur le jeu. L'objectif est de centré le texte (Comme le "text-align:center" en CSS) avec la fenêtre,
    pour ce faire on va encore utiliser la fonction qui nous permet de trouver la taille de la police. 
    Paramètres:
        LARGEUR_windows: Largeur de la fenêtre (en px)
        HAUTEUR_windows: Hauteur de la fenêtre (en px)
    Return:
        fltk
    """
    # Une liste de texte, où chaque élément est une ligne de texte
    list_text = [
        "The objective of this project is to implement a multi-player strategy game called",           
        "Traps! (Stay alive! in English), developed by Milton Bradley in 19711.",
        "Figure 1: An example part", 
        "1 Rules of the game", 
        "The game consists of a 7×7 grid, with 14 zippers, 7 horizontal (orange)", 
        "and 7 vertical (white). Each zipper has a fixed number of holes, and can", 
        "be placed in three positions, by pushing or pulling on its ends. HAS", 
        "each point of the grid, when two holes are superimposed (that of the zipper", 
        "vertical and that of the horizontal pull), the ball located above falls, and the", 
        "player loses his ball. The game is played with 2, 3 or 4 players, each having 5", 
        "1Stay Alive, official website for the game. See also the 1994 French ad.", 
        "1 balls of your chosen color. The objective of the game is to be the last player to have", 
        "at least one ball on the board."]
    font_size = 1
    LongestSentence = ""
    # Pour chaque élément dans la liste, on va chercher la ligne de texte la plus longue
    for elem in list_text:
        if len(elem) > len(LongestSentence):
            LongestSentence = elem
    # Puis on utilise la fonction qui permet de trouver la taille de police, mais en fonction de la LARGEUR de la fenêtre
    taille = fltk.taille_texte(LongestSentence, taille=font_size)
    while taille[0] <= LARGEUR_windows*0.9: #90% de la largeur comme ça on à une marge avec le bord de la fenêtre
        font_size += 1 
        taille = fltk.taille_texte(LongestSentence, taille=font_size)
    # Après avoir obtenu la taille, on affiche chaque ligne de texte
    for i, elem in enumerate(list_text):
        fltk.texte(LARGEUR_windows/2, taille[1] + taille[1]*i, elem, ancrage="center", taille=font_size, tag="information") # i nous permet d'espacer les lignes de textes
    # Création du bouton pour revenir en arrière, il sera en bas à gauche 
    taille = fltk.taille_texte(" Retour ", font_size)
    # On crée le rectangle en fonction de la taille du texte
    # On multiplie par 0.01 comme ça on a une marge avec le bord de la fenêtre
    fltk.rectangle(LARGEUR_windows*0.01, HAUTEUR_windows - taille[1] - HAUTEUR_windows*0.01, 
                   LARGEUR_windows*0.01 + taille[0], HAUTEUR_windows - HAUTEUR_windows*0.01,
                   "black", remplissage="red", tag="information")
    # On divise par 2 et on change l'ancrage au centre car on veut que ce soit par rapport au centre du bouton
    fltk.texte(LARGEUR_windows*0.01 + taille[0]/2, HAUTEUR_windows - HAUTEUR_windows*0.01 - taille[1]/2 , " Retour ", taille=font_size, ancrage="center", tag="information")
    # Boucle qui va nous permettre de savoir si on clique sur le bouton Retour 
    Info_page = True
    while Info_page:
        click = fltk.donne_ev()
        type_click = fltk.type_ev(click)
        if type_click == 'Quitte':
            fltk.ferme_fenetre()
        if type_click == 'ClicGauche':
            abs = fltk.abscisse_souris()
            ord = fltk.ordonnee_souris()
            # Comme pour la page d'acceuil on regarde si l'abs et l'ord de la souris est entre les coordonnées du boutons 
            if LARGEUR_windows*0.01 < abs < LARGEUR_windows*0.01 + taille[0]:
                if HAUTEUR_windows - taille[1] - HAUTEUR_windows*0.01 < ord < HAUTEUR_windows - HAUTEUR_windows*0.01:
                    fltk.efface("information")
                    Info_page = False
        fltk.mise_a_jour()


