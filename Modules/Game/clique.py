def detect_click(abs:int, ord:int, NB_CASE:int, margin:tuple, boxDimensions:tuple, coordinateNW:tuple):
    """
    Fonction qui va permettre de détecter si on clique sur une case ou non, si c'est le cas,
    elle va renvoyer l'indice de la case.
    
    Le problème majeur était de vérifier qu'on ne clique pas entre les cases.
    La solution est de vérifier 1 par 1 chaque case en les parcourants chacune   
    
    Paramètres:
        abs: Coordonnée X de la souris
        ord: Coordonnée Y de la souris
        margin: Un tuple avec les marge (x,y) entre les cases
        boxDimensions: Un tuple avec les dimensions (x,y) d'une case
        coordinateNW : Coordonnées (x,y) de la fenêtre qu'on a crée (pour faire la marge avec la fenêtre windows) 
    Returns:
        Les indices X et Y, de la cases 
    
    >>> detect_click_case(20, 20, 7, (5, 5), (50, 50), (10, 10))
    (0, 0)
    """
    # On cherche comme si il n'y avait pas de marge entre les cases 
    # On va soustraite l'abscisse par le point d'origine, puis son va diviser par la taille d'une case, pour connaître c'est quelle cases qu'on clique
    nb_case_x = int((abs - coordinateNW[0]) // boxDimensions[0])
    nb_case_y = int((ord - coordinateNW[1]) // boxDimensions[1])
    # Variable pour vérifier si on a cliqué entre les cases ou pas 
    positionX, positionY = coordinateNW[0], coordinateNW[1] # Origine des points
    if nb_case_x < 0 or nb_case_y < 0: # Si on clique à gauche ou en haut de la grille
        if nb_case_x < 0 and 0 <= nb_case_y < NB_CASE:
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Gauche")
        elif nb_case_y < 0 and NB_CASE > nb_case_x >= 0:
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Haut")
    if nb_case_x >= NB_CASE or nb_case_y >= NB_CASE: # Si on clique à droite ou en bas de la grille
        if nb_case_x >= NB_CASE and 0 <= nb_case_y < NB_CASE:
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Droite")
        elif nb_case_y == NB_CASE and NB_CASE > nb_case_x >= 0 :
            return detect_click_compteur(abs, ord, nb_case_x, nb_case_y, coordinateNW, boxDimensions, NB_CASE, "Bas")
    
    checkX, checkY = False, False # Si les 2 sont True alors on n'a pas cliqué entre les cases
    # On commmence tout d'abord avec l'abscisse  
    for i in range(nb_case_x + 1 ): # +1 car si on commence à 0, comme la 1er case a pour indice 0, le for ne va pas s'activer.
        # A la première case on ajoute la marge 1 fois
        if i == 0: 
            left_positionX = positionX + margin[0]
        # Puis pour le reste on ajoute 2 fois la marge 
        else: 
            left_positionX = positionX + margin[0]*2
        # Puis on avance la position originale de la taille de la case
        positionX = left_positionX + (boxDimensions[0] - 2*margin[0])
        if left_positionX <= abs <= positionX: # Puis on vérifier si l'abs est entre les 2 points 
             checkX = True # Si c'est le cas alors on est sur une case X
             # A effacer en dessous, c'est pour mieux visualiser     
             "a l'intérieur X"
             """fltk.cercle(left_positionX, ord,
                         3, couleur="black")
             fltk.cercle(positionX, ord,
                         3, couleur="black")"""
    # Pareil pour l'ordonnée
    for i in range(nb_case_y + 1 ):
        if i == 0:
            left_positionY = positionY + margin[1]
        else:
            left_positionY = positionY + margin[1]*2
        positionY = left_positionY + (boxDimensions[1] - 2*margin[1])
        if left_positionY <= ord <= positionY: 
             checkY = True # Si c'est le cas alors on est sur une case Y
             # A effacer en dessous, c'est pour mieux visualiser          
             "a l'intérieur Y"
             """fltk.cercle(abs, left_positionY,
                         3, couleur="blue")
             fltk.cercle(abs, positionY,
                         3, couleur="blue")"""
    if checkX and checkY:
        return nb_case_x, nb_case_y
    else:
        return False
    
def detect_click_compteur(abs:int, ord:int, nb_caseX:int, nb_caseY:int, coordinateNW:tuple, boxDimensions:tuple, NB_CASE:int, direction:str):
    radius = boxDimensions[0]//5
    if direction == "Gauche":
        if coordinateNW[0] + boxDimensions[0]/2 * -2 + 2*radius > abs: # Si on touche la 2ème case
            nb_caseX = nb_caseX - 1
        border_position1 = (coordinateNW[0] + boxDimensions[0]/2 * nb_caseX + 2*radius, # Droite du cercle
                            coordinateNW[1] + boxDimensions[1] * nb_caseY + boxDimensions[1]/2 - radius) # Haut du cercle
        border_position2 = (coordinateNW[0] + boxDimensions[0]/2 * nb_caseX, # Gauche du cercle
                            coordinateNW[1] + boxDimensions[1]*nb_caseY + boxDimensions[1]/2 + radius) # Bas du cercle

        if (border_position1[1] < ord < border_position2[1]) and (border_position1[0] > abs > border_position2[0]):
            return [nb_caseX, nb_caseY]
    elif direction == "Haut":
        if coordinateNW[1] + boxDimensions[1]/2 * -2 + 2*radius > ord: # Si on touche la 2ème case
            nb_caseY = nb_caseY - 1
        border_position1 = (coordinateNW[0] + boxDimensions[0] * nb_caseX + boxDimensions[0]/2 + radius, # Droite du cercle
                            coordinateNW[1] + boxDimensions[1]/2 * nb_caseY) # Haut du cercle
        border_position2 = (coordinateNW[0] + boxDimensions[0] * nb_caseX + boxDimensions[0]/2 - radius, # Gauche du cercle
                            coordinateNW[1] + boxDimensions[1]/2 * nb_caseY + 2*radius) # Bas du cercle
        if (border_position1[1] < ord < border_position2[1]) and (border_position1[0] > abs > border_position2[0]):
            return [nb_caseX, nb_caseY]
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
