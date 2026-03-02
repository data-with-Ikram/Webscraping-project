#analyses descriptives

#moyennes des prix, pages et poids

import pandas as pd
import pdb

chemin_ADO = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Ado.csv'
chemin_mangas = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_BD-Mangas.csv'
chemin_enfants = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Enfants.csv'

# 3 dataframes
df_ado = pd.read_csv(chemin_ADO, sep='|', encoding='utf-8')
df_mangas = pd.read_csv(chemin_mangas, sep='|', encoding='utf-8')
df_enfants = pd.read_csv(chemin_enfants, sep='|', encoding='utf-8')

#nombre de livres

nb_livres_ado = df_ado.shape[0] - 1
nb_livres_mangas = df_mangas.shape[0] - 1
nb_livres_enfants = df_enfants.shape[0] - 1

print(f"Nombre total de livres dans ado : {nb_livres_ado}")
print(f"Nombre total de livres dans mangas : {nb_livres_mangas}")
print(f"Nombre total de livres dans enfants : {nb_livres_enfants}")

#VARIABLE PRIX

# valeurs manquantes
NA_prix_ado = df_ado['Prix'].isna()
NA_prix_mangas = df_mangas['Prix'].isna()
NA_prix_enfants = df_enfants['Prix'].isna()

# nombre de NA
nb_NA_prix_ado = NA_prix_ado.sum()
print(f"{nb_NA_prix_ado} livres pour ado sur {nb_livres_ado} n'ont pas encore de prix affiché ")

nb_NA_prix_mangas = NA_prix_mangas.sum()
print(f"{nb_NA_prix_mangas} mangas sur {nb_livres_mangas} n'ont pas encore de prix affiché ")

nb_NA_prix_enfants = NA_prix_enfants.sum()
print(f"{nb_NA_prix_enfants} livres pour enfants sur {nb_livres_enfants} n'ont pas encore de prix affiché ")

# moyenne prix
moyenne_prix_ado = df_ado['Prix'].mean(skipna=True)
moyenne_prix_mangas = df_mangas['Prix'].mean(skipna=True)
moyenne_prix_enfants = df_enfants['Prix'].mean(skipna=True)

print(f"Moyenne des prix des livres pour ado : {moyenne_prix_ado}")
print(f"Moyenne des prix des mangas : {moyenne_prix_mangas}")
print(f"Moyenne des prix des livres pour enfants : {moyenne_prix_enfants}")


#VARIABLE POIDS

NA_poids_ado = df_ado['Poids'].isna()
NA_poids_mangas = df_mangas['Poids'].isna()
NA_poids_enfants = df_enfants['Poids'].isna()

nb_NA_poids_ado = NA_poids_ado.sum()
print(f"{nb_NA_poids_ado} livres pour ado sur {nb_livres_ado} n'ont pas encore de poids affiché ")

nb_NA_poids_mangas = NA_poids_mangas.sum()
print(f"{nb_NA_poids_mangas} mangas sur {nb_livres_mangas} n'ont pas encore de poids affiché")

nb_NA_poids_enfants = NA_poids_enfants.sum()
print(f"{nb_NA_poids_enfants} livres pour enfants sur {nb_livres_enfants} n'ont pas encore de poids affiché")

# moyenne poids
moyenne_poids_ado = df_ado['Poids'].mean(skipna=True)
moyenne_poids_mangas = df_mangas['Poids'].mean(skipna=True)
moyenne_poids_enfants = df_enfants['Poids'].mean(skipna=True)

print(f"Moyenne des poids des livres pour ado : {moyenne_poids_ado}")
print(f"Moyenne des poids des mangas : {moyenne_poids_mangas}")
print(f"Moyenne des poids des livres pour enfants : {moyenne_poids_enfants}")

#VARIABLE PAGES

NA_pages_ado = df_ado['Pages'].isna()
NA_pages_mangas = df_mangas['Pages'].isna()
NA_pages_enfants = df_enfants['Pages'].isna()

