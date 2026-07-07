# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: VendorBook
def weekly_stats(vendors):
    """Расчёт недельной статистики по датам."""
    stats = {}
    for vendor in vendors:
        if not hasattr(vendor, 'orders') or not vendor.orders:
            continue
        dates = []
        for order in vendor.orders:
            try:
                date_str = str(order.get('date', ''))
                if date_str:
                    from datetime import datetime
                    dt = datetime.strptime(date_str[:10], '%Y-%m-%d')
                    week = dt.isocalendar()[1]  # неделя по ISO
                    dates.append(week)
            except (ValueError, AttributeError):
                pass
        if dates:
            stats[vendor.name] = {
                'min_week': min(dates),
                'max_week': max(dates),
                'avg_week': sum(dates) / len(dates),
                'count': len(dates),
            }
    return stats
