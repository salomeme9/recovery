# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: VendorBook
def main():
    print("=== VendorBook: Справочник поставщиков ===")
    while True:
        cmd = input("\n1 - Список, 2 - Добавить, 3 - Поиск, 4 - Выход: ").strip()
        if not cmd or cmd == "4": break
        elif cmd == "1": print("Список поставщиков (заглушка): [A] Apple, [B] Samsung")
        elif cmd == "2": name = input("Имя: "); print(f"Поставщик '{name}' добавлен.")
        elif cmd == "3": q = input("Поиск по имени: ").strip(); results = [n for n in ["Apple", "Samsung"] if q.lower() in n]; print(results or "Ничего не найдено")

if __name__ == "__main__": main()
