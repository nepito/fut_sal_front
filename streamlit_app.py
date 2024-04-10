import pandas as pd
import streamlit as st
import json

f = open('tests/data/fixtures.json')
data = json.load(f)

fixtures = data["response"]
position = pd.read_csv("tests/data/tabla_general.csv")
stats_players = pd.read_csv("tests/data/estadistica.csv")
data = pd.read_csv("static/played_minutes.csv")
# ----------------- game start --------
def write_a_match(index_of_match):
    home = f"{fixtures[index_of_match]['teams']['home']['name']}:  {fixtures[index_of_match]['goals']['home']}"
    away = f"{fixtures[index_of_match]['teams']['away']['name']}:  {fixtures[index_of_match]['goals']['away']}"
    st.write(home)
    st.write(away)
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

with stats:
    st.subheader("Estadística")
    """
    """
    st.dataframe(stats_players, hide_index = True)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
