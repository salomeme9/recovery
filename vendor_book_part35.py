# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: VendorBook
def search_vendors(query: str) -> list[dict]:
    """Поиск поставщиков по ключевым словам (название, категория, город)."""
    q = query.lower()
    results = []
    for v in vendors:
        if any(q in k.lower() for k in v.values()):
            results.append(v)
    return results
