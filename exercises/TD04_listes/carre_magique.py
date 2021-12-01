def afficheCarre(carre):
    for ligne in carre:
        for case in ligne:
            print (case, end="\t")
        print()

def testLignesEgales(carre):
    cste = 0
    somme_ligne = 0
    for ligne in carre:
        somme_ligne += case

    if carre.index(ligne)!= 0 and somme_ligne != cste:
        return -1
    elif carre.index(ligne) == 0:
        cste = somme_ligne

    return cste
