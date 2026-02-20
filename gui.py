import streamlit as st
from dal import DataAccessLayer
from bll import BusinessLogicLayer

# App Konfiguration
st.set_page_config(page_title="Ferienhaus Manager", layout="wide")

# 2. HIER DEIN CSS: Versteckt Header, Footer und Menü für einen "Clean Look"
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none;} 
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# Initialisierung der Logik im SessionState (LocalStorage-Ersatz)
if 'bll' not in st.session_state:
    st.session_state.bll = BusinessLogicLayer(DataAccessLayer())

bll = st.session_state.bll

st.title("🏡 Luxus Ferienhaus Manager")
st.markdown("---")

# Sidebar für neue Einträge
with st.sidebar:
    st.header("➕ Neues Haus")
    with st.form("add_form", clear_on_submit=True):
        hid = st.text_input("Haus-ID")
        n = st.text_input("Name")
        o = st.text_input("Ort")
        p = st.number_input("Preis/Nacht", min_value=0.0)
        k = st.number_input("Personen", min_value=1)
        if st.form_submit_button("Anlegen"):
            ok, msg = bll.haus_erstellen(hid, n, o, p, k)
            st.info(msg)
            st.rerun()

# Hauptbereich: Anzeige der Häuser
tabs = st.tabs(["🏠 Verfügbare Häuser", "📑 Buchungs-Status"])

with tabs[0]:
    freie = bll.hole_freie_haeuser()
    if not freie:
        st.warning("Keine freien Häuser gefunden.")
    else:
        cols = st.columns(3)
        for idx, h in enumerate(freie):
            with cols[idx % 3]:
                # Zufälliges Hausbild basierend auf der ID
                img = f"https://loremflickr.com{h['id']}"
                st.image(img, use_container_width=True)
                st.subheader(h['name'])
                st.write(f"📍 {h['ort']} | 💶 {h['preis_pro_nacht']}€")
                if st.button(f"Buchen: {h['id']}", key=f"book_{h['id']}"):
                    bll.buchen(h['id'])
                    st.success("Gebucht!")
                    st.rerun()

with tabs[1]:
    st.subheader("Alle Häuser verwalten")
    for h in bll.dal.alle_auflisten():
        status = "✅ Frei" if h['verfuegbarkeit'] else "❌ Belegt"
        c1, c2, c3 = st.columns([2, 1, 1])
        c1.write(f"**{h['name']}** ({h['id']})")
        c2.write(status)
        if not h['verfuegbarkeit']:
            if c3.button("Stornieren", key=f"storno_{h['id']}"):
                bll.stornieren(h['id'])
                st.rerun()
