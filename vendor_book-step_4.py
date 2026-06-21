# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: VendorBook
def edit_vendor(vendor_id, updates):
    if vendor_id not in vendors:
        raise ValueError(f"Поставщик с id {vendor_id} не найден")
    for key, value in updates.items():
        if key in ['id', 'orders']: continue
        vendors[vendor_id][key] = value
