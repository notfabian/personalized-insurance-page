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

# Claude Integration
def get_personalized_content(user_data):
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    prompt = f"""Du bist ein Versicherungsberater der Helvetia. Erstelle eine personalisierte Produktseite für folgende Person:

    Alter: {user_data['alter']}
    Geschlecht: {user_data['geschlecht']}
    Ausbildung: {user_data['ausbildung']}
    Hausbesitzer: {'Ja' if user_data['hausbesitzer'] else 'Nein'}
    Familienstand: {user_data['familienstand']}
    Haustiere: {'Ja' if user_data['haustiere'] else 'Nein'}
    Hobbies: {', '.join(user_data['hobbies'])}

    Wichtige Vorgaben:
    - Formatiere deinen Output als sauberes HTML mit <div>, <h2>, <p> Tags.
    - Nutze nur verifizierte, faktisch korrekte Versicherungsinformationen
    - Kommuniziere im professionellen, vertrauenswürdigen Helvetia-Stil
    - Biete konkrete Self-Service Optionen an
    - Vermeide Halluzinationen oder ungeprüfte Aussagen
    - Strukturiere die Ausgabe mit HTML für bessere Lesbarkeit
    - Personalisiere die Empfehlungen basierend auf der Lebenssituation
    """

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0.5,  # Reduziert für höhere Faktentreue
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Saubere Extraktion des Texts
    content = message.content[0].text if isinstance(message.content[0].text, str) else str(message.content[0])
    
    # Streamlit erwartet standardmäßig Markdown
    return content.strip()

# Personalisierte Inhalte generieren und anzeigen
if st.sidebar.button('Inhalte personalisieren'):
    user_data = {
        'alter': alter,
        'geschlecht': geschlecht,
        'ausbildung': ausbildung,
        'hausbesitzer': hausbesitzer,
        'familienstand': familienstand,
        'haustiere': haustiere,
        'hobbies': hobbies
    }
    
    with st.spinner('Personalisiere Inhalte...'):
        content = get_personalized_content(user_data)
        st.markdown(content, unsafe_allow_html=True)
