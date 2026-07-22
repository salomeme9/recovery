# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: VendorBook
def print_table(data, headers):
    col_widths = {h: len(str(h)) for h in headers}
    for row in data:
        for i, v in enumerate(row.values()):
            w = len(str(v)) if v is not None else 0
            if w > col_widths[headers[i]]:
                col_widths[headers[i]] = w
    lines = ['| ' + ' | '.join(f'{h:<{col_widths[h]}}' for h in headers) + ' |']
    lines.append('|' + '|'.join('-' * col_widths[h] for h in headers) + '|')
    for row in data:
        line = '| ' + ' | '.join(f'{v:<{col_widths[h]}}' if v is not None else f'{"":<{col_widths[h]}}' for h, v in zip(headers, row.values())) + ' |'
        lines.append(line)
    print('\n'.join(lines))
