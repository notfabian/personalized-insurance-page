import streamlit as st
import anthropic
import os

st.title('Personalisierte Versicherungsseite')

# Sidebar für Benutzereingaben
st.sidebar.header('Persönliche Informationen')

alter = st.sidebar.slider('Alter', 18, 100, 30)
geschlecht = st.sidebar.selectbox('Geschlecht', ['Männlich', 'Weiblich', 'Divers'])
ausbildung = st.sidebar.selectbox('Höchste Ausbildung', [
    'Obligatorische Schule',
    'Berufslehre',
    'Matura',
    'Hochschule/Universität'
])
hausbesitzer = st.sidebar.checkbox('Hausbesitzer')
familienstand = st.sidebar.selectbox('Familienstand', [
    'Ledig',
    'Verheiratet',
    'Geschieden',
    'Verwitwet'
])
haustiere = st.sidebar.checkbox('Haustiere')
hobbies = st.sidebar.multiselect('Hobbies', [
    'Sport',
    'Reisen',
    'Musik',
    'Kunst',
    'Gaming',
    'Lesen'
])

def get_personalized_content(user_data):
    client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    system_prompt = """Du bist Clara, der vertrauenswürdige Chatbot der Helvetia Versicherung. Halte dich an folgende Regeln:
    - Kommuniziere natürlich und verständlich
    - Nutze nur verifizierte Informationen
    - Biete relevante Self-Services an
    - Formatiere den Output als sauberes HTML mit korrekter Struktur"""
    
    user_prompt = f"""Erstelle eine personalisierte Versicherungsberatung für:
    Alter: {user_data['alter']}
    Geschlecht: {user_data['geschlecht']}
    Ausbildung: {user_data['ausbildung']}
    Hausbesitzer: {'Ja' if user_data['hausbesitzer'] else 'Nein'}
    Familienstand: {user_data['familienstand']}
    Haustiere: {'Ja' if user_data['haustiere'] else 'Nein'}
    Hobbies: {', '.join(user_data['hobbies'])}"""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        temperature=0.5,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    content = message.content[0].text
    return st.markdown(content, unsafe_allow_html=True)

# Button für Personalisierung
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
        get_personalized_content(user_data)
