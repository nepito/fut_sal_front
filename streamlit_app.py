import json
from pathlib import Path
from PIL import Image
import pandas as pd
import streamlit as st


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = current_dir / "static" / "fut_sal.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Fut Sal | NIES"
PAGE_ICON = "⚽"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
profile_pic = Image.open(profile_pic)
col1, _ = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)


f = open("tests/data/fixtures.json")
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

matches, table, stats = st.tabs(["Partidos", "Tabla", "Estadísticas"])

with matches:
    st.subheader("Partidos")
    for i in reversed(range(7)):
        write_a_match(i)
        """
        ---
        """

with table:
    st.subheader("Tabla general")
    """
    """
    st.dataframe(position, hide_index=True)

with stats:
    st.subheader("Estadísticas")
    """
    """
    st.dataframe(stats_players, hide_index=True)
    html_string = '<iframe width="450" height="800" src="https://lookerstudio.google.com/embed/reporting/d3f6cc9b-b30b-4732-b240-1a4241349bae/page/7ETwD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>'
    st.markdown(html_string, unsafe_allow_html=True)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
