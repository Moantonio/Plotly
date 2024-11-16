import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
data = pd.read_csv("train.csv") 

# Crear un gráfico interactivo (scatter plot como ejemplo)
fig = px.scatter(data, x="Age", y="Fare", color="Survived",
                 title="Scatter Plot: Age vs Fare",
                 labels={"Age": "Age", "Fare": "Fare", "Survived": "Survived"},
                 hover_data=["Pclass"])

# Desplegar en Streamlit
st.title("Grafico con Plotly")
st.plotly_chart(fig)