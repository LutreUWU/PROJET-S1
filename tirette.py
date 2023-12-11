import Modules.fltk as fltk

fltk.cree_fenetre(800,800)
#Pour les tirettes horizontales
fltk.image(500, 500, "Tirette.png", largeur=200, hauteur=100, ancrage="center")
fltk.image(500, 100, "Tirette.png", largeur=150, hauteur=100, ancrage="center")
#Pour les tirettes verticales
fltk.image(100, 200, "Tirette.png", largeur=200, hauteur=100, ancrage="center")
fltk.image(100, 500, "Tirette.png", largeur=150, hauteur=100, ancrage="center")

fltk.attend_ev()
fltk.ferme_fenetre