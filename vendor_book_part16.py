# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: VendorBook
def monthly_stats(vendors):
    stats = {}
    for v in vendors:
        month_key = v['orders'][0]['date'][:7] if v.get('orders') and v['orders'][0].get('date') else None
        if not month_key:
            continue
        if month_key not in stats:
            stats[month_key] = {'count': 0, 'total': 0.0}
        stats[month_key]['count'] += 1
        stats[month_key]['total'] += sum(o['price'] for o in v['orders'])
    return stats
