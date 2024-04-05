import pandas as pd
import streamlit as st
import json

f = open('tests/data/fixtures.json')
data = json.load(f)

fixtures = data["response"]
position = pd.read_csv("tests/data/tabla_general.csv")
data = pd.read_csv("static/played_minutes.csv")
# ----------------- game start --------
def write_a_match(index_of_match):
    col2, col3 = st.columns([2, 1])
    with col2:
        st.write(fixtures[index_of_match]["teams"]["home"]["name"])
        st.write(fixtures[index_of_match]["teams"]["away"]["name"])
    with col3:
        st.write(fixtures[index_of_match]["goals"]["home"])
        st.write(fixtures[index_of_match]["goals"]["away"])
# ---------------------------------------

matches, table, stats, player = st.tabs(["Partidos", "Tabla", "Estadísticas", "Jugadores"])

with matches:
    st.subheader("Partidos")
    """
    """
    write_a_match(0)
    """
    ---
    """
    write_a_match(1)
    """
    ---
    """
    write_a_match(2)
    """
    ---
    """
    write_a_match(3)

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
