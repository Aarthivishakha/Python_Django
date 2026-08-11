"""CSV export helpers used by the storefront's reporting views."""
from __future__ import annotations

import csv
import io

from .models import Product


def export_products_csv() -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "name", "price_cents", "in_stock"])
    for product in Product.objects.all().order_by("id"):
        writer.writerow([product.id, product.name, product.price_cents, product.in_stock])
    return buffer.getvalue()
