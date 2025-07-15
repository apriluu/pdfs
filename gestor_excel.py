import pandas as pd
import os

EXCEL_PATH = "resultats_projectes.xlsx"


def afegir_a_excel(dades_json):
    try:
        dades_json = {k.lower().strip(): v for k, v in dades_json.items()}

        fila = {
            "Nom del projecte": dades_json.get("nom del projecte"),
            "Ubicació": dades_json.get("ubicació"),
            "Pressupost de licitació (PEM)": dades_json.get("pressupost de licitació (PEM)"),
            "Data de licitació": dades_json.get("data de licitació"),
            "Termini d'execució": dades_json.get("termini d'execució"),
            "Requisits legals o tècnics destacats": dades_json.get("requisits legals o tècnics destacats"),
            "Perfils tècnics requerits": "\n".join(
                [str(p) for p in dades_json.get("perfils tècnics requerits", [])]
            )
        }

        nova_fila = pd.DataFrame([fila])

        if os.path.exists(EXCEL_PATH):
            df = pd.read_excel(EXCEL_PATH)
            df = pd.concat([df, nova_fila], ignore_index=True)
        else:
            df = nova_fila

        df.to_excel(EXCEL_PATH, index=False)
        print(f"✅ Fila afegida correctament a '{EXCEL_PATH}'")

    except Exception as e:
        print(f"❌ Error afegint dades a Excel: {e}")

