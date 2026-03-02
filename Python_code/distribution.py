#DISTRIBUTION HISTO PRIX

import matplotlib.pyplot as plt
import pandas as pd

df_ado = pd.read_csv(r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Ado.csv', sep='|', encoding='utf-8')

# histogramme des prix pour ados
plt.hist(df_ado['Prix'], bins=range(0, 9000, 5) , color='skyblue', edgecolor='black',  density=True)
plt.xlim(0, 50)
plt.xlabel('Prix')
plt.ylabel('Fréquence')
plt.title('Histogramme des prix romans adolescents')
plt.show()

#mangas
df_mangas = pd.read_csv(r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_BD-Mangas.csv', sep='|', encoding='utf-8')

# histogramme des prix pour mangas
plt.hist(df_mangas['Prix'], bins=range(0, 100, 5) , color='salmon', edgecolor='black',  density=True)
plt.xlim(0, 100)
plt.xlabel('Prix')
plt.ylabel('Fréquence')
plt.title('Histogramme des prix mangas')
plt.show()

#enfants
df_enfants = pd.read_csv(r'C:\Users\OneDrive\Bureau\Projet_webscraping\DataFinal\Base_Enfants.csv', sep='|', encoding='utf-8')

# histogramme des prix pour enfants
plt.hist(df_enfants['Prix'], bins=range(0, 50, 5) , color='green', edgecolor='black',  density=True)
plt.xlim(0, 50)
plt.xlabel('Prix')
plt.ylabel('Fréquence')
plt.title('Histogramme des prix livres enfants')
plt.show()

