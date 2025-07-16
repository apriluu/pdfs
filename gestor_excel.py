import pandas as pd
import os

def afegir_a_excel(json_data, fitxer="base_dades.xlsx"):
    nou = pd.DataFrame([json_data])
    if os.path.exists(fitxer):
        existent = pd.read_excel(fitxer)
        actualitzat = pd.concat([existent, nou], ignore_index=True)
    else:
        actualitzat = nou
    actualitzat.to_excel(fitxer, index=False)
