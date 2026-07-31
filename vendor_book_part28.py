# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: VendorBook
def print_metrics():
    total_vendors = len(vendor_list)
    active_orders = sum(1 for v in vendor_list for o in v.orders.values() if not o['done'])
    total_rating = sum(sum(o.get('rating', 0) for o in v.orders.values()) for v in vendor_list)
    avg_rating = (total_rating / (active_orders * len(vendor_list))) if active_orders else 0
    print(f"Поставщиков: {total_vendors}")
    print(f"Активных заказов: {active_orders}")
    print(f"Средний рейтинг: {avg_rating:.1f}/5")

if __name__ == "__main__":
    vendor_list = []
    with open("vendorbook.py", "r") as f:
        source = f.read()
    
    if 'def add_vendor' in source and 'print_metrics' not in source:
        exec(source)
        print_metrics()
