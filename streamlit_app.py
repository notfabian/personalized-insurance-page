import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Seitenkonfiguration
st.set_page_config(page_title="Personalisierte Versicherungsseite", layout="wide")

# Sidebar für Benutzereingaben
st.sidebar.header("Persönliche Angaben")
alter = st.sidebar.slider("Alter", 18, 80, 30)
geschlecht = st.sidebar.selectbox("Geschlecht", ["männlich", "weiblich", "divers"])
ausbildung = st.sidebar.selectbox("Ausbildung", ["Lehre", "Matura", "Hochschule"])
hausbesitzer = st.sidebar.checkbox("Hausbesitzer")
familienstand = st.sidebar.selectbox("Familienstand", ["ledig", "verheiratet", "geschieden", "verwitwet"])
haustiere = st.sidebar.checkbox("Haustiere")
hobbies = st.sidebar.multiselect("Hobbies", ["Sport", "Reisen", "Musik", "Kunst", "Gaming", "Outdoor"])

# Hauptbereich
st.title("Ihre personalisierte Versicherungslösung")

# Hier kommt später der Claude-API-Call
