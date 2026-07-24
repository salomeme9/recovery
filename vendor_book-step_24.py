# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: VendorBook
def print_vendor_summary(vendor: Vendor) -> None:
    """Компактный вывод одной записи поставщика."""
    print(f"=== Поставщик: {vendor.name} ===")
    print(f"  Контакты: {', '.join(vendor.contacts.keys())}")
    for k, v in vendor.contacts.items():
        print(f"    {k}: {v}")
    print(f"  Условия: {vendor.conditions}")
    print(f"  Заказы: {len(vendor.orders)}")
    if vendor.orders:
        total = sum(o.total for o in vendor.orders)
        print(f"    Всего потрачено: {total:.2f} €")
    print(f"  Рейтинг: {vendor.rating}/5")
