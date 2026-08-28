# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: VendorBook
TEMPLATE_REGISTRY = {}

def register_template(name, fields, default_values=None):
    TEMPLATE_REGISTRY[name] = {'fields': fields, 'default_values': default_values or {}}

def create_from_template(name, **overrides):
    if name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Template '{name}' not found. Available: {list(TEMPLATE_REGISTRY.keys())}")
    template = TEMPLATE_REGISTRY[name]
    record = {f: template['default_values'].get(f, '') for f in template['fields']}
    record.update(overrides)
    return record

def quick_add_suppliers(supplier_list):
    suppliers = []
    for name, fields, defaults in supplier_list:
        register_template(name, fields, defaults)
        suppliers.append(create_from_template(name))
    return suppliers
