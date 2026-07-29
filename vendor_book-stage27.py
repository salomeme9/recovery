# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: VendorBook
def reset_demo_data():
    """Сброс всех данных к демо-состоянию."""
    global vendors, orders, ratings, messages, search_history
    
    # Возвращаем список поставщиков в исходное состояние
    vendors = [
        {
            'id': 1,
            'name': 'TechSupply Co.',
            'contact': {'email': 'sales@techsupply.com', 'phone': '+7 (495) 123-45-67'},
            'conditions': {'payment_terms': 'net_30', 'min_order': 1000, 'currency': 'USD'},
            'orders': [],
            'rating': {'score': 0, 'reviews': []}
        },
        {
            'id': 2,
            'name': 'GlobalParts Inc.',
            'contact': {'email': 'info@globalparts.com', 'phone': '+7 (812) 987-65-43'},
            'conditions': {'payment_terms': 'net_60', 'min_order': 2500, 'currency': 'USD'},
            'orders': [],
            'rating': {'score': 0, 'reviews': []}
        },
        {
            'id': 3,
            'name': 'EcoMaterials Ltd.',
            'contact': {'email': 'procurement@ecomaterials.com', 'phone': '+7 (343) 555-12-34'},
            'conditions': {'payment_terms': 'net_15', 'min_order': 500, 'currency': 'USD'},
            'orders': [],
            'rating': {'score': 0, 'reviews': []}
        }
    ]
    
    orders = []
    ratings = []
    messages = []
    search_history = []


def clear_state():
    """Полная очистка состояния приложения."""
    global vendors, orders, ratings, messages, search_history
    
    vendors = []
    orders = []
    ratings = []
    messages = []
    search_history = []
