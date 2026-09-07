# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: VendorBook
import sys
from vendorbook import VendorBook

def main():
    book = VendorBook()
    if len(sys.argv) < 2:
        print("Usage: python vendorbook.py <add|list|search|order|rating>")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "add":
        name = input("Vendor name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        book.add_vendor(name, email, phone)
        print("Vendor added.")
    elif cmd == "list":
        book.list_vendors()
    elif cmd == "search":
        q = input("Search: ").lower()
        book.search_vendors(q)
    elif cmd == "order":
        vid = input("Vendor ID: ")
        item = input("Item: ")
        qty = int(input("Quantity: "))
        book.place_order(vid, item, qty)
        print("Order placed.")
    elif cmd == "rating":
        vid = input("Vendor ID: ")
        score = float(input("Score (0-5): "))
        book.update_rating(vid, score)
        print("Rating updated.")
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
