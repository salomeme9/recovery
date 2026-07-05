# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: VendorBook
def generate_summary():
    print("=" * 40)
    print("СВОДКА ПОСТАВЩИКОВ")
    print("=" * 40)
    
    total_suppliers = len(suppliers)
    active_orders = sum(1 for s in suppliers if s['orders'])
    avg_rating = sum(s.get('rating', 0) for s in suppliers) / max(total_suppliers, 1)
    
    print(f"Всего поставщиков: {total_suppliers}")
    print(f"Поставщики с активными заказами: {active_orders}")
    print(f"Средний рейтинг: {avg_rating:.2f}")
    
    if total_suppliers > 0:
        top_supplier = max(suppliers, key=lambda x: x.get('rating', 0))
        print(f"Лучший поставщик по рейтингу: {top_supplier['name']} ({top_supplier['rating']})")
        
        low_stock_alerts = [s for s in suppliers if s.get('stock_level', float('inf')) < 10]
        if low_stock_alerts:
            print(f"Внимание! Низкий остаток у {len(low_stock_alerts)} поставщиков:")
            for s in low_stock_alerts[:3]:
                print(f"  - {s['name']}: {s.get('stock_level', 'N/A')} ед.")
        else:
            print("Остатки на складах в норме.")
    
    print("=" * 40)
