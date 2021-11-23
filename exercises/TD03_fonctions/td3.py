def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[3]+60*temps[2]+60*60*temps[1] +temps[0]*(60*60*24)
    
temps = (3,23,1,34)
print(type(temps))
print( "Le temps en seconde est", (tempsEnSeconde(temps)))
   
"""Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
def secondeEnTemps(seconde):
    
    temps_jour = seconde // (24*60*60)
    seconde = seconde % (24*3600)

    temps_heure = seconde // 3600
    seconde = seconde % 3600

    temps_minute = seconde //60
    temps_seconde = seconde % 60
    return (int(temps_jour),int( temps_heure), int(temps_minute),int(temps_seconde))
    

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici

def afficheTemps(temps):
    str_temps= ""

    if temps[0] > 1:
        str_temps += f'{ (temps[0])}jours'
    elif temps[0]>0 :
        str_temps += f'{ (temps[0])}jour'
    if temps[0] > 0 and (temps[1]>0 or temps[2]>0 or temps[3]>0):
        str_temps +="."
    
    if temps[1] >1:
        str_temps += f'{ (temps[1])}heures'
    elif temps[1]>0 :
        str_temps += f'{ (temps[0])}heure'
    if temps[1] > 0 and ( temps[2]>0 or temps[3]>0):
        str_temps +="."

    if temps[2] >1:
        str_temps += f'{ (temps[2])}minutes'
    elif temps[2]>0 :
        str_temps += f'{ (temps[2])}minute'
    if temps[2] > 0 and temps[3]>0:
        str_temps += "."

    if temps[3] >1:
        str_temps += f'{ (temps[3])}secondes'
    elif temps[3]>0 :
        str_temps += f'{ (temps[3])}seconde'
    print(str_temps)

afficheTemps((1,0,14,23))

def demandeTemps():
   jour = int(input ("entrez un temps en jour, heures, minutes et secondes"))
   while jour < 0:
       jour = int(input("le nbr d'heures doit être compris entre 0 et 24"))
     
    heure = int(input("Entrez un nombre d'heures") 
    while heure < 0:


    minute =
   while minute <0 :
    seconde =
    seconde

afficheTemps(demandeTemps())


def sommeTemps(temps1,temps2):
    

def sommeTemps((2,3,4,25),(5,22,57,1))
    seconde_t1 = tempsEnSeconde (temps1)
    seconde_t2 = tempsEnSeconde (temps2)
    return secondeEnTemps (seconde_t1 + seconde_t2)


def proportionTemps(temps,proportion):
    seconde_t = tempsEnSeconde( temps)

    return secondeEnTemps( seconde_t * proportion)


afficheTemps(proportionTemps((2,0,36,0),0.2))

afficheTemps((1,0,14,23))

def proportionTemps(temps: list, proportion: int):
    return secondeEnTemps((tempsEnSeconde(temps) * (proportion / 100)))
# resultat = proportionTemps((2, 0, 36, 0), 0.2)
# afficheTemps(resultat)


def tempsEnDate(temps: list):
    annees = tempsEnSeconde(temps) // (60 * 60 * 24 * 365)
    temps = tempsEnSeconde(temps) % (60 * 60 * 24 * 365)
    jours = temps // (60 * 60 * 24)
    temps = temps % (60 * 60 * 24)
    heures = temps // (60 * 60)
    temps = temps % (60 * 60)
    minutes = temps // 60
    temps = temps % 60
    secondes = temps
    return (annees, jours, heures, minutes, secondes)


def secondeEnDate(secondes: int):
    return tempsEnDate(secondeEnTemps(secondes))


def afficheDate(date=secondeEnDate(time.time())):
    if date[0] != 0 and date[0] > 1:
        print(date[0], "années", end=" ")
    elif date[0] == 1:
        print(date[0], "année", end=" ")
    if date[1] != 0 and date[1] > 1:
        print(date[1], "jours", end=" ")
    elif date[1] == 1:
        print(date[1], "jour", end=" ")
    if date[2] != 0 and date[2] > 1:
        print(date[2], "heures", end=" ")
    elif date[2] == 1:
        print(date[2], "heure", end=" ")
    if date[3] != 0 and date[3] > 1:
        print(temps[3], "minutes", end=" ")
    elif date[3] == 1:
        print(date[3], "minute", end=" ")
    if date[4] != 0 and date[4] > 1:
        print(date[4], "secondes", end=" ")
    elif date[4] == 1:
        print(date[4], "seconde", end=" ")


# temps = secondeEnTemps(1000000000)
# afficheTemps(temps)
# afficheDate(tempsEnDate(temps))


# import time
# print(secondeEnTemps(time.time()))
# afficheDate(tempsEnDate(secondeEnTemps(time.time())))
# secondeEnTemps(time.time())
# time.gmtime()

def nombreBisextile(jour: int):
    temps = (int(jour), 0, 0, 0)
    date = tempsEnDate(secondeEnTemps(tempsEnSeconde(temps)))
    annee = date[0]
    compteur = 0
    while annee != 0:
        if (annee % 4) == 0 and (annee % 100 != 0 or annee % 400 == 0):
            compteur += 1
        annee += -1
    return compteur


# print(nombreBisextile(200000))


def tempsEnDateBisextile(temps: list):
    jours = temps[0]
    jours += nombreBisextile(jours)
    date = (0, jours, temps[1], temps[2], temps[3])
    return date


# temps = secondeEnTemps(1000000000)
# afficheTemps(temps)
# afficheDate(tempsEnDateBisextile(temps))
# afficheDate()


def verifie(horaires: list):
    sommeHoraires = 0
    for elem in horaires:
        print("L'employé a fait", elem[1] + 24 * elem[0], "heures dans la semaine.")
        sommeHoraires += tempsEnSeconde(elem)
        if tempsEnSeconde(elem) > (48 * 3600) or sommeHoraires > (140 * 3600):
            return print("Les horaires limites ont été dépassés.", "Il a fait", sommeHoraires // 3600, "heures dans le mois.")
    return print("Les horaires limites ont été respectés.", "Il a fait", sommeHoraires // 3600, "heures dans le mois.")


# horaires = [[1, 2, 39, 34], [0, 3, 9, 4], [0, 2, 39, 51], [0, 1, 13, 46]]
# verifie(horaires)


