import streamlit as st
import json
from gestor_excel import afegir_a_excel

st.set_page_config(page_title="Importador de projectes", layout="centered")
st.title("📥 Importador de dades de projectes")

st.markdown("""
Copia aquí el **JSON** que t’ha generat el GPT personalitzat després d’analitzar el PDF del projecte.
""")

input_json = st.text_area("📋 Enganxa el JSON aquí", height=300)

if st.button("✅ Validar i desar"):
    try:
        dades = json.loads(input_json)
        afegir_a_excel(dades)
        st.success("✅ Dades desades correctament a `base_dades.xlsx`")
        st.write("Dades registrades:")
        st.json(dades)
    except Exception as e:
        st.error(f"⚠️ Error: el contingut no és un JSON vàlid.\n\n{str(e)}")
