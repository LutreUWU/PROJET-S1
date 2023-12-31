def player_setup(joueur:list, NB_JOUEUR:int, player_number:int, ball_case:tuple):
    color = ["green", "red", "black", "blue", "yellow", "purple"]
    if player_number < NB_JOUEUR:
        joueur_dic =  {}
        joueur_dic[f"Joueur {player_number}"] = 1
        joueur_dic["Color"] = color[player_number]
        joueur.append(joueur_dic)
    else:
        joueur[player_number%NB_JOUEUR][f"Joueur {player_number%NB_JOUEUR}"] += 1
    return joueur[player_number%NB_JOUEUR]["Color"]