nb_NA_pages_ado = NA_pages_ado.sum()
print(f"{nb_NA_pages_ado} livres pour ado n'ont pas d'indication sur le nombre de pages")

nb_NA_pages_mangas = NA_pages_mangas.sum()
print(f"{nb_NA_pages_mangas} mangas n'ont pas d'indication sur le nombre de pages")

nb_NA_pages_enfants = NA_pages_enfants.sum()
print(f"{nb_NA_pages_enfants} livres pour enfants n'ont pas d'indication sur le nombre de pages")

# moyenne pages
moyenne_pages_ado = df_ado['Pages'].mean(skipna=True)
moyenne_pages_mangas = df_mangas['Pages'].mean(skipna=True)
moyenne_pages_enfants = df_enfants['Pages'].mean(skipna=True)

print(f"Moyenne des pages des livres pour ado : {moyenne_pages_ado}")
print(f"Moyenne des pages des mangas : {moyenne_pages_mangas}")
print(f"Moyenne des pages des livres pour enfants : {moyenne_pages_enfants}")


##TABLEAU MOYENNE

tableau_moyenne =  {'Catégories': ['Romans adolescents', 'BD-mangas', 'Enfants'],
           'Prix': [moyenne_prix_ado, moyenne_prix_mangas, moyenne_prix_enfants],
            'Poids': [moyenne_poids_ado, moyenne_poids_mangas, moyenne_poids_enfants],
            'Pages': [moyenne_pages_ado,moyenne_pages_mangas,moyenne_pages_enfants]}

df = pd.DataFrame(tableau_moyenne)
print(df)

#GRAPHIQUES

#LIEN ENTRE PRIX ET POIDS POUR CHAQUE categories (prix en fonction du poids)

#graphique ado
#VALEUR ABERRANTE
print(df_ado['Prix'].max())
print(df_ado.loc[df_ado['Prix'] == 9000, 'EAN13']) #valeur aberrante

#GRAPHIQUE

import matplotlib.pyplot as plt

# on exclut les valeurs aberrantes (par exemple, les livres avec un prix de 9000)
df_ado_filtre = df_ado[df_ado['Prix'] != 9000]


# creation du nuage en points
plt.scatter(df_ado_filtre['Poids'], df_ado_filtre['Prix'])
plt.xlabel('Poids')
plt.ylabel('Prix')
plt.title('Relation entre prix et poids des livres - romans d\'adolescents')
plt.show()


#graphique mangas

plt.scatter(df_mangas['Poids'], df_mangas['Prix'], color='red')
plt.xlabel('Poids')
plt.ylabel('Prix')
plt.title('Relation entre prix et poids des livres - BD-mangas')
plt.show()

#graphique enfants

plt.scatter(df_enfants['Poids'], df_enfants['Prix'], color='green')
plt.xlabel('Poids')
plt.ylabel('Prix')
plt.title('Relation entre prix et poids des livres - livres enfants ')
plt.show()

#correlation prix-poids

correlation_ado = df_ado['Prix'].corr(df_ado['Poids'])
print("Corrélation entre prix et poids ado :", correlation_ado)

correlation_mangas = df_mangas['Prix'].corr(df_mangas['Poids'])
print("Corrélation entre prix et poids mangas :", correlation_mangas)

correlation_enfants = df_enfants['Prix'].corr(df_enfants['Poids'])
print("Corrélation entre prix et poids enfants :", correlation_enfants)


#LIEN ENTRE PRIX et pages

#ado

plt.scatter(df_ado['Pages'], df_ado['Prix'])
plt.xlabel('Pages')
plt.ylabel('Prix')
plt.title('Relation entre le prix et les pages - romans adolescents')
plt.show()


#mangas

