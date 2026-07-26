# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: VendorBook
def parse_date(date_str):
    """Парсит дату в формате ДД.ММ.ГГГГ, возвращает datetime или None."""
    if not isinstance(date_str, str) or len(date_str.strip()) < 3:
        return None
    try:
        parts = date_str.strip().split(".")
        if len(parts) != 3:
            return None
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 9999):
            return None
        from datetime import date as dt_date
        return dt_date(year, month, day)
    except Exception:
        return None

def format_error(msg):
    """Формирует понятное сообщение об ошибке."""
    print(f"[Ошибка] {msg}")
