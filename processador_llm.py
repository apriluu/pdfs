from llama_cpp import Llama
import json

# Inicia el model (només una vegada)
llm = Llama(model_path="./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=4096)

# Instrucció base (el que tu li vols demanar sempre al model)
PROMPT_BASE = """
Extreu del text següent les dades en format JSON amb els camps següents:

- nom del projecte
- ubicació
- pressupost de licitació (PEM)
- data de licitació
- perfils tècnics requerits (amb titulació, anys d’experiència i funcions)
- termini d'execució
- requisits legals o tècnics destacats

Si alguna dada no hi és, posa null. No afegeixis cap explicació ni cap text addicional.
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

        resposta = llm(prompt, max_tokens=800, stop=["</s>"], echo=False)
        try:
            json_resultat = json.loads(resposta["choices"][0]["text"].strip())

            # Fusionem la info
            for clau in dades_totals:
                if dades_totals[clau] is None and json_resultat.get(clau):
                    dades_totals[clau] = json_resultat[clau]
                elif isinstance(dades_totals[clau], list):
                    dades_totals[clau].extend(json_resultat.get(clau, []))

        except Exception as e:
            print(f"⚠️ Error en chunk {i+1}: {e}")
            continue

    return dades_totals
