# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: VendorBook
def search_suppliers(query: str) -> list[dict]:
    if not query.strip():
        return []
    q = query.lower()
    results = [s for s in suppliers.values() if any(q in str(v).lower() for v in s.values())]
    return sorted(results, key=lambda x: (x.get('rating', 0), x.get('order_count', 0)), reverse=True)
