import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import init_db, load_csv_to_db
from utils.visualizations import render_dashboard

st.title("Mlops Project")

conn = init_db()

uploaded_file = st.file_uploader("Téléverser un fichier CSV", type="csv")

if uploaded_file:
    df = load_csv_to_db(conn, uploaded_file)

    st.success("Fichier chargé avec succès !")

       # 👇 AJOUT IMPORTANT
    render_dashboard(conn)
