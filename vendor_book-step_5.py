# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: VendorBook
def delete_supplier(supplier_id: int) -> bool:
    if supplier_id not in suppliers_db:
        print(f"Поставщик с ID {supplier_id} не найден.")
        return False
    
    del suppliers_db[supplier_id]
    
    # Удаление связанных заказов и рейтингов для чистоты данных
    orders_to_remove = [order for order in orders_db if order['supplier_id'] == supplier_id]
    ratings_to_remove = [rating for rating in ratings_db if rating['supplier_id'] == supplier_id]
    
    if orders_to_remove:
        print(f"Удалено {len(orders_to_remove)} заказов.")
    if ratings_to_remove:
        print(f"Удалено {len(ratings_to_remove)} рейтингов.")
        
    return True

def delete_order(order_id: int) -> bool:
    order = orders_db.get(order_id)
    if not order:
        print(f"Заказ с ID {order_id} не найден.")
        return False
    
    supplier_id = order['supplier_id']
    
    # Удаление рейтинга заказа, если он существует
    rating_key = f"{supplier_id}_{order_id}"
    ratings_db.pop(rating_key, None)
    
    del orders_db[order_id]
    print(f"Заказ {order_id} успешно удален.")
    return True

def delete_rating(supplier_id: int, order_id: int) -> bool:
    rating_key = f"{supplier_id}_{order_id}"
    if rating_key not in ratings_db:
        print(f"Рейтинг для поставщика {supplier_id}, заказ {order_id} не найден.")
        return False
    
    del ratings_db[rating_key]
    print("Рейтинг успешно удален.")
    return True
