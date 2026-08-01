# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: VendorBook
APP_CONFIG = {
    "app_name": "VendorBook",
    "version": "0.29",
    "max_orders_per_vendor": 10,
    "default_rating_threshold": 3.5,
    "data_file": "vendors.json",
    "log_level": "INFO",
}


def get_config(key: str):
    """Return a config value or raise KeyError."""
    return APP_CONFIG[key]


def set_config(key: str, value):
    """Set a config value and print confirmation."""
    if key not in APP_CONFIG:
        raise KeyError(f"Unknown config key: {key}")
    APP_CONFIG[key] = value
    print(f"[VendorBook Config] {key} → {value}")


def reset_default_config():
    """Reset all settings to their default values."""
    for k, v in list(APP_CONFIG.items()):
        if isinstance(v, str):
            APP_CONFIG[k] = v


if __name__ == "__main__":
    set_config("log_level", "DEBUG")
    print(APP_CONFIG)
