# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: VendorBook
def check_overdue_reminders(vendors):
    today = datetime.date.today()
    overdue = []
    for v in vendors:
        if v.get("reminders") and v["reminders"]:
            for rem in v["reminders"]:
                due_date = datetime.date.fromisoformat(rem["due_date"])
                if due_date < today and not rem.get("completed", False):
                    overdue.append({"vendor": v["name"], "reminder": rem})
    return overdue

def print_overdue_report(vendors):
    report = check_overdue_reminders(vendors)
    if report:
        print(f"\n⚠ Просрочено {len(report)} напоминаний:")
        for item in report:
            print(f"  - Поставщик: {item['vendor']}, Напоминание: {item['reminder']['text']}")
    else:
        print("\n✅ Все напоминания в порядке.")

print_overdue_report(vendor_db)
