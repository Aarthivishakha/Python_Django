import csv
import io

from django.contrib import admin
from django.http import HttpResponse

from catalog.models import Product


def export_selected_csv(modeladmin, request, queryset):
    # Mirrors exports.export_products_csv() almost exactly - a real
    # copy-paste anti-pattern for jscpd-style duplication tools to catch.
    buffer = io.BytesIO()
    writer = csv.writer(buffer)
    writer.writerow(['id', 'name', 'price_cents', 'in_stock'])
    for product in queryset.order_by('id'):
        writer.writerow([product.id, product.name, product.price_cents, product.in_stock])
    response = HttpResponse(buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    return response
export_selected_csv.short_description = 'Export selected products to CSV'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_cents', 'in_stock', 'created_at')
    actions = [export_selected_csv]

admin.site.register(Product, ProductAdmin)
