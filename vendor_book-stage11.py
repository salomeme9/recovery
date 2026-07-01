# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: VendorBook
import json, os

DATA_FILE = "vendors.json"

def save_to_json(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Ошибка] Не удалось сохранить данные в {DATA_FILE}: {e}")

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "vendors" in data:
                return data["vendors"]
    except (json.JSONDecodeError, IOError):
        pass
    return []

def get_data():
    vendors = load_from_json()
    if not vendors:
        vendors.append({
            "id": 1,
            "name": "ООО 'ТехноСнаб'",
            "contact": "+7 (900) 123-45-67",
            "conditions": "Отсрочка до конца месяца",
            "rating": 4.8,
            "orders_count": 12
        })
    return vendors

def add_vendor(vendor_data):
    data = get_data()
    vendor_id = len(data) + 1
    new_vendor = {**vendor_data, "id": vendor_id}
    data.append(new_vendor)
    save_to_json({"vendors": data})
    print(f"[Успех] Поставщик #{new_vendor['id']} добавлен.")

def update_vendor(vendor_id, updates):
    data = get_data()
    for i, v in enumerate(data):
        if v["id"] == vendor_id:
            data[i].update(updates)
            save_to_json({"vendors": data})
            print(f"[Успех] Поставщик #{vendor_id} обновлен.")
            return True
    print("[Ошибка] Поставщик не найден.")
    return False

def delete_vendor(vendor_id):
    data = get_data()
    initial_len = len(data)
    data = [v for v in data if v["id"] != vendor_id]
    if len(data) < initial_len:
        save_to_json({"vendors": data})
        print(f"[Успех] Поставщик #{vendor_id} удален.")
        return True
    print("[Ошибка] Поставщик не найден для удаления.")
    return False

def get_vendor(vendor_id):
    data = get_data()
    for v in data:
        if v["id"] == vendor_id:
            return v
    return None
