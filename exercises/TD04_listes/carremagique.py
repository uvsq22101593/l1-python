def afficheCarre(carre):
    for ligne in carre:
        for case in ligne:
            print (case, end="\t")
        print()

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]

print (carre_mag[0])
print (carre_mag[1])
print (carre_mag[2])
print (carre_mag[3])
print (carre_mag[0][1]) # 2e élément de la 1ere ligne

carre_pas_mag = [i.copy() for i in carre_mag]

carre_pas_mag [3][2] = 7
print ("Carre M", carre_mag)
print ("Carre P", carre_pas_mag)

def testLignesEgales(carre):
    cste = 0
    for ligne in carre :
        somme_ligne = 0
        for case in ligne :
            somme_ligne += case

        if carre.index(ligne)!= 0 and somme_ligne != cste :
            return -1
        elif carre.index(ligne) == 0 :
            cste = somme_ligne

    return cste

print ("Carre M : cste ligne", testLignesEgales (carre_mag))
print ("Carre P : cste ligne", testLignesEgales (carre_pas_mag))

def testColonnesEgales(carre):
    sommes = [i for i in carre [0]]
    for ligne in carre [1:]: #1 jusqu'à la fin
        for j in range (len(ligne)):
            sommes[j] += ligne [j]

    cste = sommes [0]
    for s in sommes [1:]:
        if s != cste :
            return -1

    return cste
print ("Carre M : cste colonne", testColonnesEgales (carre_mag))
print ("Carre P : cste colonne", testColonnesEgales (carre_pas_mag))

#CORRECTION

def testDiagonalesEgales(carre):
    taille = len(carre[0])

    cste =0
    for i in range(taille):
        cste += carre [i][i]

    somme = 0
    for i in range (taille, 0, -1):
        somme += carre [i-1][i-1]

    if somme != cste :
        return -1
    return cste

print ("Carre M : cste diagonale", testDiagonalesEgales (carre_mag))
print ("Carre P : cste diagonale", testDiagonalesEgales (carre_pas_mag))

def estCarreMagique(carre):
    cste= testLignesEgales(carre)
    if cste == -1 :
        return False

    if cste != testColonnesEgales(carre):
        return False

    if cste != testDiagonalesEgales (carre):
        return False
        
    return True
print ("Carre M : est magique ?", estCarreMagique (carre_mag))
print ("Carre P : est magique ?", estCarreMagique (carre_pas_mag))

def estNormal(carre):
    all = []
    for ligne in carre :
        for elem in ligne :
            if all.count(elem) > 0:
                return False
            all.append (elem)
    all.sort(reverse= True)

    taille = len(carre)
    if all[0] != pow(taille, 2):
        return False
    return True

print ("Carre Normal:", estNormal(carre_mag))
print ("Carre pas Normal:", estNormal(carre_pas_mag))