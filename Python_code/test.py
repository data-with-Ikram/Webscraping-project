from scipy.stats import kruskal, shapiro, levene
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

chemin_ADO = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Ado.csv'
chemin_mangas = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_BD-Mangas.csv'
chemin_enfants = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Enfants.csv'

df_ado = pd.read_csv(chemin_ADO, sep='|', encoding='utf-8')
df_mangas = pd.read_csv(chemin_mangas, sep='|', encoding='utf-8')
df_enfants = pd.read_csv(chemin_enfants, sep='|', encoding='utf-8')

#BOXPLOT PRIX

# ajout d'une colonne "Catégorie" à chaque df
df_ado['Catégorie'] = 'Adolescents'
df_mangas['Catégorie'] = 'BD'
df_enfants['Catégorie'] = 'Enfants'

df_ado_cleaned = df_ado[df_ado['Prix'] < 9000] #enlever la valeur aberrante pour mieux voir la distribution

# df qui combine les 3 categories
combined_df = pd.concat([df_enfants, df_mangas, df_ado_cleaned])

combined_df['Log_Prix'] = np.log(combined_df['Prix'])

# boxplot
plt.figure(figsize=(10, 6))
boxplot = combined_df.boxplot(column='Log_Prix', by='Catégorie', figsize=(10, 6))
plt.title('Boxplot du log des prix des livres par catégorie')
plt.xlabel('Catégorie')
plt.ylabel('Prix en log')
plt.show()

#test difference prix
df_ado_n = df_ado.dropna(subset=['Prix'])
df_mangas_n = df_mangas.dropna(subset=['Prix'])
df_enfants_n = df_enfants.dropna(subset=['Prix'])

# separation des données en 3 échantillons
prix_ado = df_ado_n['Prix']
prix_mangas = df_mangas_n['Prix']
prix_enfants = df_enfants_n['Prix']

# Test de Levene pour l'homogénéité des variances
statistic, p_value = levene(prix_ado, prix_mangas, prix_enfants)
print("Test de Levene - Statistique:", statistic, "p-valeur:", p_value)

# Test de normalité
statistic, p_value = shapiro(prix_ado)
print("Test de normalité - prix_ado - Statistique:", statistic, "p-valeur:", p_value)

statistic, p_value = shapiro(prix_mangas)
print("Test de normalité - prix_mangas - Statistique:", statistic, "p-valeur:", p_value)

statistic, p_value = shapiro(prix_enfants)
print("Test de normalité - prix_enfants - Statistique:", statistic, "p-valeur:", p_value)

# kruskal

statistic, p_value = kruskal(prix_ado, prix_mangas, prix_enfants)

# resultat
print("Statistique:", statistic)
print("p-valeur:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Les échantillons ne proviennent pas de la même distribution")
else:
    print("Les échantillons proviennent probablement de la même distribution")

#POIDS

# boxplot
plt.figure(figsize=(10, 6))
boxplot = combined_df.boxplot(column='Poids', by='Catégorie', figsize=(10, 6))
plt.title('Boxplot des poids pour les livres par catégorie')
plt.xlabel('Catégorie')
plt.ylabel('Poids')
plt.show()

#test difference poids
df_ado_n = df_ado.dropna(subset=['Poids'])
df_mangas_n = df_mangas.dropna(subset=['Poids'])
df_enfants_n = df_enfants.dropna(subset=['Poids'])

poids_ado = df_ado_n['Poids']
poids_mangas = df_mangas_n['Poids']
poids_enfants = df_enfants_n['Poids']

# Test de Levene
statistic, p_value = levene(poids_ado, poids_mangas, poids_enfants)
print("Test de Levene - Statistique:", statistic, "p-valeur:", p_value)

# Test de normalité
statistic, p_value = shapiro(poids_ado)
print("Test de normalité - poids_ado - Statistique:", statistic, "p-valeur:", p_value)

statistic, p_value = shapiro(poids_mangas)
print("Test de normalité - poids_mangas - Statistique:", statistic, "p-valeur:", p_value)

statistic, p_value = shapiro(poids_enfants)
print("Test de normalité - poids_enfants - Statistique:", statistic, "p-valeur:", p_value)

#PAGES

# boxplot
plt.figure(figsize=(10, 6))
boxplot = combined_df.boxplot(column='Pages', by='Catégorie', figsize=(10, 6))
plt.title('Boxplot des pages pour les livres par catégorie')
plt.xlabel('Catégorie')
plt.ylabel('Pages')
plt.show()

#test difference pages
df_ado_n = df_ado.dropna(subset=['Pages'])
df_mangas_n = df_mangas.dropna(subset=['Pages'])
df_enfants_n = df_enfants.dropna(subset=['Pages'])

pages_ado = df_ado_n['Pages']
pages_mangas = df_mangas_n['Pages']
pages_enfants = df_enfants_n['Pages']

# Test de Levene
statistic, p_value = levene(pages_ado, pages_mangas, pages_enfants)
print("Test de Levene - Statistique:", statistic, "p-valeur:", p_value)

# Test de normalité
statistic, p_value = shapiro(pages_ado)
print("Test de normalité - pages_ado - Statistique:", statistic, "p-valeur:", p_value)

statistic, p_value = shapiro(pages_mangas)
print("Test de normalité - pages_mangas - Statistique:", statistic, "p-valeur:", p_value)

statistic, p_value = shapiro(pages_enfants)
print("Test de normalité - pages_enfants - Statistique:", statistic, "p-valeur:", p_value)


