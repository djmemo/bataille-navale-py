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


def initgrille(ligne, colonne):
    """innitialisation de la grille de jeu"""
    row = []
    for i in range(ligne):
        column = []
        for j in range(colonne):
            column.append(f"{i} {j}")
        row.append(column)
    return row


def remplirbateau(grille, longueur_bateau, sens, debut):
    """Placement d'un bateau dans la grille"""
    coor_debut = a1_to_coor(debut)

    if (longueur_bateau + coor_debut[1]) > len(grille) and sens == "Vertical":
        print("Le bateau est trop grand pour rentré sur la colonne")
        return grille

    if (longueur_bateau + coor_debut[0]) > len(grille[0]) and sens == "Horizontal":
        print("Le bateau est trop grand pour rentré sur la ligne")
        return grille

    if sens == "Vertical":
        for index_longeur in range(longueur_bateau):
            grille[index_longeur + coor_debut[0]][coor_debut[1]] = f"B{index_longeur+1}"

    if sens == "Horizontal":
        for index_longeur in range(longueur_bateau):
            grille[coor_debut[0]][index_longeur + coor_debut[1]] = f"B{index_longeur+1}"

    return grille


maGrille = initgrille(5, 3)
# print(ma_grille)

maGrilleremplie = remplirbateau(maGrille, 4, "Vertical", "B2")
print(maGrilleremplie)
