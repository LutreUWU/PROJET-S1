from random import choice

def creation_tirette(NB_CASE:int):
    """
    Fonction qui créer les tirettes, 
    fonction qui créer la matrix des tirette
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
    >>> foo(7)
    (True, True)
    >>> foo(10)
    (True, True)
    >>> foo(50)
    (True, True)
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
            # Pour finir le jeu on doit avoir un trou toutes les 2 cases max
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

def optimisation_tirette(ligne, booleen_tirette, i):
    optimisation_trou_hori = False
    for j in range(1, 3):
        if ligne[i - j] == True:
            optimisation_trou_hori = True
    if not optimisation_trou_hori:
        ligne.append(True)
    else:
        ligne.append(booleen_tirette)
    return ligne

def click_opposer(save_click:list, prochain_click:list):
    """
    fonction qui verifier si le joueur n'a pas click sur le coté opposer
    et renvoi True si c'est le cas sinon False
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
