import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV  en spécifiant les colonnes pertinentes
donnees = pd.read_csv('RTE_2020.csv', delimiter=',',  usecols=['Fioul', 'Charbon', 'Gaz', 'Nucleaire', 'Eolien', 'Solaire', 'Hydraulique',  'Bioenergies'])

# Remplacer les valeurs manquantes par des zéros et convertir les données en entiers
donnees = donnees.fillna(0)
donnees = donnees.astype(int)

# Calculer la somme de chaque type d'énergie
sommes_par_energie = {source: donnees[source].sum() for source in donnees.columns}

# Création du premier graphique pour la part des énergies par source
labels = list(sommes_par_energie.keys())
tailles = list(sommes_par_energie.values())

plt.subplot(1, 2, 1)
plt.pie(tailles, labels=labels, autopct='%1.1f%%')
plt.title('Répartition des différentes sources d\'énergie')

# Calcul du pourcentage d'énergie renouvelable dans la production totale
non_renouvelable = donnees.iloc[:, :4].sum().sum()
renouvelable = donnees.iloc[:, 4:].sum().sum()
production_totale = non_renouvelable + renouvelable

pourcentage_renouvelable = (renouvelable / production_totale) * 100 if production_totale != 0 else 0
tailles_renouvelable = [pourcentage_renouvelable, 100 - pourcentage_renouvelable]

plt.subplot(1, 2, 2)
plt.pie(tailles_renouvelable, labels=['Renouvelable', 'Non Renouvelable'], autopct='%1.1f%%')
plt.title('Pourcentage de l\'énergie renouvelable dans la production totale')

plt.tight_layout()
plt.show()
