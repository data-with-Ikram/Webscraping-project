import re
import pdb
import os
import pandas as pd
from html import unescape

def analyse(folder_path):
    Base = {}
    Base['EAN13'] = []
    Base['Titre'] = []
    Base['Auteur'] = []
    Base['Editeur'] = []
    Base['Date_de_publication'] = []
    Base['Pages'] = []
    Base['Poids'] = []
    Base['Prix'] = []
    Base['Dispo_Fréjus'] = []
    Base['Dispo_La_Valette'] = []
    Base['Dispo_Seyne'] = []
    Base['Dispo_Toulon'] = []
    Base['Dispo_La_Soupe'] = []
    Base['Dispo_Hyères'] = []

    Page = os.listdir(folder_path)

    for page in Page:
        page_path = os.path.join(folder_path, page)
        with open(page_path, 'r', encoding='utf-8') as output:
            contenu = output.read()

        #EAN13
        pattern_ean13 = r'>EAN13</dt>[\s\S]*?<dd>(\d+)</dd>'
        EAN13 = re.findall(pattern_ean13, contenu)

        # TITRE
        pattern_titre = r'<title>(.*?)<\/title>'
        Titre = re.findall(pattern_titre, contenu, re.DOTALL)  # Utiliser re.DOTALL pour inclure les sauts de ligne

        # editeur avec la balise <a>
        pattern_editeur_a = r'<a href="/editeur/([^"]*)">(.*?)</a>'
        Editeur_a = re.findall(pattern_editeur_a, contenu)

        # editeur avec la balise <dd>
        pattern_editeur_dd = r'<dd[^>]*itemprop="publisher"[^>]*>(.*?)</dd>'
        Editeur_dd = re.findall(pattern_editeur_dd, contenu)

        # DATE
        pattern_date = r'datetime="([^"]+)"'
        Date_de_publication = re.findall(pattern_date, contenu)

        # NOMBRE DE PAGES
        pattern_pages = r'itemprop="numberOfPages">(\d+)<\/dd>'
        Pages = re.findall(pattern_pages, contenu)

        # POIDS
        pattern_poids = r'itemtype="http:\/\/schema\.org\/Weight">(\d+)'
        Poids = re.findall(pattern_poids, contenu)

        # PRIX
        pattern_prix = r'<span class="price">([\d.]+)</span>'
        Prix = re.findall(pattern_prix, contenu)

        # DISPO_FREJUS
        pattern_frejus = r'Librairie Charlemagne Fréjus<\/td>\s*<td><span class="([^"]+)" >'
        pattern_frejus_2 = r'<span class="delay future"></span>'
        Dispo_frejus = re.findall(pattern_frejus, contenu)
        Dispo_frejus_2 = re.findall(pattern_frejus_2, contenu)

        # DISPO LA VALETTE
        pattern_v = r'Librairie Charlemagne La Valette<\/td>\s*<td><span class="([^"]+)" >'
        pattern_v_2 = r'<span class="delay future"></span>'
        Dispo_v = re.findall(pattern_v, contenu)
        Dispo_v_2 = re.findall(pattern_v_2, contenu)

        # DISPO seyne
        pattern_seyne = r'Librairie Charlemagne La-Seyne-sur-Mer<\/td>\s*<td><span class="([^"]+)" >'
        pattern_seyne_2 = r'<span class="delay future"></span>'
        Dispo_seyne = re.findall(pattern_seyne, contenu)
        Dispo_seyne_2 = re.findall(pattern_seyne_2, contenu)

        # DISPO TOULON
        pattern_T = r'Librairie Charlemagne Toulon<\/td>\s*<td><span class="([^"]+)" >'
        pattern_T_2 = r'<span class="delay future"></span>'
        Dispo_T = re.findall(pattern_T, contenu)
        Dispo_T_2 = re.findall(pattern_T_2, contenu)

        # DISPO LA SOUPE
        pattern_soupe = r'Librairie Charlemagne La Soupe de l&#39;Espace<\/td>\s*<td><span class="([^"]+)" >'
        pattern_soupe_2 = r'<span class="delay future"></span>'
        Dispo_soupe = re.findall(pattern_soupe, contenu)
        Dispo_soupe_2 = re.findall(pattern_soupe_2, contenu)

        # DISPO HYERES
        pattern_H = r'Librairie Charlemagne Hyères<\/td>\s*<td><span class="([^"]+)" >'
        pattern_H_2 = r'<span class="delay future"></span>'
        Dispo_H = re.findall(pattern_H, contenu)
        Dispo_H_2 = re.findall(pattern_H_2, contenu)

        if len(EAN13) == 1:
            ean13 = EAN13[0]
        else:
            print('Problème avec EAN13 sur la page', page)

        if Titre:
            # exception pour les tirets entourés de caractères alphanumériques
            titre = re.split(r'(?<!\w)-|-(?!\w)', Titre[0].replace('\n', ''))[0].strip()
            titre_split = re.split(r'(?<!\w)-|-(?!\w)', Titre[0].replace('\n', ''))
            if len(titre_split) >= 2:
                auteur = titre_split[-2].strip()
            else:
                # cas où la liste n'a pas assez d'éléments
                auteur = "NA"

            titre = unescape(titre)
            auteur = unescape(auteur)
        else:
            print('Pas de correspondance pour Titre/Auteur dans', page)
            titre = "NA"
            auteur = "NA"

        if Editeur_a:
            editeur = unescape(Editeur_a[0][1])
        elif Editeur_dd:
            editeur = unescape(Editeur_dd[0])
        else:
            print(f'Pas de correspondance dans {page}')

        if len(Date_de_publication) == 1:
            date_de_publication = Date_de_publication[0]
        else:
            date_de_publication = "NA"

        if len(Pages) == 1:
            pages = Pages[0]
        else:
            pages = "NA"

        if len(Poids) == 1:
            poids = Poids[0]
        else:
            print('Problème avec poids sur la page', page)
            poids = "NA"

        if Prix:
            prix = Prix[0]
        else:
            print('Problème avec prix sur la page', page)
            prix = "NA"

        # frejus
        if Dispo_frejus:
            dispo_frejus = Dispo_frejus[0]
            if dispo_frejus == "delay short":
                dispo_frejus = "en stock"
            elif dispo_frejus == "delay medium":
                dispo_frejus = "sur commande"
            else:
                dispo_frejus = "indisponible"

        elif Dispo_frejus_2:
            dispo_frejus = Dispo_frejus_2[0]
            if dispo_frejus:
                dispo_frejus = "à paraitre"
        else:
            print('Problème avec dispo_frejus sur la page', page)
            dispo_frejus = "NA"

        # VALETTE
        if Dispo_v:
            dispo_v = Dispo_v[0]
            if dispo_v == "delay short":
                dispo_v = "en stock"
            elif dispo_v == "delay medium":
                dispo_v = "sur commande"
            else:
                dispo_v = "indisponible"

        elif Dispo_v_2:
            dispo_v = Dispo_v_2[0]
            if dispo_v:
                dispo_v = "à paraitre"
        else:
            print('Problème avec dispo_valette sur la page', page)
            dispo_v = "NA"

        # SEYNE
        if Dispo_seyne:
            dispo_seyne = Dispo_seyne[0]
            if dispo_seyne == "delay short":
                dispo_seyne = "en stock"
            elif dispo_seyne == "delay medium":
                dispo_seyne = "sur commande"
            else:
                dispo_seyne = "indisponible"

        elif Dispo_seyne_2:
            dispo_seyne = Dispo_seyne_2[0]
            if dispo_seyne:
                dispo_seyne = "à paraitre"
        else:
            print('Problème avec dispo_seyne sur la page', page)
            dispo_seyne = "NA"

        # toulon
        if Dispo_T:
            dispo_t = Dispo_T[0]
            if dispo_t == "delay short":
                dispo_t = "en stock"
            elif dispo_t == "delay medium":
                dispo_t = "sur commande"
            else:
                dispo_t = "indisponible"

        elif Dispo_T_2:
            dispo_t = Dispo_T_2[0]
            if dispo_t:
                dispo_t = "à paraitre"
        else:
            print('Problème avec dispo_toulon sur la page', page)
            dispo_t = "NA"
        # soupe
        if Dispo_soupe:
            dispo_soupe = Dispo_soupe[0]
            if dispo_soupe == "delay short":
                dispo_soupe = "en stock"
            elif dispo_soupe == "delay medium":
                dispo_soupe = "sur commande"
            else:
                dispo_soupe = "indisponible"

        elif Dispo_soupe_2:
            dispo_soupe = Dispo_soupe_2[0]
            if dispo_soupe:
                dispo_soupe = "à paraitre"
        else:
            print('Problème avec dispo_soupe sur la page', page)
            dispo_soupe = "NA"

        # hyeres
        if Dispo_H:
            dispo_H = Dispo_H[0]
            if dispo_H == "delay short":
                dispo_H = "en stock"
            elif dispo_H == "delay medium":
                dispo_H = "sur commande"
            else:
                dispo_H = "indisponible"

        elif Dispo_H_2:
            dispo_H = Dispo_T_2[0]
            if dispo_H:
                dispo_H = "à paraitre"
        else:
            print('Problème avec dispo_hyeres sur la page', page)
            dispo_H = "NA"

        # ahout des valeurs à la base
        Base['EAN13'].append(ean13.replace('|', ''))
        Base['Titre'].append(titre.replace('|', ''))
        Base['Auteur'].append(auteur.replace('|', ''))
        Base['Editeur'].append(editeur.replace('|', ''))
        Base['Date_de_publication'].append(date_de_publication.replace('|', ''))
        Base['Pages'].append(pages.replace('|', ''))
        Base['Poids'].append(poids.replace('|', ''))
        Base['Prix'].append(prix.replace('|', ''))
        Base['Dispo_Fréjus'].append(dispo_frejus.replace('|', ''))
        Base['Dispo_La_Valette'].append(dispo_v.replace('|', ''))
        Base['Dispo_Seyne'].append(dispo_seyne.replace('|', ''))
        Base['Dispo_Toulon'].append(dispo_t.replace('|', ''))
        Base['Dispo_La_Soupe'].append(dispo_soupe.replace('|', ''))
        Base['Dispo_Hyères'].append(dispo_H.replace('|', ''))

    return Base

data_folders = ['Ado', 'BD-Mangas', 'Enfants']
data_path = 'C:/Users/OneDrive/Bureau/Projet_webscraping/Data'

for folder in data_folders:
    folder_path = os.path.join(data_path, folder)
    data = analyse(folder_path)
    df = pd.DataFrame(data)
    df.to_csv(f'DataFinal/Base_{folder}.csv', sep='|', encoding='utf-8', index=False)

