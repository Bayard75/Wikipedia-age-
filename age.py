from functions import *
import unicodedata

print('Quel est le nom du fichier qui contient les noms ? (sans extention)')
nom_fichier = input()
liste_nom = ouvrir_fichier(nom_fichier)
for nom in liste_nom:
        resume = bypass_api(nom)
        naissance = get_naissance(resume)
        print(naissance)
        age = get_age(naissance)
        print(age)
        if age >= 40 and age <= 60:
            print(nom + ' a ' + str(age) +' ans \nInscription dans le fichier excell')
            excell(nom,age)
        else:
            print(nom + ' a ' + str(age) +" ce qui n'est pas dans la tranche recherché.\nSuivant")
