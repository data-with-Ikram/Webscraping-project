#CREATION D'UNE INTERFACE POUR UTILISATEUR

import tkinter as tk
from tkinter import ttk
import pandas as pd

chemin_ADO = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Ado.csv'
chemin_mangas = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_BD-Mangas.csv'
chemin_enfants = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Enfants.csv'

# Charger le fichier CSV dans un DataFrame
df_ado = pd.read_csv(chemin_ADO, sep='|', encoding='utf-8')
df_mangas = pd.read_csv(chemin_mangas, sep='|', encoding='utf-8')
df_enfants = pd.read_csv(chemin_enfants, sep='|', encoding='utf-8')

df_combined = pd.concat([df_ado, df_mangas, df_enfants], ignore_index=True)

def livres_par_editeur_auteur(dataframe, keyword):
    keyword = keyword.lower()  # Convertir en minuscules pour une correspondance insensible à la casse
    result = dataframe[(dataframe['Auteur'].str.lower().str.contains(keyword)) |
                       (dataframe['Editeur'].str.lower().str.contains(keyword)) |
                       (dataframe['Titre'].str.lower().str.contains(keyword))]
    return result

def livre_moins_cher(dataframe, keyword):
    keyword = keyword.lower()  # Convertir en minuscules pour une correspondance insensible à la casse
    result = dataframe[(dataframe['Auteur'].str.lower() == keyword) |
                       (dataframe['Editeur'].str.lower() == keyword) |
                       (dataframe['Titre'].str.lower() == keyword)].nsmallest(1, 'Prix')
    return result

def livre_plus_cher(dataframe, keyword):
    keyword = keyword.lower()  # Convertir en minuscules pour une correspondance insensible à la casse
    result = dataframe[(dataframe['Auteur'].str.lower() == keyword) |
                       (dataframe['Editeur'].str.lower() == keyword) |
                       (dataframe['Titre'].str.lower() == keyword)].nlargest(1, 'Prix')
    return result

def librairies_pour_livre(dataframe, keyword):
    keyword = keyword.lower()  # Convertir en minuscules pour une correspondance insensible à la casse
    result = dataframe[(dataframe['Titre'].str.lower() == keyword) |
                       (dataframe['EAN13'].astype(str) == keyword)][['Titre', 'EAN13', 'Dispo_Fréjus', 'Dispo_La_Valette', 'Dispo_Seyne', 'Dispo_Toulon', 'Dispo_La_Soupe', 'Dispo_Hyères']]
    return result

def search():
    keyword = entry.get()

    if search_type.get() == "Livres par éditeur / auteur":
        result = livres_par_editeur_auteur(df_combined, keyword)
        result_str = result.to_string(index=False)

        # Créer une nouvelle fenêtre pour afficher les résultats
        result_window = tk.Toplevel(root)
        result_text = tk.Text(result_window, height=20, width=100)
        result_text.pack()
        result_text.insert(tk.END, result_str)

    elif search_type.get() == "livre le moins cher":
        result = livre_moins_cher(df_combined, keyword)
        output.delete(1.0, tk.END)
        output.insert(tk.END, result.to_string(index=False))

    elif search_type.get() == "Livre plus cher":
        result = livre_plus_cher(df_combined, keyword)
        output.delete(1.0, tk.END)
        output.insert(tk.END, result.to_string(index=False))

    elif search_type.get() == "Librairies pour livre":
        result = librairies_pour_livre(df_combined, keyword)
        output.delete(1.0, tk.END)
        output.insert(tk.END, result.to_string(index=False))

    else:
        output.delete(1.0, tk.END)
        output.insert(tk.END, "Type de recherche non pris en charge.")

# Interface utilisateur
root = tk.Tk()
root.title("Recherche de livres")

search_type = ttk.Combobox(root, values=["Livres par éditeur / auteur", "Livre le moins cher", "Livre le plus cher", "Disponibilité du livre"])
search_type.set("Livres par éditeur / auteur")
search_type.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=10)

output = tk.Text(root, height=20, width=100)
output.pack()

search_button = ttk.Button(root, text="Rechercher", command=search)
search_button.pack(pady=10)

root.mainloop()

