# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: VendorBook
import unittest

class TestEdgeCases(unittest.TestCase):
    def test_empty_vendor_name(self):
        from vendorbook import Vendor
        with self.assertRaises(ValueError):
            Vendor(name="")

    def test_vendor_with_special_chars(self):
        from vendorbook import Vendor
        v = Vendor(name="Test Vendor & Co., Ltd.")
        self.assertEqual(v.name, "Test Vendor & Co., Ltd.")

    def test_order_negative_amount(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="Widget", amount=-100, price=10)

    def test_order_zero_amount(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="Widget", amount=0, price=10)

    def test_order_non_numeric_amount(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(TypeError):
            Order(vendor=v, item="Widget", amount="ten", price=10)

    def test_order_non_numeric_price(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(TypeError):
            Order(vendor=v, item="Widget", amount=10, price="ten")

    def test_order_non_numeric_quantity(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(TypeError):
            Order(vendor=v, item="Widget", amount=10, price=10, quantity="two")

    def test_rating_non_numeric(self):
        from vendorbook import Vendor
        v = Vendor(name="Rating Vendor")
        with self.assertRaises(TypeError):
            v.set_rating("five")

    def test_rating_below_zero(self):
        from vendorbook import Vendor
        v = Vendor(name="Rating Vendor")
        with self.assertRaises(ValueError):
            v.set_rating(-1)

    def test_rating_above_max(self):
        from vendorbook import Vendor
        v = Vendor(name="Rating Vendor")
        with self.assertRaises(ValueError):
            v.set_rating(6)

    def test_rating_max(self):
        from vendorbook import Vendor
        v = Vendor(name="Rating Vendor")
        v.set_rating(5)
        self.assertEqual(v.rating, 5)

    def test_order_no_vendor(self):
        from vendorbook import Order
        with self.assertRaises(ValueError):
            Order(vendor=None, item="Widget", amount=10, price=10)

    def test_order_no_item(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="", amount=10, price=10)

    def test_order_no_amount(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="Widget", amount=None, price=10)

    def test_order_no_price(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="Widget", amount=10, price=None)

    def test_order_no_quantity(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="Widget", amount=10, price=10, quantity=None)

    def test_order_no_date(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="Widget", amount=10, price=10, quantity=1, date=None)

    def test_order_no_total(self):
        from vendorbook import Vendor, Order
        v = Vendor(name="Edge Vendor")
        with self.assertRaises(ValueError):
            Order(vendor=v, item="Widget", amount=10, price=10, quantity=1, total=None)
