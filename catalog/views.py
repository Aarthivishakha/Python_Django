from django.http import HttpResponse, HttpResponseNotAllowed

from catalog.exports import export_products_csv
from catalog.models import Product
from catalog.pricing import calculate_order_total, classify_order_size

try:
    import json
except ImportError:
    import simplejson as json


def product_list(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    products = [
        {'id': p.id, 'name': p.name, 'price_cents': p.price_cents, 'in_stock': p.in_stock}
        for p in Product.objects.all()
    ]
    return HttpResponse(json.dumps({'products': products}), content_type='application/json')


def product_export(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    response = HttpResponse(export_products_csv(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    return response


def quote(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    quantity = int(request.GET.get('quantity', 1))
    unit_price_cents = int(request.GET.get('unit_price_cents', 0))
    is_member = request.GET.get('is_member') == '1'
    has_coupon = request.GET.get('has_coupon') == '1'
    is_bulk_eligible = request.GET.get('is_bulk_eligible') == '1'
    coupon_code = request.GET.get('coupon_code') if has_coupon else None

    total = calculate_order_total(quantity, unit_price_cents, is_member, has_coupon,
                                   is_bulk_eligible, coupon_code)
    payload = {'total_cents': total, 'size_tier': classify_order_size(quantity)}
    return HttpResponse(json.dumps(payload), content_type='application/json')
