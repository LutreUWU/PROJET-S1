if __name__ != "__main__":
   import Modules.fltk as fltk

def detect_click(abs:int, ord:int, NB_CASE:int, margin:tuple, boxDimensions:tuple, coordinateNW:tuple):
    """
    Fonction qui va permettre de détecter si on clique sur une case ou non, si c'est le cas,
    elle va renvoyer l'indice de la case.
    Le problème majeur était de vérifier qu'on ne clique pas entre les cases.
    La solution est de vérifier 1 par 1 chaque case en rajoutant la marge 1 par 1    
    
    La fonction va aussi détecter si on clique sur un compteur de tirette, si c'est le cas alors elle va appeller
    une autre fonction qui va vérifier si on a bien cliquer sur un compteur.
    
    Paramètres:
        abs: Coordonnée X de la souris
        ord: Coordonnée Y de la souris
        margin: Un tuple avec les marge (x,y) entre les cases
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
        coordinateNW : Coordonnées (x,y) de la fenêtre qu'on a crée (pour faire la marge avec la fenêtre windows) 
    Returns:
        tuple (x,y) de la case qu'on a cliqué 
        ou
        liste [x,y] du compteur tirette qu'on a cliqué 
    
    >>> detect_click(20, 20, 7, (5, 5), (50, 50), (10, 10))
    (0, 0)
    """
    # On cherche comme si il n'y avait pas de marge entre les cases 
    # On va soustraite l'abscisse par le point d'origine, puis son va diviser par la taille d'une case, pour connaître c'est quelle cases qu'on clique
    nb_case_x = int((abs - coordinateNW[0]) // boxDimensions[0])
    nb_case_y = int((ord - coordinateNW[1]) // boxDimensions[1])
    # Variables qui va permettre de vérifier si on a cliqué entre les cases ou pas 
    positionX, positionY = coordinateNW[0], coordinateNW[1] # Origine des points
    # Dans le cas où on a cliqué hors de la grille :
    # Si on clique à gauche ou en haut de la grille
    if nb_case_x < 0 or nb_case_y < 0: 
        # Si on a cliqué à gauche alors on vérifie pour le côté Gauche
        if nb_case_x < 0 and 0 <= nb_case_y < NB_CASE:
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Gauche") # Alors on renvoie l'indice du compteur où on a cliqué 
        # Si on a cliqué en haut alors on vérifie pour le côté Haut
        elif nb_case_y < 0 and NB_CASE > nb_case_x >= 0: 
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Haut")
    # Si on clique à droite ou en bas de la grille
    if nb_case_x >= NB_CASE or nb_case_y >= NB_CASE: 
        # Si on a cliqué à droite alors on vérifie pour le côté Droite
        if nb_case_x >= NB_CASE and 0 <= nb_case_y < NB_CASE:  
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Droite")
        # Si on a cliqué en bas alors on  vérifie pour le côté Bas
        elif nb_case_y == NB_CASE and NB_CASE > nb_case_x >= 0 : 
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Bas")
    # Dans la suite du code on est dans le cas si on a cliqué sur une case de la grille :
    checkX, checkY = False, False # Si les 2 sont True alors on a cliqué entre les cases
    # On commmence tout d'abord avec l'abscisse  
    for i in range(nb_case_x + 1 ): # +1 car si on commence à 0, comme la 1er case a pour indice 0, le for ne va pas s'activer.
        # A la première case on ajoute la marge 1 fois
        if i == 0: 
            left_positionX = positionX + margin[0]
        else:         
            # Puis pour le reste on ajoute 2 fois la marge  
            left_positionX = positionX + margin[0]*2
        # Puis on avance la position originale de la taille de la case
        positionX = left_positionX + (boxDimensions[0] - 2*margin[0])
        if left_positionX <= abs <= positionX: # Puis on vérifie si l'abs est entre les 2 points 
             checkX = True # Si c'est le cas alors on est sur une case X
             # Pour voir sur fltk effacer les """     
             """fltk.cercle(left_positionX, ord,
                         3, couleur="black", remplissage="black")
             fltk.cercle(positionX, ord,
                         3, couleur="black", remplissage="black")"""
    # Pareil pour l'ordonnée
    for i in range(nb_case_y + 1 ):
        if i == 0:
            left_positionY = positionY + margin[1]
        else:
            left_positionY = positionY + margin[1]*2
        positionY = left_positionY + (boxDimensions[1] - 2*margin[1])
        if left_positionY <= ord <= positionY: 
             checkY = True # Si c'est le cas alors on est sur une case Y
             # Pour voir sur fltk effacer les """         
             """fltk.cercle(abs, left_positionY,
                         3, couleur="blue", remplissage="blue")
             fltk.cercle(abs, positionY,
                         3, couleur="blue", remplissage="blue")"""
    # Si checkX and checkY alors on a cliqué sur une case et on renvoie l'indice de la case
    if checkX and checkY:
        return nb_case_x, nb_case_y
    # Sinon on renvoie False
    else: 
        return False
    
def detect_click_compteur(abs:int, ord:int, nb_caseX:int, nb_caseY:int, coordinateNW:tuple, boxDimensions:tuple, NB_CASE:int, direction:str):
    """
    Fonction qui va permettre de savoir si on a cliqué sur un compteur tirette (les petits cercles), 
    pour cela on va trouver les extremités des petits cercles et on va vérifier si on entre ses extrémités là. 
    
    La fonction a été appellé par la fonction detec_click dans le cas où on a cliqué en dehors de la grille du jeu.

    Paramètres:
        abs: Coordonnée X de la souris
        ord: Coordonnée Y de la souris
        nb_caseX (int): Ce qui nous permet de savoir on a cliqué où (Les compteur à gauche ont comme valeur -1 et -2, tandis que les droites ont comme valeur NB_CASE + 1 et NB_CASE + 2)
        nb_caseY (int): Ce qui nous permet de savoir on a cliqué où (Les compteur en haut ont comme valeur -1 et -2, tandis que les bas ont comme valeur NB_CASE + 1 et NB_CASE + 2)
        coordinateNW : Coordonnées (x,y) de la fenêtre qu'on a crée (pour faire la marge avec la fenêtre windows) 
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
        NB_CASE (int): Nombre de cases
        direction (str): String avec la direction dont a cliqué, et en fonction de la direction on va vérifier si on a bien appuyé sur la tirette

    Returns:
        Tuple (x,y) avec les indices du compteur tirettes
    >>> detect_click_compteur(139, 197, -1, 0, (160.0, 160.0), (68.57142857142857, 68.57142857142857), 7 , "Gauche")
    [-1, 0]
    >>> detect_click_compteur(0, 0, -1, 0, (160.0, 160.0), (68.57142857142857, 68.57142857142857), 7 , "Gauche")
    
    """
    # Rayon du petit cercle
    radius = boxDimensions[0]//5
    # Si on a cliqué à gauche de la grille 
    if direction == "Gauche":
        # On regarde si on a cliqué sur le 2ème cran
        if coordinateNW[0] + boxDimensions[0]/2 * -2 + 2*radius > abs: # On regarde juste si on a dépassé le cercle du 1er cran
            nb_caseX = nb_caseX - 1 # Si c'est le cas alors l'indice du compteur est -2
        # On cherche les tuples (x, y) qui vont représentés les bordures du petit cercle  
        border_position1 = (coordinateNW[0] + boxDimensions[0]/2 * nb_caseX + 2*radius, # Droite du cercle
                            coordinateNW[1] + boxDimensions[1] * nb_caseY + boxDimensions[1]/2 - radius) # Haut du cercle
        border_position2 = (coordinateNW[0] + boxDimensions[0]/2 * nb_caseX, # Gauche du cercle
                            coordinateNW[1] + boxDimensions[1]*nb_caseY + boxDimensions[1]/2 + radius) # Bas du cercle
        # Puis on vérifie si on est entre les coordonnées 
        if (border_position1[1] < ord < border_position2[1]) and (border_position1[0] > abs > border_position2[0]):
            return [nb_caseX, nb_caseY]
    # Puis on fait pareil pour les autres directions
    elif direction == "Haut":
        if coordinateNW[1] + boxDimensions[1]/2 * -2 + 2*radius > ord: # Si on touche la 2ème case
            nb_caseY = nb_caseY - 1
        border_position1 = (coordinateNW[0] + boxDimensions[0] * nb_caseX + boxDimensions[0]/2 + radius, # Droite du cercle
                            coordinateNW[1] + boxDimensions[1]/2 * nb_caseY) # Haut du cercle
        border_position2 = (coordinateNW[0] + boxDimensions[0] * nb_caseX + boxDimensions[0]/2 - radius, # Gauche du cercle
                            coordinateNW[1] + boxDimensions[1]/2 * nb_caseY + 2*radius) # Bas du cercle
        if (border_position1[1] < ord < border_position2[1]) and (border_position1[0] > abs > border_position2[0]):
            return [nb_caseX, nb_caseY]
    # Pour la "Droite" et le "Bas" on ajoute + 1 car on veut que les compteurs aient comme valeur NB_CASE + 1 (Pour la 1er cran) et NB_CASE + 2 (Pour le 2ème cran)
    if direction == "Droite":
        nb_caseX += 1
        if abs > coordinateNW[0] + boxDimensions[0] * NB_CASE + boxDimensions[0]/2 * 2 - 2*radius: # Si on touche la 2ème case
            nb_caseX = nb_caseX + 1
        border_position1 = (coordinateNW[0] + boxDimensions[0] * NB_CASE + boxDimensions[0]/2 * (nb_caseX - NB_CASE), # Droite du cercle
                            coordinateNW[1] + boxDimensions[1] * nb_caseY + boxDimensions[1]/2 - radius) # Haut du cercle
        border_position2 = (coordinateNW[0] + boxDimensions[0] * NB_CASE + boxDimensions[0]/2 * (nb_caseX - NB_CASE) - 2*radius, # Gauche du cercle
                            coordinateNW[1] + boxDimensions[1] * nb_caseY + boxDimensions[1]/2 + radius) # Bas du cercle
        if (border_position1[1] < ord < border_position2[1]) and (border_position1[0] > abs > border_position2[0]):
            return [nb_caseX, nb_caseY]

    elif direction == "Bas":
        nb_caseY += 1
        if ord > coordinateNW[1] + boxDimensions[1] * NB_CASE + boxDimensions[1]/2 * 2 - 2*radius: # Si on touche la 2ème case
            nb_caseY = nb_caseY + 1
        border_position1 = (coordinateNW[0] + boxDimensions[0] * nb_caseX + boxDimensions[0]/2 + radius, # Droite du cercle
                            coordinateNW[1] + boxDimensions[1] * NB_CASE + boxDimensions[1]/2 * (nb_caseY - NB_CASE) - 2*radius) # Haut du cercle
        border_position2 = (coordinateNW[0] + boxDimensions[0] * nb_caseX + boxDimensions[0]/2 - radius, # Gauche du cercle
                            coordinateNW[1] + boxDimensions[1] * NB_CASE + boxDimensions[1]/2 * (nb_caseY - NB_CASE)) # Bas du cercle
        if (border_position1[1] < ord < border_position2[1]) and (border_position1[0] > abs > border_position2[0]):
            return [nb_caseX, nb_caseY]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
