"""CODE FAIT PAR DAVID, ABDELKADER ET WALID."""

from random import choice

def creation_tirette(NB_CASE:int):
    """
    Fonction qui va créer la liste des tirettes horizontale et verticale avec des valeurs booléennes, 
    elle va aussi appeler la fonction pour optimiser la tirette afin qu'on puisse toujours terminer le jeu.
    
    Paramètres:
        NB_CASE : Nombre de case 
    Return:
        all_tirette_h : Liste où chaque élément est une liste d'élément booléenne, True = Y a un trou, False = Y a une tirette horizontale
        all_tirette_v : Liste où chaque élément est une liste d'élément booléenne, True = Y a un trou, False = Y a une tirette verticale 
    
    Doctest compliqués à faire car les valeurs sont aléatoires, mais on aura toujours maximum 2 False de suite dans une tirette.
    Ex : [False, False, True, False, False, True, False, True, False]
    Il peut y avoir que des True.
    Ex : [True, False, True, True, True, True, True, True, False]
    >>>
    """
    all_tirette_h, all_tirette_v = [], []
    max_push = 2 # Car on peut tirer 2 fois d'un côté max 
    for _ in range(NB_CASE):
        ligne_h, ligne_v = [], []
        # Les 2 premières valeurs de chaque tirette sont aléatoires
        for _ in range(2):
            ligne_h.append(choice([True, False]))
            ligne_v.append(choice([True, False]))
        # Pour le reste des tirettes, on prend aléatoirement une valeur booléenne
        for i in range(2, NB_CASE + max_push): # On commence à 2 car on a déja 2 valeurs
            # On choisis aléatoirement 
            choix_h = choice([True, False])
            choix_v = choice([True, False])
            # Pour finir le jeu on doit avoir au moins un trou toutes les 2 cases max
            # Si on a choisit Faux, alors on doit s'assurer qu'il y a au moins un trou dans les 2 cases d'avant
            if not choix_h:
                optimisation_tirette(ligne_h, choix_h, i)
            # Si on a choisit True, alors on a pas de problème 
            else:
                ligne_h.append(choix_h)
            # Pareil pour les tirettes verticales    
            if not choix_v:
                optimisation_tirette(ligne_v, choix_v, i)
            else:
                ligne_v.append(choix_v)
        # On pousse la tirette dans la liste
        all_tirette_h.append(ligne_h)
        all_tirette_v.append(ligne_v)    
    return all_tirette_h, all_tirette_v

def optimisation_tirette(tirette:list, booleen_tirette:bool, i:int):
    """
    Fonction qui va optimiser l'emplacement des trous dans chaque tirette afin
    que le jeu soit toujours terminable.
    Le but est de vérifier l'état des 2 cases derrière l'origine et si elles n'ont pas de trous alors
    on va obligatoirement mettre un trou.

    Paramètres:
        tirette (_list_): La ligne de tirette qu'on veut sélectionner 
        booleen_tirette (_bool_): La valeur booléene de la case avant l'optimisation
        i (_int_): Indice de la case dans la tirette

    Returns:
        La valeur booléene de la case après l'optimisation  
    >>> optimisation_tirette([False, False], False, 2)
    [False, False, True]
    >>> optimisation_tirette([False, False, True], False, 3)
    [False, False, True, False]
    >>> optimisation_tirette([True, False, False], False, 3)
    [True, False, False, True]
    """
    # Permet de déterminer si on doit activer l'optimisation ou pas 
    activate_optimisation_trou = False 
    # On va regarder les 2 cases derrières celle qu'on veut optimiser
    if tirette[i - 1] == False: 
        if tirette[i - 2] == False:
            activate_optimisation_trou = True
    # S'il n'y a pas de trou alors on va activer l'optimisation et on va obligatoirement mettre un True
    if activate_optimisation_trou:
        tirette.append(True)
    else:
        # Sinon on apprend la valeur booléene de base 
        tirette.append(booleen_tirette)
    return tirette

