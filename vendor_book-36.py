# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: VendorBook
def fix_vendor_data(db):
    """Проверяет и чинит типовые проблемы в справочнике:
    - пустые поля обязательных полей
    - несуществующие ID поставщиков в заказах
    - отрицательные цены в заказах
    - невалидные рейтинги (от 0 до 10)
    """
    fixed = 0
    # Чиним пустые обязательные поля у поставщиков
    for v in db['suppliers']:
        if not v.get('name'):
            v['name'] = '(без имени)'
            fixed += 1
        if not v.get('company'):
            v['company'] = '(без компании)'
            fixed += 1
    # Чиним заказы: невалидные цены и несуществующие поставщики
    for o in db['orders']:
        if o.get('price', 0) < 0:
            o['price'] = 0
            fixed += 1
        if o.get('vendor_id') not in [s['id'] for s in db['suppliers']]:
            o['vendor_id'] = None
            fixed += 1
        rating = o.get('rating')
        if rating is not None and (rating < 0 or rating > 10):
            o['rating'] = 0 if rating < 0 else 10
            fixed += 1
    return fixed
