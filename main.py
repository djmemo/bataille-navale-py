"""
Jeux de la bataille navale
"""
import re


def a1_to_coor(cell):
    """converti le format A1 en coordonée"""
    temp = re.compile(r"(\w+?)(\d+)")
    res = temp.match(cell).groups()
    letter = 0
    for index_letter in range(len(res[0])):
        letter_to_num = ord(res[0][index_letter].upper()) - 64
        letter += letter_to_num * (26 ** (len(res[0]) - index_letter - 1))
    return (letter - 1, int(res[1]) - 1)


def init_grille(ligne, colonne):
    """innitialisation de la grille de jeu"""
    row = []
    for i in range(ligne):
        column = []
        for j in range(colonne):
            # column.append(f"{i} {j}")
            column.append(f"~~")
        row.append(column)
    return row


def placer_bateau(grille, longueur_bateau, sens, debut):
    """Placement d'un bateau dans la grille"""
    coor_debut = a1_to_coor(debut)

    if (longueur_bateau + coor_debut[1]) > len(grille) and sens == "Horizontal":
        print("Le bateau est trop grand pour rentré sur la colonne")
        return grille

    if (longueur_bateau + coor_debut[0]) > len(grille[0]) and sens == "Vertical":
        print("Le bateau est trop grand pour rentré sur la ligne")
        return grille

    if sens == "Vertical":
        for index_longeur in range(longueur_bateau):
            if grille[index_longeur + coor_debut[1]][coor_debut[0]] != "~~":
                print("un bateau est déjà sur cette colonne")
                return grille
        for index_longeur in range(longueur_bateau):
            grille[index_longeur + coor_debut[1]][coor_debut[0]] = f"B{index_longeur+1}"

    if sens == "Horizontal":
        for index_longeur in range(longueur_bateau):
            if grille[coor_debut[1]][index_longeur + coor_debut[0]] != "~~":
                print("un bateau est déjà sur cette ligne")
                return grille
        for index_longeur in range(longueur_bateau):
            grille[coor_debut[1]][index_longeur + coor_debut[0]] = f"B{index_longeur+1}"

    return grille


def afficher_grille(grille):
    """affiche la grille"""
    aff_grille = "\\  "

    for colonne in enumerate(grille[0]):
        num_colonne = colonne[0]
        aff = ""
        if colonne[0] >= 26:
            aff += chr(ord("A") + int(num_colonne / 26) - 1)
            num_colonne = num_colonne % 26
        aff += chr(ord("A") + num_colonne)
        if len(aff) == 1:
            aff += " "
        aff_grille += f"{aff} "
    aff_grille += "\n"

    for ligne in enumerate(grille):
        aff_grille += f"{ligne[0]+1} "
        if len(f"{ligne[0]+1}") == 1:
            aff_grille += " "
        for colonne in enumerate(ligne[1]):
            aff_grille += f"{colonne[1]} "

        aff_grille += "\n"
    return aff_grille


maGrille = init_grille(10, 10)

maGrilleremplie = placer_bateau(maGrille, 4, "Vertical", "B2")
maGrilleremplie = placer_bateau(maGrille, 1, "Vertical", "D2")
maGrilleremplie = placer_bateau(maGrille, 3, "Horizontal", "F8")

print(afficher_grille(maGrilleremplie))
