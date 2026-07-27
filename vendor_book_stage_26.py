# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: VendorBook
def demo_run():
    print("=== VendorBook Demo ===")
    vendors = list(get_all_vendors())
    orders = list(get_orders())
    ratings = get_ratings_summary()
    print(f"Всего поставщиков: {len(vendors)}")
    print(f"Всего заказов: {len(orders)}")
    print(f"\nТоп-3 по рейтингу:")
    for i, (vendor_id, score) in enumerate(ratings[:3], 1):
        name = next((v["name"] for v in vendors if v["id"] == vendor_id), "Не найден")
        print(f"  {i}. {name} — рейтинг: {score}")

    top_orders = sorted(orders, key=lambda o: -o.get("total_amount", 0))[:3]
    print(f"\nТоп-3 заказа по сумме:")
    for i, order in enumerate(top_orders, 1):
        vendor_name = next((v["name"] for v in vendors if v["id"] == order.get("vendor_id")), "?")
        print(f"  {i}. Поставщик: {vendor_name}, сумма: {order['total_amount']}")

    demo_vendors = [
        {"id": "demo1", "name": "DemoCorp", "contact_person": "Алексей", "email": "alex@democorp.com",
         "phone": "+7-900-111-22-33", "address": "г. Москва, ул. Демо 1"},
        {"id": "demo2", "name": "DemoTech", "contact_person": "Мария", "email": "maria@demotech.ru",
         "phone": "+7-900-444-55-66", "address": "г. Санкт-Петербург, пр. Демо 2"},
    ]
    print(f"\nДобавлено {len(demo_vendors)} демо-поставщиков")

if __name__ == "__main__":
    demo_run()
