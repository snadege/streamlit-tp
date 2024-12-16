import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titre de l'application
st.title('Analyse des Données Iris')

# Affichage de la description
st.markdown("""
Streamlit est un framework open source en Python qui simplifie la création d'applications web interactives pour la visualisation et l'analyse de données.

Dans ce projet, nous utilisons la base de données Iris pour créer des visualisations interactives. 
""")

# Charger les données Iris
iris = sns.load_dataset('iris')

# Afficher les premières lignes du DataFrame
st.subheader('Aperçu des données Iris')
st.write(iris.head())

# Afficher la description des données
st.subheader('Statistiques descriptives')
st.write(iris.describe())

# Créer un graphique de dispersion des différentes variables
st.subheader('Graphique de dispersion')
sns.pairplot(iris, hue='species')
st.pyplot()

# Ajouter une option de filtrage pour afficher les données par espèce
species = st.selectbox('Choisissez l\'espèce', iris['species'].unique())
filtered_data = iris[iris['species'] == species]
st.write(f"Les données pour l'espèce: {species}")
st.write(filtered_data)

# Ajouter des informations supplémentaires sur les colonnes
st.subheader('Description des colonnes')
st.markdown("""
- **sepal_length**: Longueur du sépale en cm
- **sepal_width**: Largeur du sépale en cm
- **petal_length**: Longueur du pétale en cm
- **petal_width**: Largeur du pétale en cm
- **species**: Espèce de la fleur (setosa, versicolor, virginica)
""")

# Déployer un graphique supplémentaire en fonction de l'espèce choisie
st.subheader(f'Graphique de la longueur des sépales pour {species}')
sns.boxplot(x='species', y='sepal_length', data=iris)
st.pyplot()
