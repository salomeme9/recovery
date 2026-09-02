# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: VendorBook
def test_vendor_creation():
    from vendorbook import Vendor, Product, Order, Rating
    v = Vendor(name="TestCo", email="test@example.com", phone="+1234567890")
    assert v.name == "TestCo"
    assert v.email == "test@example.com"
    assert v.phone == "+1234567890"
    assert v.id is not None
    p = Product(name="Widget", price=10.0, vendor=v)
    assert p.name == "Widget"
    assert p.price == 10.0
    assert p.vendor == v
    o = Order(id="ORD-001", product=p, quantity=5, date="2024-01-01")
    assert o.id == "ORD-001"
    assert o.product == p
    assert o.quantity == 5
    r = Rating(vendor=v, stars=4.5)
    assert r.stars == 4.5
    assert r.vendor == v
