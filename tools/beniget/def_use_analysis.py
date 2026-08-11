"""Beniget def-use fixture with intentional dead definitions."""


def process_order(sku, quantity, price):
    unused_currency_symbol = "$"
    last_seen_sku = sku
    _draft_notes = "not used in return path"
    total = quantity * price
    used_sku = sku
    return {"sku": used_sku, "total": total, "seen": last_seen_sku}


def normalize_tags(tags):
    unused_prefix = "tag:"
    cleaned = []
    for tag in tags:
        if tag:
            cleaned.append(str(tag).strip().lower())
    return cleaned
