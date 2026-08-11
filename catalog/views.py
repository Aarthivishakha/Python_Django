from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET

from .exports import export_products_csv
from .models import Product
from .pricing import calculate_order_total, classify_order_size


@require_GET
def product_list(request) -> JsonResponse:
    products = [
        {"id": p.id, "name": p.name, "price_cents": p.price_cents, "in_stock": p.in_stock}
        for p in Product.objects.all()
    ]
    return JsonResponse({"products": products})


@require_GET
def product_export(request) -> HttpResponse:
    response = HttpResponse(export_products_csv(), content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=products.csv"
    return response


@require_GET
def quote(request) -> JsonResponse:
    quantity = int(request.GET.get("quantity", 1))
    unit_price_cents = int(request.GET.get("unit_price_cents", 0))
    is_member = request.GET.get("is_member") == "1"
    has_coupon = request.GET.get("has_coupon") == "1"
    is_bulk_eligible = request.GET.get("is_bulk_eligible") == "1"

    total = calculate_order_total(quantity, unit_price_cents, is_member, has_coupon, is_bulk_eligible)
    return JsonResponse({"total_cents": total, "size_tier": classify_order_size(quantity)})
