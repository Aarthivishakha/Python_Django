from __future__ import unicode_literals

from django.test import TestCase

from catalog.models import Product


class ProductModelTests(TestCase):
    def test_str_returns_name(self):
        product = Product.objects.create(name='Widget', price_cents=999)
        self.assertEqual(str(product), 'Widget')

    def test_defaults_in_stock_true(self):
        product = Product.objects.create(name='Gadget', price_cents=1500)
        self.assertTrue(product.in_stock)
