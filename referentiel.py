# -*- coding: utf-8 -*-
# Permet de trouver un fuseau à  partir d'une position et vice et versa
# Martin Couture
# Cegep Limoilou, octobre 2019

# Prends un fuseau et retourne le méridien central
import math #Import du module math

#Deéfinition des fonctions

#Prends le fuseau et retourne le méridien central
def MTM_Meridien(fuseau):
    return str(((51 + (3 * fuseau)) - 1.5))

#Prends le fuseau et retourne le méridien central
def UTM_Meridien(fuseau):
    return str(((180 + (-6 * fuseau)) + 3))

#Prends la coordonnée et retourne le fuseau
def MTM_Fuseau(coordX):
    return str((math.floor((math.fabs(coordX) - 51) / 3) + 1))

#Prends la coordonnée et retourne le fuseau
def UTM_Fuseau(coordX):
    return str((math.floor((180-(math.fabs(coordX)))/6) + 1))


if __name__ == "__main__":  #Si l'application démarre avec ce fichier
    #Affichage de du menu
    print("Faire votre choix")
    print("\t1-Trouver le méridien central à partir d'un fuseau (MTM)")
    print("\t2-Trouver le méridien central à partir d'un fuseau (UTM)")
    print("\t3-Trouver le fuseau à partir d'une coordonnée (MTM)")
    print("\t4-Trouver le fuseau à partir d'une coordonnée (UTM)")
    #Lecture du choix
    choix = input("Faire votre choix:")

    #Si le choix est ...
    if choix=="1":
        f = int(input("Entrer le fuseau (MTM):"))
        print("Le méridien central est " + MTM_Meridien(f))
    elif choix=="2":
        f = int(input("Entrer le fuseau (UTM):"))
        print("Le méridien central est " + UTM_Meridien(f))
    elif choix=="3":
        coord = float(input("Entrer la coordonnée en format décimale (MTM):"))
        print("Le fuseau est " + MTM_Fuseau(coord))
    elif choix=="4":
        coord = float(input("Entrer la coordonnée en format décimal (MTM):"))
        print("Le fuseau est " + UTM_Fuseau(coord))
    else:
        print("Mauvais choix \n Bye!")