def create_CompteurTirette(tirette_h:list, tirette_v:list):
    """
    Fonction qui permet d'associer à chaque tirette un compteur, 
    pour savoir combien de fois on peut tirer à gauche, à droite, en haut, en bas.
    (Par défault elles sont de 2 à gauche et 2 en haut)
    
    Paramètres:
        tirette_h: La liste de True et de False pour les tirettes horizontales
        tirette_v: La liste de True et de False pour les tirettes verticales

    Returns:
        allCompteurX: Liste de dictionnaire avec le compteur gauche et droite de chaque tirette horizontale (1 de chaque côté par défault)
        allCompteurY: Liste de dictionnaire avec le compteur haut et bas de chaque tirette verticale (1 de chaque côté par défault)

    >>> create_CompteurTirette([True, True], [True, False])
    ([{'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}], [{'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}])
    """
    
    allCompteurX, allCompteurY = [], []
    for elem in tirette_h:
        compteur = {"gauche": 2, "droite": 0}
        allCompteurX.append(compteur)
    for elem in tirette_v:
        compteur = {"haut": 2, "bas": 0}
        allCompteurY.append(compteur)
    return allCompteurX, allCompteurY
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
def working_compteurTirette(click_tirette:list, compteur_tiretteh:list, compteur_tirettev:list, NB_CASE:int,
                            playerTurn: int, forbidden_click: list):
    """
    Fonction qui va modifier le compteur de la tirette où on a cliqué en fonction de l'endroit qu'on a cliqué
    Args:
        click_tirette (_list_): LISTE qui contient l'indice [x, y] du compteur qu'on a cliqué 
        compteur_tiretteh (_list_): Liste de dictionnaire avec le compteur gauche et droite de chaque tirette horizontale (1 de chaque côté par défault)
        compteur_tirettev (_list_): Liste de dictionnaire avec le compteur haut et bas de chaque tirette verticale (1 de chaque côté par défault)
        NB_CASE (_int_): Nombre de cases
        playerTurn (_int_): Int qui réprésente l'index du joueur qui joue dans la "playerlist"
        forbidden_click (_list_): LISTE qui contient l'indice [x, y] du compteur dont on ne peut pas cliqué car c'est son opposé

    Returns:
        forbidden_click : LISTE qui contient l'indice [x, y] du compteur dont on ne peut pas cliqué car c'est son opposé
        playerTurn: Int Int qui réprésente l'index du joueur suivant qui joue dans la "playerlist" après qu'on ai déplacé les tirettes
    >>> working_compteurTirette([8, 0], [{'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}], [{'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}], 7, 0, None)
    ([-1, 0], 1)
    >>> working_compteurTirette([-1, 0], [{'gauche': 1, 'droite': 1}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}, {'gauche': 2, 'droite': 0}], [{'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}, {'haut': 2, 'bas': 0}], 7, 1, None)
    ([8, 0], 2)
    """
    # On regarde d'abord si on a pas cliqué sur le compteur interdit
    if click_tirette == forbidden_click:
        return forbidden_click, playerTurn
    # Si on a cliqué sur un compteur, click_tirette renvoie une liste, donc on vérifie
    if type(click_tirette) == list:
        # Puis on vérifie qu'on a bien cliqué sur une tirette qu'on peut tirer
            # On regarde à gauche
            if click_tirette[0] < 0: 
                if click_tirette[0] == -1 and compteur_tiretteh[click_tirette[1]]["gauche"] < 2 : # Il faut que la tirette de gauche soit à 1 cran ou 0 pour pouvoir la tirer
                    # Si c'est le cas alors on peut modifier la tirette et passer au tour du joueur suivant
                    compteur_tiretteh[click_tirette[1]]["gauche"] += 1
                    compteur_tiretteh[click_tirette[1]]["droite"] -= 1
                    forbidden_click = [abs(click_tirette[0] - NB_CASE), click_tirette[1]] # On modifie la case interdite
                    playerTurn += 1
                    return forbidden_click, playerTurn
            # On regarde à droite
            elif click_tirette[0] > NB_CASE:
                if click_tirette[0] == NB_CASE + 1 and compteur_tiretteh[click_tirette[1]]["droite"] < 2 : # Il faut que la tirette de droite soit à 1 cran ou 0 pour pouvoir la tirer
                    compteur_tiretteh[click_tirette[1]]["gauche"] -= 1
                    compteur_tiretteh[click_tirette[1]]["droite"] += 1
                    forbidden_click = [-(click_tirette[0] - NB_CASE), click_tirette[1]]
                    playerTurn += 1
                    return forbidden_click, playerTurn
            # On regarde en haut
            elif click_tirette[1] < 0:
                if click_tirette[1] == -1 and compteur_tirettev[click_tirette[0]]["haut"] < 2 : # Il faut que la tirette de haut soit à 1 cran ou 0 pour pouvoir la tirer
                    compteur_tirettev[click_tirette[0]]["haut"] += 1
                    compteur_tirettev[click_tirette[0]]["bas"] -= 1
                    forbidden_click = [click_tirette[0], abs(click_tirette[1] - NB_CASE)]
                    playerTurn += 1
                    return forbidden_click, playerTurn
            # On regarde en bas
            elif click_tirette[1] > NB_CASE:
                if click_tirette[1] == NB_CASE + 1 and compteur_tirettev[click_tirette[0]]["bas"] < 2 : # Il faut que la tirette de bas soit à 1 cran ou 0 pour pouvoir la tirer
                    compteur_tirettev[click_tirette[0]]["haut"] -= 1
                    compteur_tirettev[click_tirette[0]]["bas"] += 1
                    forbidden_click = [click_tirette[0], -(click_tirette[1] - NB_CASE)]
                    playerTurn += 1
                    return forbidden_click, playerTurn
    return forbidden_click, playerTurn

if __name__ == "__main__":
    import doctest
    doctest.testmod()