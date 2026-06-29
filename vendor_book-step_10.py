# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: VendorBook
def export_to_json():
    import json
    data = {
        "suppliers": suppliers,
        "orders": orders,
        "ratings": ratings,
        "metadata": {"version": 10, "timestamp": datetime.now().isoformat()}
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
