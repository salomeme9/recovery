# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: VendorBook
def archive_records(records, min_age_days=90):
    """Archive records older than min_age_days or with completed status."""
    import datetime
    now = datetime.datetime.now()
    for r in records:
        if isinstance(r.get('created', 0), (int, float)):
            age = (now - datetime.datetime.fromtimestamp(float(r['created']))).days
            if age >= min_age_days or r.get('status') == 'completed':
                r.setdefault('archived_at', now.isoformat())
                r['archive_reason'] = f'age={age}d,status={r["status"]}'
    return records
