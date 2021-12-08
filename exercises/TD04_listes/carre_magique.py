carree_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [i.copy() for i in carree_mag]
carre_pas_mag [3][2] = 7

def afficheCarre(carre):
    for ligne in carre:
        for case in ligne:
            print (case, end="\t")
        print()

carree_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], 516, 2, 3, 13]
print (carree_mag[0])
print (carree_mag[1])
print (carree_mag[2])
print (carree_mag[3])
print (carree_mag[0][1])

carre_pas_mag = [i.copy() for i in carree_mag]
carre_pas_mag [3][2] = 7
print ("Carre M", carre_pas_mag)
print ("Carre P", carre_pas_mag)

afficheCarre        

def testLignesEgales(carre):
    cste = 0
    somme_ligne = 0
    case = 0
    for ligne in carre:
        somme_ligne += case

    if carre.index(ligne)!= 0 and somme_ligne != cste:
        return -1
    elif carre.index(ligne) == 0:
        cste = somme_ligne

    return cste
