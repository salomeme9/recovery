# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: VendorBook
import json, os, random
from dataclasses import asdict
from datetime import date, timedelta

DATA_FILE = "vendors.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"suppliers": [], "orders": []}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"suppliers": [], "orders": []}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True) if os.path.dirname(DATA_FILE) else None
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_demo_data():
    suppliers = [
        {"id": 1, "name": "TechSupply Co.", "contact": "+7 (900) 123-45-67", "rating": 4.8},
        {"id": 2, "name": "Global Parts Ltd.", "contact": "+7 (900) 987-65-43", "rating": 4.5}
    ]
    orders = [
        {"id": 101, "supplier_id": 1, "amount": 15000, "status": "completed"},
        {"id": 102, "supplier_id": 2, "amount": 8500, "status": "pending"}
    ]
    return {"suppliers": suppliers, "orders": orders}

def main():
    data = load_data()
    if not data["suppliers"]:
        print("Инициализация демо-данных...")
        demo = generate_demo_data()
        data.update(demo)
        save_data(data)
        print(f"Демо-записи добавлены: {len(data['suppliers'])} поставщиков, {len(data['orders'])} заказов.")

if __name__ == "__main__":
    main()
