# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: VendorBook
class Vendor:
    def __init__(self, name: str, email: str, rating: float = 0.0):
        self.name = name.strip() if name else "Unknown"
        self.email = email.lower().strip() if email else ""
        self.rating = max(0.0, min(5.0, round(float(rating), 1)))

    def validate(self) -> bool:
        return "@" in self.email and "." in self.email.split("@")[-1] and len(self.name) > 2


def parse_order_line(line: str) -> dict | None:
    parts = line.strip().split(";")
    if len(parts) != 3 or not all(p for p in parts):
        return None
    try:
        item, qty, price = parts
        return {"item": item.strip(), "qty": int(qty), "price": float(price)}
    except ValueError:
        return None
