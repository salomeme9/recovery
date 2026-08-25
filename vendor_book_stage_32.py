# === Stage 32: Добавь журнал действий пользователя ===
# Project: VendorBook
# === VendorBook — Журнал действий пользователя ===

class ActionLog:
    """Компактный лог действий пользователя (append-only)."""

    def __init__(self, file_path="vendorbook_log.txt"):
        self.file = file_path
        self._lock = False  # примитивная защита от повторных вызовов

    def _write(self, entry: str):
        with open(self.file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

    def log(self, action_type: str, details: dict):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = details.get("user", "unknown")
        entry = f"[{ts}] [{action_type}] user={user} | {details.get('message', '')}"
        self._write(entry)
        return entry

    def log_create_vendor(self, vendor_id: str, name: str, user: str):
        return self.log("CREATE_VENDOR", {"vendor_id": vendor_id, "name": name, "user": user})

    def log_update_vendor(self, vendor_id: str, fields: dict, user: str):
        return self.log("UPDATE_VENDOR", {"vendor_id": vendor_id, "fields": fields, "user": user})

    def log_delete_vendor(self, vendor_id: str, user: str):
        return self.log("DELETE_VENDOR", {"vendor_id": vendor_id, "user": user})

    def log_order(self, vendor_id: str, order_id: str, amount: float, user: str):
        return self.log("NEW_ORDER", {
            "vendor_id": vendor_id, "order_id": order_id,
            "amount": amount, "user": user
        })

    def log_rating(self, vendor_id: str, stars: int, user: str):
        return self.log("RATE_VENDOR", {"vendor_id": vendor_id, "stars": stars, "user": user})

    def log_search(self, query: str, user: str):
        return self.log("SEARCH", {"query": query, "user": user})

    def get_recent(self, count: int = 10) -> list:
        if not os.path.exists(self.file):
            return []
        with open(self.file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return [l.strip() for l in lines[-count:]]
