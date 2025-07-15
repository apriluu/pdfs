from llama_cpp import Llama

# Carrega el model un cop i el manté en memòria
llm = Llama(model_path="./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=4096, n_threads=8)

# Instrucció fixa per extreure informació en JSON
prompt_fixe = """
Extreu del text següent les següents dades i retorna-les en format JSON estructurat:
- nom del projecte
- ubicació
- pressupost de licitació (PEM), encara que estigui dins d'una taula o expressat com "Import base de licitació", "PEM sense IVA" o similar
- data de licitació
- perfils tècnics requerits (amb titulació, anys d’experiència i funcions)
- termini d'execució si està indicat
- requisits legals o tècnics destacats

El format de sortida ha de ser estrictament JSON. Si alguna dada no hi és, posa null. No afegeixis explicacions, només el JSON.

TEXT:
"""

def demanar_json_a_model(text_pdf: str) -> str:
    prompt = prompt_fixe + text_pdf.strip()

    resposta = llm(
        prompt=prompt,
        max_tokens=1024,
        stop=["</s>"],
        temperature=0.1,
        echo=False
    )

    return resposta["choices"][0]["text"].strip()
