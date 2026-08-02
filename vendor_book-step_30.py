# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: VendorBook
class UserProfiles:
    _profiles = {}
    
    @staticmethod
    def add_profile(name, role="user", permissions=None):
        if name in UserProfiles._profiles:
            print(f"Профиль '{name}' уже существует.")
            return False
        permissions = permissions or {"read": True, "write": False, "admin": False}
        UserProfiles._profiles[name] = {
            "name": name,
            "role": role,
            "permissions": permissions,
            "created_at": datetime.datetime.now(),
        }
        print(f"Профиль '{name}' добавлен.")
        return True
    
    @staticmethod
    def remove_profile(name):
        if name in UserProfiles._profiles:
            del UserProfiles._profiles[name]
            print(f"Профиль '{name}' удалён.")
            return True
        print(f"Профиль '{name}' не найден.")
        return False
    
    @staticmethod
    def get_profile(name):
        return UserProfiles._profiles.get(name)
    
    @staticmethod
    def list_profiles():
        for name, data in UserProfiles._profiles.items():
            print(f"{data['role']}: {name}")
