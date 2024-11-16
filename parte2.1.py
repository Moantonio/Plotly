import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Cargar los datos
data = pd.read_csv("cleaned_data.csv")

# Crear un gráfico interactivo (scatter plot como ejemplo)
fig = go.Figure()

# Agregar datos al scatter plot
fig.add_trace(go.Scatter(
    x=data["Age"], 
    y=data["Fare"], 
    mode="markers",
    marker=dict(
        size=10,
        color=data["Survived"],  # Usar la columna 'Survived' para asignar colores
        colorscale="Viridis",    # Escala de colores
        showscale=True           # Mostrar barra de escala
    ),
    text=data["Pclass"],         # Mostrar 'Pclass' al pasar el cursor
    name="Edad vs Tarifa"
))

# Configurar el título y etiquetas
fig.update_layout(
    title="Scatter Plot: Age vs Fare",
    xaxis_title="Age",
    yaxis_title="Fare",
    legend_title="Survived",
    hovermode="closest"
)

# Desplegar en Streamlit
st.title("Visualización Interactiva con Plotly (go)")
st.plotly_chart(fig)