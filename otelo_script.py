# le joueur blanc commence
color = "blanc"

# grille de jeu
grille = [["     ", "     ", "     ", "     ", "     ", "     ", "     ", "     "],
          ["     ", "     ", "     ", "     ", "     ", "     ", "     ", "     "],
          ["     ", "     ", "     ", "     ", "     ", "     ", "     ", "     "],
          ["     ", "     ", "     ", "noir ", "blanc", "     ", "     ", "     "],
          ["     ", "     ", "     ", "blanc", "noir ", "     ", "     ", "     "],
          ["     ", "     ", "     ", "     ", "     ", "     ", "     ", "     "],
          ["     ", "     ", "     ", "     ", "     ", "     ", "     ", "     "],
          ["     ", "     ", "     ", "     ", "     ", "     ", "     ", "     "]]

# direction des different teste a effectuer
direction = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]


# definition des variable
def changement_joueur(couleur):
    """
    fonction permettant le changement de joueur a la fin du tour

    :param couleur: str

    :return: une couleur (joueur)
    """
    if couleur == "blanc":
        return "noir "
    elif couleur == "noir ":
        return "blanc"


def affichage_grille():
    """
    fonction permettant l'affichage de la grille

    :return: aucun retour
        effet de bord : affiche la grille de jeu

    """
    print("      0        1        2        3        4        5        6        7")
    for k in range(8):
        print(k, grille[k])
        print()


def demande_case():
    """
    fonction permettant de recuperer une case

    :return: -la colonne: int
             -la ligne: int
             -la case (colonne, ligne): tuple

    """
    demande_colonne = int(input("Numero de la colonne "))
    demande_ligne = int(input("Numero de la ligne "))

    while demande_colonne >= 8 or demande_ligne >= 8:
        print("La case saisie doit etre dans la grille (n° compris en 0 et 7)")
        demande_colonne = int(input("Numero de la colonne "))
        demande_ligne = int(input("Numero de la ligne "))

    return demande_colonne, demande_ligne, (
        demande_colonne, demande_ligne)  # cree une variable case qui comptient le n° de ligne et le n° de colonne


def verifie_case(blanc, noir, vide):
    """
    fonction permettant de verifier que la case saisie est vide

    :param: blanc: int
    :param: noir: int
    :param: vide: int

    :return: -la colonne: int
             -la ligne: int
             -la case (colonne, ligne): tuple

    """
    print("""case vide : {}
blanc : {}
noir : {}""".format(vide, blanc, noir))
    print("Au joueur {} de jouer".format(color.upper()))
    affichage_grille()

    demande_colonne, demande_ligne, case = demande_case()  # cree une variable case qui comptient le n° de ligne et
    # le n° de colonne

    # Tant que la case n'est pas vide on en demande une autre
    while not case_vide(case):
        print("La case saisie doit etre vide")
        demande_colonne, demande_ligne, case = demande_case()
    return case, demande_ligne, demande_colonne


def case_vide(case):
    """
    fonction verifiant qu'un case donne est vide

    :param case: tuple

    :return: bool
    """
    colonne, ligne = case
    return grille[ligne][colonne] == "     "


def meme_couleur(case, couleur):
    """
    fonction permetant de verifier qu'une case donne est de la meme couleur que couleur

    :param case: tuple
    :param couleur: str

    :return: bool
    """

    colonne, ligne = case
    return grille[ligne][colonne] == couleur


def couleur_inverse(case, couleur):
    """
    fonction permettant de verifier qu'une case donne est de la couleur inverse de couleur

    :param case: tuple
    :param couleur: str

    :return: bool ou None
    """
    if couleur == "noir ":
        new_couleur = "blanc"
    elif couleur == "blanc":
        new_couleur = "noir "
    else:
        return None
    column, lines = case
    return grille[lines][column] == new_couleur


