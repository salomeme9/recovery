# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: VendorBook
def dry_run(operation, *args, **kwargs):
    """Execute operation in dry-run mode, returning a simulated result without side effects."""
    original_func = getattr(operation, '_dry_run_func', None)
    if original_func is None:
        return {'success': False, 'error': 'Operation not supported in dry-run mode', 'operation': operation.__name__}
    result = original_func(*args, **kwargs)
    return {'success': True, 'dry_run': True, 'result': result, 'operation': operation.__name__}
