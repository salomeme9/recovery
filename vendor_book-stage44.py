# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: VendorBook
import shutil
from datetime import datetime

def backup_data_file(data_file_path, backup_dir="."):
    """Создаёт резервную копию файла данных с временной меткой."""
    if not data_file_path or not os.path.exists(data_file_path):
        return None
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{os.path.basename(data_file_path)}_{timestamp}")
    try:
        shutil.copy2(data_file_path, backup_path)
        return backup_path
    except Exception:
        return None
