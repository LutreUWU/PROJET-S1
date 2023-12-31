from random import choice

def creation_tirette(NB_CASE:int):
    """
    Fonction qui va créer la liste des tirettes horizontale et verticale avec des valeurs booléennes, 
    elle va aussi optimiser la tirette afin qu'on puisse toujours terminer le jeu
    
    Paramètres:
        NB_CASE : Nombre de case 
        
    Return:
        La liste des tirettes horizontales et verticales 
     
    >>> def foo(NB_CASE):
    ...     x = False
    ...     tirette_h, tirette_v = creation_tirette(NB_CASE)
    ...     for a in tirette_h:
    ...         for i in range(2, len(a)):
    ...             if not a[i]:
    ...                 for j in range(1, 2):
    ...                     if a[i - j]:
    ...                         x = True
    ...     y = False
    ...     for ligne in range(NB_CASE):
    ...         for colonne in range(NB_CASE + 2):
    ...             if not tirette_v[colonne][ligne]:
    ...                 for j in range(1, 2):
    ...                     if tirette_v[colonne - j][ligne]:
    ...                         y = True
    ...     return (x, y)
    ...
    
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
    
    Paramètres:
        tirette_h: La liste de True et de False pour les tirettes horizontales
        tirette_v: La liste de True et de False pour les tirettes verticales

    Returns:
        allCompteurX: Liste de dictionnaire avec le compteur gauche et droite de chaque tirette horizontale (1 de chaque côté par défault)
        allCompteurY: Liste de dictionnaire avec le compteur haut et bas de chaque tirette verticale (1 de chaque côté par défault)

    >>> create_CompteurTirette([True, True], [True, False])
    ([{'gauche': 1, 'droite': 1}, {'gauche': 1, 'droite': 1}], [{'haut': 1, 'bas': 1}, {'haut': 1, 'bas': 1}])
    """
    
    allCompteurX, allCompteurY = [], []
    for elem in tirette_h:
        compteur = {"gauche": 2, "droite": 0}
        allCompteurX.append(compteur)
    for elem in tirette_v:
        compteur = {"haut": 2, "bas": 0}
        allCompteurY.append(compteur)
    return allCompteurX, allCompteurY
    
def click_opposer(save_click:list, prochain_click:list):
    """
    Fonction qui verifie si le joueur n'a pas cliqué sur le côté opposer
    et renvoie True si c'est le cas sinon False
    
    Paramètres:
        save_click: 
    >>> click_opposer([1, 2], ["gauche", 2])
    False
    >>> click_opposer([1, 2], ["droite", 3])
    False
    >>> click_opposer([1, 2], ["droite", 1])
    False
    >>> click_opposer([1, 2], ["droite", 2])
    True
    """
    if prochain_click[0] == "gauche":
        click, prochain_click[0] = 1, 1
    elif prochain_click[0] == "droite":
        click, prochain_click[0] = -1, -1
    elif prochain_click[0] == "haut":
        click, prochain_click[0] = 2, 2
    elif prochain_click[0] == "bas":
        click, prochain_click[0] = -2, -2
    else:
        click = save_click[0]
    if click == -save_click[0] and prochain_click[1] == save_click[1]:
        return True
    for a in range(len(save_click)):
        save_click[a] = prochain_click[a]
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()