from turtle import st

from llama_cpp import Llama
import json
import re

from mistral_local import demanar_json_a_model

# Inicia el model (només una vegada)
llm = Llama(model_path="./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=4096)

# Instrucció base (el que tu li vols demanar sempre al model)
PROMPT_BASE =PROMPT = """
Extreu del text següent les dades en format estrictament JSON amb els camps següents:
- nom del projecte
- ubicació
- pressupost de licitació (PEM)
- data de licitació
- perfils tècnics requerits (amb titulació, anys d’experiència i funcions)
- termini d'execució
- requisits legals o tècnics destacats

No afegeixis cap explicació, frase ni títol. Respon només amb JSON sense cap línia extra.

TEXT:
\"\"\"
{chunk}
\"\"\"
"""


def processar_chunks(chunks):
    dades_totals = {
        "nom del projecte": None,
        "ubicació": None,
        "pressupost de licitació (PEM)": None,
        "data de licitació": None,
        "perfils tècnics requerits": [],
        "termini d'execució": None,
        "requisits legals o tècnics destacats": None
    }

    for i, chunk in enumerate(chunks):
        prompt = f"{PROMPT_BASE}\n\nText:\n{chunk}"
        print(f"🔍 Processant chunk {i+1}/{len(chunks)}...")

        resposta = demanar_json_a_model(chunk)
        json_net = extreure_json(resposta)

        try:
            dades = json.loads(json_net)
            # Fusionem la info
            for clau in dades_totals:
                if dades_totals[clau] is None and dades.get(clau):
                    dades_totals[clau] = dades[clau]
                    st.code(resposta, language="json")
                elif isinstance(dades_totals[clau], list):
                    dades_totals[clau].extend(dades.get(clau, []))

        except Exception as e:
            print(f"⚠️ Error en chunk {i+1}: {e}")
            continue

    return dades_totals

def extreure_json(text_llm):
    """
    Troba i retorna només el bloc JSON dins del text generat pel model.
    """
    match = re.search(r"\{.*\}", text_llm, re.DOTALL)
    if match:
        return match.group(0)
    else:
        return None
