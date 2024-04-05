import pandas as pd
import streamlit as st
import json

f = open('tests/data/fixtures.json')
data = json.load(f)

fixtures = data["response"]
position = pd.read_csv("tests/data/tabla_general.csv")
data = pd.read_csv("static/played_minutes.csv")
# ----------------- game start --------
radar_player = "J. Musiala"

matches, table, stats, player = st.tabs(["Partidos", "Tabla", "Estadísticas", "Jugadores"])

with matches:
    st.subheader("Partidos")
    """
    """
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.write(fixtures[0]["teams"]["home"]["name"])
        st.write(fixtures[0]["teams"]["away"]["name"])
    with col3:
        st.write(fixtures[0]["goals"]["home"])
        st.write(fixtures[0]["goals"]["away"])
    """
    ---
    """
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.write(fixtures[1]["teams"]["home"]["name"])
        st.write(fixtures[1]["teams"]["away"]["name"])
    with col3:
        st.write(fixtures[1]["goals"]["home"])
        st.write(fixtures[1]["goals"]["away"])

with table:
    st.subheader("Tabla general")
    """
    """
    st.dataframe(position, hide_index = True)

with player:
    st.subheader("Gráficas de desempeño")
    """
    """

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
