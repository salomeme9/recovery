# === Stage 17: Добавь группировку записей по категориям ===
# Project: VendorBook
def group_by_category(self):
        """Группирует записей по категориям и показывает статистику."""
        groups = {}
        for record in self.records:
            cat = record.get("category", "Unknown")
            if cat not in groups:
                groups[cat] = {"count": 0, "total_score": 0}
            groups[cat]["count"] += 1
            groups[cat]["total_score"] += record.get("score", 0)

        print(f"\n{'─'*60}")
        print("📊 Группировка записей по категориям")
        for cat, stats in sorted(groups.items()):
            avg = (stats["total_score"] / stats["count"]) if stats["count"] else 0
            bar_len = int(stats["count"] * 25)
            print(f"  {cat:12s} | {'█' * bar_len:<25}| {stats['count']:3d} шт. | Средний рейтинг: {avg:.1f}")

        if not groups:
            print("  (Записей нет)")
