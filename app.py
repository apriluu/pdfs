import streamlit as st
from extractor_pdf import extreure_text_del_pdf
from utils import split_text
from gestor_excel import afegir_a_excel
from mistral_local import demanar_json_a_model
import json

st.set_page_config(page_title="Extractor de Projectes", layout="centered")

st.title("📄 Extracció de dades de projectes de licitació")
st.markdown("Penja un PDF i et generarem automàticament el resum en format Excel.")

# Penjar PDF
pdf_file = st.file_uploader("📎 Penja el PDF de la licitació", type=["pdf"])

if pdf_file:
    st.info("📖 Llegint el contingut del PDF...")
    text = extreure_text_del_pdf(pdf_file)
    if not text.strip():
        st.error("❌ El PDF no conté text o no s’ha pogut llegir.")
        st.stop()

    st.success("✅ PDF llegit correctament. Analitzant contingut...")

    # Dividim en chunks
    chunks = split_text(text)

    # Mostrem previsualització
    with st.expander("🔍 Visualitza text extret"):
        st.text_area("Text complet", text, height=300)

    # Processem cada chunk amb el model local
    resultat_final = {}
    for chunk in chunks:
        resposta = demanar_json_a_model(chunk)

        try:
            dades = json.loads(resposta)
            resultat_final.update({k: dades.get(k) for k in dades})
        except Exception as e:
            st.warning(f"⚠️ Error en interpretar resposta parcial: {e}")

    if resultat_final:
        # Mostrem resultat
        st.subheader("📋 Resultat obtingut:")
        st.json(resultat_final)

        # Guardem a Excel
        afegir_a_excel(resultat_final)
        st.success("✅ Dades guardades correctament a l’Excel!")
        st.download_button("📥 Descarrega Excel", data=open("resultats_projectes.xlsx", "rb").read(),
                           file_name="resultats_projectes.xlsx")

    else:
        st.error("❌ No s’ha pogut extreure informació del PDF.")
