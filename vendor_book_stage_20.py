# === Stage 20: Добавь восстановление записей из архива ===
# Project: VendorBook
class RecoveryManager:
    """Restores vendor records from an archived JSON file."""

    @staticmethod
    def load_from_archive(filepath):
        """Reads the archive and returns a list of restored record dicts."""
        try:
            import json
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, dict) and 'records' in data:
                return data['records']
            elif isinstance(data, list):
                return data
            else:
                raise ValueError("Archive must contain a list or {'records': [...]}.")
        except FileNotFoundError:
            print(f"[Recovery] Archive not found: {filepath}")
            return []

    @staticmethod
    def merge_into_db(records, db_path=None):
        """Appends restored records to an existing DB file (JSON)."""
        import json
        if db_path is None:
            db_path = 'vendor_book.json'
        try:
            with open(db_path, 'r', encoding='utf-8') as f:
                current = json.load(f)
            if isinstance(current, dict):
                existing = current.get('records', [])
            else:
                existing = []
            merged = existing + records
            with open(db_path, 'w', encoding='utf-8') as f:
                json.dump({'records': merged}, f, indent=2, ensure_ascii=False)
            print(f"[Recovery] Merged {len(records)} records into {db_path}")
        except Exception as e:
            print(f"[Recovery] Error merging: {e}")
