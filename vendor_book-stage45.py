# === Stage 45: Добавь восстановление из резервной копии ===
# Project: VendorBook
def restore_from_backup(file_path, backup_path):
    """Restore VendorBook state from a backup file."""
    if not backup_path or not backup_path.endswith('.json'):
        print("Неверный путь к резервной копии.")
        return False
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Резервная копия восстановлена из {backup_path}")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
