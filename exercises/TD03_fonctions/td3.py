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



