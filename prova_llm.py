from llm_loader import pregunta_al_model

prompt = """Extreu les següents dades del text següent:
- Nom del projecte
- Ubicació
- Pressupost sense IVA
- Termini d'execució

Text: El projecte preveu la reforma del Centre de Convencions CC2 al recinte de Fira de Barcelona. Està situat al carrer Botànica, 62, L'Hospitalet. El pressupost base és de 220.000 euros sense IVA. El termini estimat d'execució és de 40 setmanes."""

resposta = pregunta_al_model(prompt)
print("\n🧠 Resposta del model:\n")
print(resposta)
