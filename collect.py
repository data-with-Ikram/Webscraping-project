#BIBLIOTHEQUES
import re
import os
import requests
from bs4 import BeautifulSoup

request_headers = {'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6)"}

#collecte des pages des livres pour ADO

# url de la catégorie romans ado
url_categorie_base = 'https://www.librairiecharlemagne.com/rayon/romans-adolescents-jeunes-adultes/'

# requête
req_categorie = requests.get(url_categorie_base, headers=request_headers, timeout=10)
contenu_categorie = req_categorie.text

if req_categorie.status_code == 200 and len(contenu_categorie) > 500:

    soup = BeautifulSoup(contenu_categorie, 'html.parser')
    elements_page = soup.find_all(attrs={'data-product': True})

    i = 1
    # extraire les urls de chaque livre sur la première page
    for element_page in elements_page:
        match_page = element_page.find('a', href=re.compile(r'/livre/'))
        if match_page:
            livre_url_page = 'https://www.librairiecharlemagne.com' + match_page['href']
            req_livre_page = requests.get(livre_url_page, headers=request_headers, timeout=10)
            contenu_livre_page = req_livre_page.text
            dossier_livre = 'Data/Ado/'
            if not os.path.exists(dossier_livre):
                os.makedirs(dossier_livre)

            # enregistrement dans un fichier
            with open(f'{dossier_livre}livre_{i}.html', 'w', encoding='utf8') as output:
                output.write(contenu_livre_page)
            i += 1

    for page in range(2, 495):

        page_url = f'{url_categorie_base}?page={page}'
        req_page = requests.get(page_url, headers=request_headers, timeout=10)
        contenu_page = req_page.text
        soup_page = BeautifulSoup(contenu_page, 'html.parser')
        elements_page = soup_page.find_all(attrs={'data-product': True})

        for element_page in elements_page:
            match_page = element_page.find('a', href=re.compile(r'/livre/'))
            if match_page:
                livre_url_page = 'https://www.librairiecharlemagne.com' + match_page['href']

                # requête
                req_livre_page = requests.get(livre_url_page, headers=request_headers, timeout=10)
                contenu_livre_page = req_livre_page.text

                with open(f'{dossier_livre}livre_{i}.html', 'w', encoding='utf8') as output:
                    output.write(contenu_livre_page)
                i += 1


#collecte des pages - mangas & BD


url_categorie_base = 'https://www.librairiecharlemagne.com/rayon/bd-comics-mangas/'
req_categorie = requests.get(url_categorie_base, headers=request_headers, timeout=10)
contenu_categorie = req_categorie.text

if req_categorie.status_code == 200 and len(contenu_categorie) > 500:
    soup = BeautifulSoup(contenu_categorie, 'html.parser')
    elements_page = soup.find_all(attrs={'data-product': True})

    i = 1

    for element_page in elements_page:
        match_page = element_page.find('a', href=re.compile(r'/livre/'))
        if match_page:
            livre_url_page = 'https://www.librairiecharlemagne.com' + match_page['href']
            req_livre_page = requests.get(livre_url_page, headers=request_headers, timeout=10)
            contenu_livre_page = req_livre_page.text

            dossier_livre = 'Data/BD-Mangas/'
            if not os.path.exists(dossier_livre):
                os.makedirs(dossier_livre)

            with open(f'{dossier_livre}livre_{i}.html', 'w', encoding='utf8') as output:
                output.write(contenu_livre_page)
            i += 1

    for page in range(2, 495):
        page_url = f'{url_categorie_base}?page={page}'
        req_page = requests.get(page_url, headers=request_headers, timeout=10)
        contenu_page = req_page.text
        soup_page = BeautifulSoup(contenu_page, 'html.parser')
        elements_page = soup_page.find_all(attrs={'data-product': True})

        for element_page in elements_page:
            match_page = element_page.find('a', href=re.compile(r'/livre/'))
            if match_page:
                livre_url_page = 'https://www.librairiecharlemagne.com' + match_page['href']
                req_livre_page = requests.get(livre_url_page, headers=request_headers, timeout=10)
                contenu_livre_page = req_livre_page.text

                with open(f'{dossier_livre}livre_{i}.html', 'w', encoding='utf8') as output:
                    output.write(contenu_livre_page)
                i += 1

#collecte des pages des livres pour enfants


url_categorie_base = 'https://www.librairiecharlemagne.com/rayon/livres-pour-enfants/'
req_categorie = requests.get(url_categorie_base, headers=request_headers, timeout=10)
contenu_categorie = req_categorie.text

if req_categorie.status_code == 200 and len(contenu_categorie) > 500:
    soup = BeautifulSoup(contenu_categorie, 'html.parser')
    elements_page = soup.find_all(attrs={'data-product': True})

    i = 1
    for element_page in elements_page:
        match_page = element_page.find('a', href=re.compile(r'/livre/'))
        if match_page:
            livre_url_page = 'https://www.librairiecharlemagne.com' + match_page['href']
            req_livre_page = requests.get(livre_url_page, headers=request_headers, timeout=10)
            contenu_livre_page = req_livre_page.text

            dossier_livre = 'Data/Enfants/'
            if not os.path.exists(dossier_livre):
                os.makedirs(dossier_livre)

            with open(f'{dossier_livre}livre_{i}.html', 'w', encoding='utf8') as output:
                output.write(contenu_livre_page)
            i += 1

    for page in range(2, 494):
        page_url = f'{url_categorie_base}?page={page}'
        req_page = requests.get(page_url, headers=request_headers, timeout=10)
        contenu_page = req_page.text
        soup_page = BeautifulSoup(contenu_page, 'html.parser')
        elements_page = soup_page.find_all(attrs={'data-product': True})

        for element_page in elements_page:
            match_page = element_page.find('a', href=re.compile(r'/livre/'))
            if match_page:
                livre_url_page = 'https://www.librairiecharlemagne.com' + match_page['href']
                req_livre_page = requests.get(livre_url_page, headers=request_headers, timeout=10)
                contenu_livre_page = req_livre_page.text

                with open(f'{dossier_livre}livre_{i}.html', 'w', encoding='utf8') as output:
                    output.write(contenu_livre_page)
                i += 1
