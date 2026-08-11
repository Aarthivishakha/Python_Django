from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET

from .exports import export_products_csv
from .models import Product
from .pricing import OrderQuote, QuoteCache

# Module-level cache instance - QuoteCache() with no type argument relies
# on the PEP 696 default (T = OrderQuote), so this really is a
# QuoteCache[OrderQuote] without spelling it out.
_quote_cache: QuoteCache = QuoteCache()


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
    coupon_code = request.GET.get("coupon_code") if has_coupon else None

    cache_key = f"{quantity}:{unit_price_cents}:{is_member}:{has_coupon}:{is_bulk_eligible}:{coupon_code}"
    result = _quote_cache.get(cache_key)
    if result is None:
        result = OrderQuote.from_request(
            quantity, unit_price_cents, is_member, has_coupon, is_bulk_eligible, coupon_code
        )
        _quote_cache.set(cache_key, result)

    return JsonResponse({"total_cents": result.total_cents, "size_tier": result.size_tier})
