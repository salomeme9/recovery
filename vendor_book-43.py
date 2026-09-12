# === Stage 43: Добавь пагинацию длинных списков ===
# Project: VendorBook
def paginate(data, page_size=10):
    total = len(data)
    pages = (total + page_size - 1) // page_size if page_size else 1
    page = min(max(1, page), pages)
    start = (page - 1) * page_size
    end = min(start + page_size, total)
    return {
        'data': data[start:end],
        'total': total,
        'page': page,
        'pages': pages,
        'has_next': end < total,
        'has_prev': page > 1,
    }
