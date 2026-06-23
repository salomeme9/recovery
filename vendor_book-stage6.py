# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: VendorBook
class VendorFilter:
    def __init__(self, vendors):
        self.vendors = vendors

    def filter_by_status(self, status=None):
        if not status:
            return list(self.vendors)
        return [v for v in self.vendors if getattr(v, 'status', None) == status]

    def filter_by_category(self, category=None):
        if not category:
            return list(self.vendors)
        return [v for v in self.vendors if getattr(v, 'category', None) == category]

    def filter_by_tags(self, tags=None):
        if not tags or not isinstance(tags, set):
            return list(self.vendors)
        result = []
        for vendor in self.vendors:
            vendor_tags = getattr(vendor, 'tags', [])
            if any(tag in vendor_tags for tag in tags):
                result.append(vendor)
        return result

    def filter_combined(self, status=None, category=None, tags=None):
        filtered = list(self.vendors)
        if status:
            filtered = [v for v in filtered if getattr(v, 'status', None) == status]
        if category:
            filtered = [v for v in filtered if getattr(v, 'category', None) == category]
        if tags:
            filtered = self.filter_by_tags(tags)(filtered)
        return filtered
