# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: VendorBook
def sort_records(records, key='date', reverse=False):
    if key == 'date':
        return sorted(records, key=lambda r: r.get('created_at', ''), reverse=reverse)
    elif key == 'priority':
        priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        return sorted(records, key=lambda r: priority_map.get(r.get('priority', 'low'), 3), reverse=reverse)
    elif key == 'name':
        return sorted(records, key=lambda r: r.get('name', '').lower(), reverse=False)
    else:
        raise ValueError(f"Unsupported sort key: {key}")
