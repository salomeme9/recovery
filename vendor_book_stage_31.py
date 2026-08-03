# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: VendorBook
def switch_profile(new_name):
    """Переключить активный профиль пользователя."""
    if new_name not in profiles:
        print(f"Ошибка: Профиль '{new_name}' не найден.")
        return None
    
    active = [p for p in profiles.values() if p.get('active')]
    if len(active) > 0:
        for i, profile in enumerate(profiles):
            if profile['name'] == new_name:
                profiles[profile['name']]['active'] = True
                for other_profile in active:
                    profiles[other_profile]['active'] = False
                print(f"Профиль '{new_name}' теперь активен.")
                return profiles[new_name]
    
    print("Ошибка: Не удалось переключить профиль. Убедитесь, что выбран другой профиль.")
    return None
