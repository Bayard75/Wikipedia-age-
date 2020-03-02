from functions import *
import unicodedata, os

print('Quel est le nom du fichier qui contient les noms ? (sans extention)')
nom_fichier = input()
liste_nom = ouvrir_fichier(nom_fichier)
for nom in liste_nom:
        try:
            resume = bypass_api(nom)
        except wikipedia.exceptions.PageError:
                page = get_page_id(nom)
                resume = get_summary(page)
        except:
            print('PROBELEME AVEC LE COMEDIEN SUIVANT : '+nom)
            continue

        try:
            naissance = get_naissance(resume)
        except:
            print('PROBLEME AVEC LE COMEDIEN SUIVANT : '+nom)
            continue
        age = get_age(naissance)
        if age >= 40 and age <= 60:
            print(nom + ' a ' + str(age) +' ans \nInscription dans le fichier excell')
            excell(nom,age)
        else:
            print(nom + ' a ' + str(age) +" ce qui n'est pas dans la tranche recherché.\nSuivant")
os.system("pause")