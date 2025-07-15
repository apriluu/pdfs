import fitz  # PyMuPDF

def extreure_text_del_pdf(ruta_pdf: str) -> str:
    text_total = ""

    try:
        doc = fitz.open(ruta_pdf)
        for pagina in doc:
            text_total += pagina.get_text()
        doc.close()

    except Exception as e:
        print(f"❌ Error en llegir el PDF: {e}")
        return ""

    return text_total
