# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: VendorBook
class Reminder:
    def __init__(self, vendor_id, description, due_date):
        self.vendor_id = vendor_id
        self.description = description
        self.due_date = due_date

    def is_overdue(self):
        return datetime.now().date() > self.due_date.date()

    @staticmethod
    def create_reminder(vendor_id, description, due_date_str):
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        return Reminder(vendor_id, description, due_date)