plt.scatter(df_mangas['Pages'], df_mangas['Prix'], color='red')
plt.xlabel('Pages')
plt.ylabel('Prix')
plt.title('Relation entre le prix et les pages - BD-mangas')
plt.show()

#enfants

plt.scatter(df_enfants['Pages'], df_enfants['Prix'], color='green')
plt.xlabel('Pages')
plt.ylabel('Prix')
plt.title('Relation entre le prix et les pages - livres enfants')
plt.show()

#correlation prix-pages

correlation_ado = df_ado['Prix'].corr(df_ado['Pages'])
print("Corrélation entre prix et pages ado :", correlation_ado)

correlation_mangas = df_mangas['Prix'].corr(df_mangas['Pages'])
print("Corrélation entre prix et pages mangas :", correlation_mangas)

correlation_enfants = df_enfants['Prix'].corr(df_enfants['Pages'])
print("Corrélation entre prix et pages enfants :", correlation_enfants)

#evolution des prix selon la date de publication

#ROMAN ADO

# conversion de la colonne "Date_de_publication" en datetime
df_ado['Date_de_publication'] = pd.to_datetime(df_ado['Date_de_publication'])

# extraire l'année de chaque date
df_ado['Annee'] = df_ado['Date_de_publication'].dt.year

# filtre les données à partir de l'année 1990
df_ado_filtre = df_ado[df_ado['Annee'] >= 1990]

# creation du dataframe
df_ado_annee_prix = df_ado_filtre[['Annee', 'Prix']]

# calcul de la moyenne des prix et le nombre de livres pour chaque année
moyennes_prix_par_annee = df_ado_annee_prix.groupby('Annee')['Prix'].agg(['mean', 'count']).reset_index()

# évolution des moyennes des prix et le nombre de livres dans un graphique
fig, ax1 = plt.subplots()

