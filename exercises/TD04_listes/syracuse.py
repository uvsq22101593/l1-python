#En partant d'un entier `n` de départ, on définit une suite d'entiers en obtenant chaque nouveau terme à partir du précédent
#soit en le divisant par 2 s'il est pair, soit en le multipliant par 3 et en ajoutant 1 s'il est impair. 
#Ecrire la fonction qui, à partir d'un entier initial, renvoie la liste des valeurs successives jusqu'à ce que la valeur `1` soit atteinte 

#pour exécuter aller dans l1-python ->cd exercises ->cd TD04_listes puis faire python syracuse.py puis ENTREE

""" Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """

def syracuse(n):
    liste =[]
    while n != 1:
        if n % 2 == 0 :
            n = int(n/2)
        else :
            n = (n*3)+1
        liste.append(n)    
    return (liste)
print (syracuse(1000))

""" Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """

def testeConjecture(n_max):
    for n in range (2, n_max):
        liste = syracuse(n)
    return True
        
print (f'Syracuse : {syracuse(1000)}')
print (f'Conjecture : {testeConjecture(1000)}')

""" Retourne le temps de vol de n """

def tempsVol(n):
    return len(syracuse(n))-1
print("Le temps de vol de", 1000, "est", tempsVol(1000))

""" Retourne la liste de tous les temps de vol de 1 à n_max """

def tempsVolListe(n_max):
    liste = []
    for n in range (1, n_max):
        liste.append(tempsVol(n))
    return liste

print (f'Syracuse : {syracuse (1000)}')

def tempsVolmax(n_max):
    max =(0, 0)
    for n in range (1, n_max):
        temps = tempsVol(n)
        if max [1] < temps :
         max = (n, temps)

    return max

def Altitude(n):
    altitudes= syracuse(n)
    altitudes.remove(n)
    altitudes.sort(reverse=True)
    return altitudes[0]

def AltitudeMax(n_max):
    max = (0, 0)
    for n in range (2, n_max):
        altitude = Altitude(n)
        if max [1] < altitude :
            max = (n, altitude)
    return max
print (max)