import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo de datos
data = pd.read_csv("train.csv")  # Cambiar al nombre correcto de tu archivo cargado

# Configurar Streamlit
st.set_page_config(layout="wide")
st.title("Análisis de Datos")

# Verificar y preparar las columnas necesarias
if 'Age' in data.columns and 'Fare' in data.columns and 'Survived' in data.columns:
    data['Survived'] = data['Survived'].replace({0: "No", 1: "Yes"})  # Codificar sobrevivencia
    data['Age'] = data['Age'].fillna(data['Age'].median())  # Rellenar edades faltantes

    # Filtros
    st.sidebar.header("Filtros")
    age_filter = st.sidebar.slider("Rango de Edad", int(data['Age'].min()), int(data['Age'].max()), (10, 60))
    survived_filter = st.sidebar.selectbox("Sobrevivió", options=["Todos", "Yes", "No"])
    class_filter = st.sidebar.multiselect(
        "Clase del Pasajero",
        options=data['Pclass'].unique(),
        default=data['Pclass'].unique()
    )

    # Aplicar filtros
    filtered_data = data[(data['Age'] >= age_filter[0]) & (data['Age'] <= age_filter[1])]
    if survived_filter != "Todos":
        filtered_data = filtered_data[filtered_data['Survived'] == survived_filter]
    if class_filter:
        filtered_data = filtered_data[filtered_data['Pclass'].isin(class_filter)]
else:
    st.error("Faltan columnas esenciales en los datos.")
    filtered_data = data.copy()

# Dividir en tres columnas para gráficos
col1, col2, col3 = st.columns(3)

# Gráfico 1: Dispersión (Age vs Fare)
with col1:
    st.subheader("Relación entre Edad y Tarifa")
    scatter_fig = px.scatter(
        filtered_data,
        x="Age",
        y="Fare",
        color="Survived",
        title="Edad vs. Tarifa (Segmentado por Supervivencia)",
        labels={"Age": "Edad", "Fare": "Tarifa"},
        hover_data=["Pclass"]
    )
    st.plotly_chart(scatter_fig, use_container_width=True)

# Gráfico 2: Distribución de Edad
with col2:
    st.subheader("Distribución de Edad")
    hist_fig = px.histogram(
        filtered_data,
        x="Age",
        color="Survived",
        nbins=20,
        title="Distribución de Edad por Supervivencia",
        labels={"Age": "Edad", "Survived": "Sobrevivió"}
    )
    st.plotly_chart(hist_fig, use_container_width=True)

# Gráfico 3: Distribución de Pasajeros por Clase
with col3:
    st.subheader("Distribución de Pasajeros por Clase")
    bar_fig = px.bar(
        filtered_data,
        x="Pclass",
        color="Survived",
        title="Distribución de Pasajeros por Clase y Supervivencia",
        labels={"Pclass": "Clase", "Survived": "Sobrevivió"}
    )
    st.plotly_chart(bar_fig, use_container_width=True)

# Gráfico 4: Matriz de Correlación
st.subheader("Matriz de Correlación")
numeric_cols = filtered_data.select_dtypes(include=['float64', 'int64'])
if not numeric_cols.empty:
    correlation_matrix = numeric_cols.corr()
    corr_fig = px.imshow(
        correlation_matrix,
        title="Matriz de Correlación",
        labels=dict(color="Correlación"),
        color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1
    )
    st.plotly_chart(corr_fig, use_container_width=True)
else:
    st.write("No hay datos numéricos disponibles para generar la matriz de correlación.")

# Gráfico 5: Distribución de Tarifas por Clase
st.subheader("Distribución de Tarifas por Clase de Pasajero")
box_fig = px.box(
    filtered_data,
    x="Pclass",
    y="Fare",
    color="Pclass",
    title="Distribución de Tarifas por Clase",
    labels={"Pclass": "Clase", "Fare": "Tarifa"}
)
st.plotly_chart(box_fig, use_container_width=True)