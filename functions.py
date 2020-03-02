import requests, csv, unicodedata, wikipedia
from datetime import datetime

URL ='https://fr.wikipedia.org/w/api.php'


mois_chiffre = {"janvier": 1,
                "fevrier": 2,
                "février":2,
                "mars": 3,
                "avril": 4,
                "mai": 5,
                "juin": 6,
                "juillet": 7,
                "aout": 8,
                "août": 8,
                "septembre": 9,
                "octobre": 10,
                "novembre": 11,
                "decembre": 12,
                "décembre": 12
                }

def get_page_id(nom):
        """Cette fonction nous renvoi la page id wikipedia 
            d'un nom rentré """

        #Besoin d'encodé pour suprimmer les charactères spéciaux
        nom = nom.title() #Les premieres lettres en majuscules

        PARAMS = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
            'titles': nom
        }

        response = requests.get(URL, params=PARAMS)
        data = response.json()
        ids = data["query"]["pages"]
        for key in ids:
            if type(key) == str:
                return key
                
def get_summary(page_id):
        """This function will return the summary of a article
            thanks to a page_id"""

        PARAMS = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
            'pageids': page_id
        }

        
        response = requests.get(URL, params=PARAMS)
        data = response.json()
        resume = data["query"]["pages"][page_id]["extract"]
        return resume
    

def get_naissance(summary):
    '''Cette fonction nous renvoi l'age sous ce format
        j/m/a'''
    listed = summary.split()

    for mots in listed:
        if mots in mois_chiffre:
            mois = (mois_chiffre[mots])
            position_mois = listed.index(mots)
            jour= (listed[position_mois - 1]).replace(',','')
            jour = jour.replace('1er','1') 
            annee = (listed[position_mois + 1]).replace(',','')

    return datetime(int(annee),int(mois),int(jour))

def get_age(naissance):
    '''Cettte fonction prend une date de naissance
        en format datetime et nous renvoi les années
        passé entre cette derniere et aujourd'hui'''

    aujourdhui = datetime.now()
    age = aujourdhui.year - naissance.year -((aujourdhui.month, aujourdhui.day) <(naissance.month, naissance.day)) #Cacul l'age au jour pres
    return age

def excell(nom, age):
    '''Cette fonction ecrit dans un fichier excel les noms et ages'''
    line =[nom,age]
    with open('ages.csv', mode='a') as csv_file:

        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(line)
    return "enregistrer dans le fichier."

def ouvrir_fichier(nom_fichier):
    '''Fonction qui prend en parametre un fichier
    et renvoie les noms sous forme de list'''

    with open(nom_fichier + '.txt','r') as fichier:
        liste_noms =[]
        for noms in fichier:
            liste_noms.append(noms)
       # Après avoir recupérer nos noms il faut enlever les \n   
         
    for ligne, nom in enumerate(liste_noms):
            liste_noms[ligne] = nom.strip()

    return liste_noms


def bypass_api(nom):
    '''Si l'api ne renvoi pas de page id on essaie avec ca'''

    wikipedia.set_lang("fr")
    resume = wikipedia.summary(nom)
    return resume


