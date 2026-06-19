# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: VendorBook
class VendorBook:
    def __init__(self):
        self._vendors = {}
    
    def add_vendor(self, name: str, contact: str, conditions: dict, rating: float) -> None:
        if not 0 <= rating <= 5.0:
            raise ValueError("Рейтинг должен быть от 0 до 5")
        self._vendors[name] = {
            "contact": contact,
            "conditions": conditions,
            "rating": rating,
            "orders": []
        }

    def get_vendor(self, name: str) -> dict | None:
        return self._vendors.get(name)