def augmente_case(case, direction, grille):
    """
    fonction permettant de se deplacer dans la grille dans une direction donnee a partir d'une case

    :param case: tuple
    :param direction: tuple
    :param grille: list

    :return: une case ou None
    """
    print("augmente_case")
    colonne, ligne = case
    x, y = direction
    colonne += x
    ligne += y
    print(x, y)
    try:
        a = grille[ligne][colonne]
        print(a)
        return colonne, ligne
    except IndexError:
        return None


def teste(grile, couleur, direction, case):
    """
    fonction permetant de teste si l'on peut poser sont pion par rapport au autre pion

    :param grile: list
    :param couleur: str
    :param direction: tuple
    :param case: tuple

    :return: - False et tuple (pour eviter les erreur)
             - True et (case + direction)
    """
    print("\n\n")
    new_case = augmente_case(case, direction, grile)
    print("teste")
    if new_case is None:
        print("sortie de grille")
        return False, (8, 8, 8, 8)
    else:
        # si la case a cote est un pion de couleur inverse
        if couleur_inverse(new_case, couleur):
            new_case = augmente_case(new_case, direction, grille)
            print("avant d'entrer")
            # tant qu'il n'y a pas de pion de meme couleur on continue de chercher plus loin
            while couleur_inverse(new_case, couleur):
                print("boucle de couleur inverse")
                new_case = augmente_case(new_case, direction, grille)
            print("sortie")
            if meme_couleur(new_case, couleur):
                print("poser")
                return True, (new_case + direction)
            else:
                print("pas de pion de la meme couleur")
                return False, (8, 8, 8, 8)
        else:
            print("pas possible de le poser")
            return False, (8, 8, 8, 8)


def retourne(grille, liste_case, case_depart, couleur):
    """
    fonction pour retourner les pions

    :param grille: list
    :param liste_case: list
    :param case_depart: tuple
    :param couleur: str

    :return: aucun retour
        effet de bord: modifier la grille de jeu
    """
    print("\nretourne les pions \n\n")
    for ensemble in liste_case:
        case = case_depart
        print("case = ", case)
        print("##################################################################")
        case_fin = (ensemble[0], ensemble[1])
        print("case_fin = ", case_fin)
        dir = (ensemble[2], ensemble[3])
        print("dir = ", dir)
        while case != case_fin:
            print("boucle")
            try:
                grille[case[1]][case[0]] = couleur
            except TypeError:
                print("erreur")
            print("----------------------------------\n", case)
            case = augmente_case(case=case, direction=dir, grille=grille)
            print("case = ", case)
        print("sortie de la boucle")


def compte_point(grille):
    """
    fonction pour compter les point est les case vide

    :param grille: list

    :return: le nombre de case vide, le nombre de pion blanc et le nombre de pion noir
    """
    blanc = 0
    noir = 0
    vide = 0
    for liste in grille:
        for elem in liste:
            if elem == "blanc":
                blanc += 1
            if elem == "noir ":
                noir += 1
            if elem == "     ":
                vide += 1
    return blanc, noir, vide


vide = 1
while vide != 0:
    blanc, noir, vide = compte_point(grille=grille)
    case, ligne, colonne = verifie_case(blanc, noir, vide)

    poser = False  # variable permetant de savoir si l'on peut jouer a cette endroit ou pas
    liste_case_fin = []  # variable stockant des case et de direction a retourner

    # boucle faisant les testes dans les 8 sens
    for nb_teste in range(8):
        resultat = teste(grile=grille, couleur=color, direction=direction[nb_teste], case=case)
        print(resultat)
        Poser = resultat[0]
        case_fin = resultat[1]
        if Poser:
            poser = True
            liste_case_fin.append(case_fin)

    if poser:
        grille[ligne][colonne] = color
        retourne(grille=grille, liste_case=liste_case_fin, case_depart=case, couleur=color)

        # a la fin du tour on change de joueur
        color = changement_joueur(color)
