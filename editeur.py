import pandas as pd
import matplotlib.pyplot as plt

chemin_ADO = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Ado.csv'
chemin_mangas = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_BD-Mangas.csv'
chemin_enfants = r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Enfants.csv'

df_ado = pd.read_csv(chemin_ADO, sep='|', encoding='utf-8')
df_mangas = pd.read_csv(chemin_mangas, sep='|', encoding='utf-8')
df_enfants = pd.read_csv(chemin_enfants, sep='|', encoding='utf-8')

# nombre d'éditeurs différents
nombre_editeurs = df_ado['Editeur'].nunique()
print("Nombre d'éditeurs différents dans ado :", nombre_editeurs)

nombre_editeurs = df_mangas['Editeur'].nunique()
print("Nombre d'éditeurs différents dans mangas :", nombre_editeurs)

nombre_editeurs = df_enfants['Editeur'].nunique()
print("Nombre d'éditeurs différents dans enfants :", nombre_editeurs)

# extraire les editeurs de chaque base de données
editeurs_ado = set(df_ado['Editeur'].unique())
editeurs_mangas = set(df_mangas['Editeur'].unique())
editeurs_enfants = set(df_enfants['Editeur'].unique())

# trouver les éditeurs communs
editeurs_communs_ado_mangas = editeurs_ado.intersection(editeurs_mangas)
editeurs_communs_ado_enfants = editeurs_ado.intersection(editeurs_enfants)
editeurs_communs_mangas_enfants = editeurs_enfants.intersection(editeurs_mangas)

# les éditeurs communs
print("Éditeurs communs entre les romans pour adolescents et les mangas :", editeurs_communs_ado_mangas)
print("Éditeurs communs entre les romans pour adolescents et les livres pour enfants :", editeurs_communs_ado_enfants)
print("Éditeurs communs entre les mangas  et les livres pour enfants :", editeurs_communs_mangas_enfants)

# filtrer les livres des éditeurs communs
livres_ado_editeurs_communs = df_ado[df_ado['Editeur'].isin(editeurs_communs_ado_mangas.union(editeurs_communs_ado_enfants))]
livres_mangas_editeurs_communs = df_mangas[df_mangas['Editeur'].isin(editeurs_communs_ado_mangas)]
livres_enfants_editeurs_communs = df_enfants[df_enfants['Editeur'].isin(editeurs_communs_ado_enfants)]

# supprimer les NA pour la variable prix
livres_ado_editeurs_communs = livres_ado_editeurs_communs.dropna(subset=['Prix'])
livres_mangas_editeurs_communs = livres_mangas_editeurs_communs.dropna(subset=['Prix'])
livres_enfants_editeurs_communs = livres_enfants_editeurs_communs.dropna(subset=['Prix'])

# moyenne des prix par éditeur
moyenne_prix_par_editeur_ado = livres_ado_editeurs_communs.groupby('Editeur')['Prix'].mean()
moyenne_prix_par_editeur_mangas = livres_mangas_editeurs_communs.groupby('Editeur')['Prix'].mean()
moyenne_prix_par_editeur_enfants = livres_enfants_editeurs_communs.groupby('Editeur')['Prix'].mean()

# moyenne des prix par genre
print("Moyenne des prix par éditeur pour les romans pour adolescents :")
print(moyenne_prix_par_editeur_ado)
print("\nMoyenne des prix par éditeur pour les mangas :")
print(moyenne_prix_par_editeur_mangas)
print("\nMoyenne des prix par éditeur pour les livres pour enfants :")
print(moyenne_prix_par_editeur_enfants)

# fusion des moyennes de prix par éditeur pour les romans d'adolescents et les mangas
moyenne_prix_par_editeur = pd.merge(moyenne_prix_par_editeur_ado, moyenne_prix_par_editeur_mangas,
                                    on='Editeur', suffixes=('_ado', '_mangas'))

# difference de prix
moyenne_prix_par_editeur['Différence'] = moyenne_prix_par_editeur['Prix_mangas'] - moyenne_prix_par_editeur['Prix_ado']
moyenne_prix_par_editeur = moyenne_prix_par_editeur.sort_values(by='Différence', ascending=False)

# graphique
fig, ax = plt.subplots(figsize=(10, 6))
moyenne_prix_par_editeur['Prix_ado'].plot(kind='bar', ax=ax, color='skyblue', width=0.4, position=0,
                                          label='Romans pour Adolescents')
moyenne_prix_par_editeur['Prix_mangas'].plot(kind='bar', ax=ax, color='salmon', width=0.4, position=1,
                                              label='Mangas')

ax.set_title('Moyenne des prix par éditeur - Romans pour Adolescents vs Mangas')
ax.set_ylabel('Prix moyen')
ax.set_xlabel('Editeur')
ax.legend()
plt.tight_layout()
plt.show()

#ado vs enfants

moyenne_prix_par_editeur = pd.merge(moyenne_prix_par_editeur_ado, moyenne_prix_par_editeur_enfants,
                                    on='Editeur', suffixes=('_ado', '_enfants'))

moyenne_prix_par_editeur['Différence'] = moyenne_prix_par_editeur['Prix_enfants'] - moyenne_prix_par_editeur['Prix_ado']
moyenne_prix_par_editeur = moyenne_prix_par_editeur.sort_values(by='Différence', ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))

# Tracé des moyennes de prix par éditeur pour les romans d'adolescents
moyenne_prix_par_editeur['Prix_ado'].plot(kind='bar', ax=ax, color='skyblue', width=0.4, position=0,
                                          label='Romans pour Adolescents')

# Tracé des moyennes de prix par éditeur pour les mangas
moyenne_prix_par_editeur['Prix_enfants'].plot(kind='bar', ax=ax, color='green', width=0.4, position=1,
                                              label='Enfants')

ax.set_title('Moyenne des prix par éditeur - Romans pour Adolescents et livres enfants')
ax.set_ylabel('Prix moyen')
ax.set_xlabel('Editeur')
ax.legend()
plt.tight_layout()
plt.show()

##mangas et enfants

moyenne_prix_par_editeur = pd.merge(moyenne_prix_par_editeur_mangas, moyenne_prix_par_editeur_enfants,
                                    on='Editeur', suffixes=('_mangas', '_enfants'))

moyenne_prix_par_editeur['Différence'] = moyenne_prix_par_editeur['Prix_enfants'] - moyenne_prix_par_editeur['Prix_mangas']
moyenne_prix_par_editeur = moyenne_prix_par_editeur.sort_values(by='Différence', ascending=False)

# graphique
fig, ax = plt.subplots(figsize=(10, 6))

# Tracé des moyennes de prix par éditeur pour les romans d'adolescents
moyenne_prix_par_editeur['Prix_mangas'].plot(kind='bar', ax=ax, color='salmon', width=0.4, position=0,
                                          label='Mangas et BD')

# Tracé des moyennes de prix par éditeur pour les mangas
moyenne_prix_par_editeur['Prix_enfants'].plot(kind='bar', ax=ax, color='green', width=0.4, position=1,
                                              label='Enfants')

ax.set_title('Moyenne des prix par éditeur - Mangas-BD et livres enfants')
ax.set_ylabel('Prix moyen')
ax.set_xlabel('Editeur')
ax.legend()
plt.tight_layout()
plt.show()


