# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: VendorBook
import json, os

def load_suppliers_from_file(file_path: str) -> list[dict]:
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "suppliers" in data:
            print("Предупреждение: файл содержит объект вместо списка. Используется поле 'suppliers'.")
            return data.get("suppliers", [])
        else:
            print(f"Ошибка формата JSON в {file_path}: ожидается список или объект с ключом 'suppliers'.")
            return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON из {file_path}: {e}")
        return []
    except PermissionError:
        print(f"Нет прав доступа к чтению файла {file_path}.")
        return []
