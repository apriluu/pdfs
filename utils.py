def split_text(text, max_chars=2000, overlap=200):
    """
    Divideix el text llarg en fragments més petits amb sobreposició opcional.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + max_chars, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += max_chars - overlap

    print(f"🔍 Text dividit en {len(chunks)} fragments.")
    return chunks
