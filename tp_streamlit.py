import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['species'] = iris.target

st.title("Tp Streamlit exploration des donnée Iris")

#création de menu dans la barre latérale
st.sidebar.title("Menu")
menu = st.sidebar.radio("Choisissez une option", ["Affichage des données", "Statistique", "Histogramme", "Pairplot"])

if menu == "Affichage des données":
    st.subheader("Tableau des donnés")
    st.write(df)
elif menu == "Statistiques":
    st.subheader("Statistiques descriptives")
    st.write(df.describe())

elif menu == "Histogramme":
    st.subheader("Histogrammes des caractéristiques")  

    feature = st.sidebar.selectbox("Sélectionnez la caractéristique", df.columns[:-1])  # Exclure 'species'
    

#Affichage des donnée
st.write("Aperçu des données:")
st.dataframe(df.head())

#Statistique des données
st.write("Résumé statistique des données:")
st.write(df.describe())

#Affichage histogramme
st.write("Histogramme des caractéristiques :")
st.bar_chart(df.iloc[:, :-1])

# Afficher un pairplot avec Seaborn
st.write("Pairplot des caractéristiques Iris :")

sns.pairplot(df, hue='species')
fig = plt.gcf()
st.pyplot(fig)