# moyenne des prix
color = 'tab:red'
ax1.set_xlabel('Année de publication')
ax1.set_ylabel('Moyenne des Prix', color=color)
ax1.plot(moyennes_prix_par_annee['Annee'], moyennes_prix_par_annee['mean'], marker='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# deuxième axe pour le nombre de livres
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Nombre de Livres', color=color)
ax2.plot(moyennes_prix_par_annee['Annee'], moyennes_prix_par_annee['count'], marker='o', color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.title('Évolution des prix selon l\'année de publication - romans adolescents')
plt.show()

#plus un livre est recent et plus en moyenne il coûte cher

#MANGAS

df_mangas['Date_de_publication'] = pd.to_datetime(df_mangas['Date_de_publication'])
df_mangas['Annee'] = df_mangas['Date_de_publication'].dt.year

df_mangas_filtre = df_mangas[df_mangas['Annee'] >= 2000]
df_mangas_annee_prix = df_mangas_filtre[['Annee', 'Prix']]
moyennes_prix_par_annee = df_mangas_annee_prix.groupby('Annee')['Prix'].agg(['mean', 'count']).reset_index()

fig, ax1 = plt.subplots()

# pour tracer la moyenne des prix
color = 'tab:red'
ax1.set_xlabel('Année de publication')
ax1.set_ylabel('Moyenne des Prix', color=color)
ax1.plot(moyennes_prix_par_annee['Annee'], moyennes_prix_par_annee['mean'], marker='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# deuxième axe pour le nombre de livres
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Nombre de Livres', color=color)
ax2.plot(moyennes_prix_par_annee['Annee'], moyennes_prix_par_annee['count'], marker='o', color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Évolution des prix selon l\'année de publication - BD-Mangas')
plt.show()

#ENFANTS

df_enfants['Date_de_publication'] = pd.to_datetime(df_enfants['Date_de_publication'])
df_enfants['Annee'] = df_enfants['Date_de_publication'].dt.year
df_enfants_filtre = df_enfants[df_enfants['Annee'] >= 2000]
df_enfants_annee_prix = df_enfants_filtre[['Annee', 'Prix']]
moyennes_prix_par_annee = df_enfants_annee_prix.groupby('Annee')['Prix'].agg(['mean', 'count']).reset_index()

fig, ax1 = plt.subplots()

#premier axe
color = 'tab:red'
ax1.set_xlabel('Année de publication')
ax1.set_ylabel('Moyenne des Prix', color=color)
ax1.plot(moyennes_prix_par_annee['Annee'], moyennes_prix_par_annee['mean'], marker='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# deuxieme axe
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Nombre de Livres', color=color)
ax2.plot(moyennes_prix_par_annee['Annee'], moyennes_prix_par_annee['count'], marker='o', color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Évolution des prix selon l\'année de publication - livres pour enfants')
plt.show()



#tableaux croisées : lignes (commande, à paraitre, dispo), colonnes (localisation)

#base_ado

print(df_ado['Dispo_Fréjus'].value_counts())
print(df_ado['Dispo_La_Valette'].value_counts())
print(df_ado['Dispo_Seyne'].value_counts())
print(df_ado['Dispo_Toulon'].value_counts())
print(df_ado['Dispo_La_Soupe'].value_counts())
print(df_ado['Dispo_Hyères'].value_counts())

# creation des dataframes pour chaque variable
dispo_frejus_counts = df_ado['Dispo_Fréjus'].value_counts().to_dict()
df_dispo_frejus = pd.DataFrame(list(dispo_frejus_counts.items()), columns=['Statut', 'Nombre_Fréjus'])

dispo_la_valette_counts = df_ado['Dispo_La_Valette'].value_counts().to_dict()
df_dispo_la_valette = pd.DataFrame(list(dispo_la_valette_counts.items()), columns=['Statut', 'Nombre_La_Valette'])

dispo_seyne_counts = df_ado['Dispo_Seyne'].value_counts().to_dict()
df_dispo_seyne = pd.DataFrame(list(dispo_seyne_counts.items()), columns=['Statut', 'Nombre_Seyne'])

dispo_toulon_counts = df_ado['Dispo_Toulon'].value_counts().to_dict()
df_dispo_toulon = pd.DataFrame(list(dispo_toulon_counts.items()), columns=['Statut', 'Nombre_Toulon'])

dispo_la_soupe_counts = df_ado['Dispo_La_Soupe'].value_counts().to_dict()
df_dispo_la_soupe = pd.DataFrame(list(dispo_la_soupe_counts.items()), columns=['Statut', 'Nombre_La_Soupe'])

dispo_hyeres_counts = df_ado['Dispo_Hyères'].value_counts().to_dict()
df_dispo_hyeres = pd.DataFrame(list(dispo_hyeres_counts.items()), columns=['Statut', 'Nombre_Hyères'])

# concatener les df en fonction de la variable statut
df_stats = pd.concat([df_dispo_frejus, df_dispo_la_valette, df_dispo_seyne, df_dispo_toulon, df_dispo_la_soupe, df_dispo_hyeres])
merged_df = df_stats.groupby('Statut').sum().reset_index()
print(merged_df)

merged_df['Nombre_Fréjus'] /= 11817
merged_df['Nombre_La_Valette'] /= 11817
merged_df['Nombre_Seyne'] /= 11817
merged_df['Nombre_Toulon'] /= 11817
merged_df['Nombre_La_Soupe'] /= 11817
merged_df['Nombre_Hyères'] /= 11817

print(merged_df.to_string(index=False))

#mangas

dispo_frejus_counts = df_mangas['Dispo_Fréjus'].value_counts().to_dict()
df_dispo_frejus = pd.DataFrame(list(dispo_frejus_counts.items()), columns=['Statut', 'Nombre_Fréjus'])

dispo_la_valette_counts = df_mangas['Dispo_La_Valette'].value_counts().to_dict()
df_dispo_la_valette = pd.DataFrame(list(dispo_la_valette_counts.items()), columns=['Statut', 'Nombre_La_Valette'])

dispo_seyne_counts = df_mangas['Dispo_Seyne'].value_counts().to_dict()
df_dispo_seyne = pd.DataFrame(list(dispo_seyne_counts.items()), columns=['Statut', 'Nombre_Seyne'])

dispo_toulon_counts = df_mangas['Dispo_Toulon'].value_counts().to_dict()
df_dispo_toulon = pd.DataFrame(list(dispo_toulon_counts.items()), columns=['Statut', 'Nombre_Toulon'])

dispo_la_soupe_counts = df_mangas['Dispo_La_Soupe'].value_counts().to_dict()
df_dispo_la_soupe = pd.DataFrame(list(dispo_la_soupe_counts.items()), columns=['Statut', 'Nombre_La_Soupe'])

dispo_hyeres_counts = df_mangas['Dispo_Hyères'].value_counts().to_dict()
df_dispo_hyeres = pd.DataFrame(list(dispo_hyeres_counts.items()), columns=['Statut', 'Nombre_Hyères'])

df_stats = pd.concat([df_dispo_frejus, df_dispo_la_valette, df_dispo_seyne, df_dispo_toulon, df_dispo_la_soupe, df_dispo_hyeres])
merged_df = df_stats.groupby('Statut').sum().reset_index()

merged_df['Nombre_Fréjus'] /= 11822
merged_df['Nombre_La_Valette'] /= 11822
merged_df['Nombre_Seyne'] /= 11822
merged_df['Nombre_Toulon'] /= 11822
merged_df['Nombre_La_Soupe'] /= 11822
merged_df['Nombre_Hyères'] /= 11822

print(merged_df.to_string(index=False))

#ENFANTS

dispo_frejus_counts = df_enfants['Dispo_Fréjus'].value_counts().to_dict()
df_dispo_frejus = pd.DataFrame(list(dispo_frejus_counts.items()), columns=['Statut', 'Nombre_Fréjus'])

dispo_la_valette_counts = df_enfants['Dispo_La_Valette'].value_counts().to_dict()
df_dispo_la_valette = pd.DataFrame(list(dispo_la_valette_counts.items()), columns=['Statut', 'Nombre_La_Valette'])

dispo_seyne_counts = df_enfants['Dispo_Seyne'].value_counts().to_dict()
df_dispo_seyne = pd.DataFrame(list(dispo_seyne_counts.items()), columns=['Statut', 'Nombre_Seyne'])

dispo_toulon_counts = df_enfants['Dispo_Toulon'].value_counts().to_dict()
df_dispo_toulon = pd.DataFrame(list(dispo_toulon_counts.items()), columns=['Statut', 'Nombre_Toulon'])

dispo_la_soupe_counts = df_enfants['Dispo_La_Soupe'].value_counts().to_dict()
df_dispo_la_soupe = pd.DataFrame(list(dispo_la_soupe_counts.items()), columns=['Statut', 'Nombre_La_Soupe'])

dispo_hyeres_counts = df_enfants['Dispo_Hyères'].value_counts().to_dict()
df_dispo_hyeres = pd.DataFrame(list(dispo_hyeres_counts.items()), columns=['Statut', 'Nombre_Hyères'])

df_stats = pd.concat([df_dispo_frejus, df_dispo_la_valette, df_dispo_seyne, df_dispo_toulon, df_dispo_la_soupe, df_dispo_hyeres])
merged_df = df_stats.groupby('Statut').sum().reset_index()

merged_df['Nombre_Fréjus'] /= 11505
merged_df['Nombre_La_Valette'] /= 11505
merged_df['Nombre_Seyne'] /= 11505
merged_df['Nombre_Toulon'] /= 11505
merged_df['Nombre_La_Soupe'] /= 11505
merged_df['Nombre_Hyères'] /= 11505

# df final
print(merged_df.to_string(index=False))



