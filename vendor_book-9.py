# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: VendorBook
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

    if not isinstance(data, dict):
        raise ValueError("JSON должен содержать объект (словарь), а не массив или скаляр.")

    required_keys = ["suppliers", "orders"]
    missing = [k for k in required_keys if k not in data]
    if missing:
        raise KeyError(f"Отсутствуют обязательные ключи: {', '.join(missing)}")

    # Валидация структуры поставщиков
    suppliers = {}
    for idx, supplier in enumerate(data.get("suppliers", [])):
        if not isinstance(supplier, dict):
            print(f"Предупреждение: Игнорирую запись поставщика {idx}, так как это не словарь.")
            continue
        name = supplier.get("name")
        if not name:
            print(f"Предупреждение: Поставщик без имени на позиции {idx} игнорируется.")
            continue
        suppliers[name] = supplier

    # Валидация структуры заказов и привязка к поставщикам
    orders = []
    for idx, order in enumerate(data.get("orders", [])):
        if not isinstance(order, dict):
            print(f"Предупреждение: Игнорирую запись заказа {idx}, так как это не словарь.")
            continue
        supplier_name = order.get("supplier")
        if supplier_name and supplier_name in suppliers:
            orders.append({**order, "_valid": True})
        else:
            print(f"Предупреждение: Заказ привязан к несуществующему поставщику '{supplier_name}'.")

    return {
        "suppliers": list(suppliers.values()),
        "orders": [o for o in orders if o.get("_valid", False)],
        "_meta": {"loaded_from": "string"}
    }
