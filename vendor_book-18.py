# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: VendorBook
def add_tags(self, vendor_id: int, tags: list[str]) -> None:
    if not isinstance(tags, list) or len(tags) == 0:
        raise ValueError("Tags must be a non-empty list.")
    vendor = self._vendors.get(vendor_id)
    if not vendor:
        raise KeyError(f"Vendor {vendor_id} not found.")
    current_tags = set(vendor["tags"]) | set(self._default_tags)
    for tag in tags:
        if not isinstance(tag, str) or len(tag.strip()) == 0:
            raise ValueError("Each tag must be a non-empty string.")
        new_tag = tag.strip().lower()
        if new_tag in current_tags:
            continue
        current_tags.add(new_tag)
    vendor["tags"] = sorted(current_tags)

def remove_tags(self, vendor_id: int, tags_to_remove: list[str]) -> list[str]:
    if not isinstance(tags_to_remove, list):
        raise ValueError("Tags to remove must be a list.")
    vendor = self._vendors.get(vendor_id)
    if not vendor:
        raise KeyError(f"Vendor {vendor_id} not found.")
    current_tags = set(vendor["tags"]) | set(self._default_tags)
    removed = []
    for tag in tags_to_remove:
        new_tag = tag.strip().lower() if isinstance(tag, str) else ""
        if new_tag and new_tag in current_tags:
            current_tags.discard(new_tag)
            removed.append(new_tag)
    vendor["tags"] = sorted(current_tags)
    return removed
