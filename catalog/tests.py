"""Deliberately partial tests, not padded to full coverage.

classify_order_size's "invalid" and "wholesale" branches are left
untested, and calculate_order_total is never exercised with
has_coupon=True alone or with is_bulk_eligible=True below the bulk
threshold - genuine gaps for the analysis tools to report.

A single tests.py module, not a tests/ package: Django 1.5's default
test runner (predating DiscoverRunner, which became default in 1.6)
expects app tests in catalog/tests.py.
"""
from django.test import TestCase
from django.test.client import Client

from catalog.models import Product
from catalog.pricing import calculate_order_total, classify_order_size


class ProductModelTests(TestCase):
    def test_unicode_returns_name(self):
        product = Product.objects.create(name='Widget', price_cents=999)
        self.assertEqual(unicode(product), u'Widget')

    def test_defaults_in_stock_true(self):
        product = Product.objects.create(name='Gadget', price_cents=1500)
        self.assertTrue(product.in_stock)


class CalculateOrderTotalTests(TestCase):
    def test_no_discount(self):
        self.assertEqual(calculate_order_total(2, 500, False, False, False), 1000)

    def test_member_discount(self):
        self.assertEqual(calculate_order_total(2, 500, True, False, False), 900)

    def test_member_and_coupon_stack(self):
        self.assertEqual(
            calculate_order_total(2, 500, True, True, False, coupon_code='SAVE15'), 750)

    def test_bulk_discount_with_membership(self):
        self.assertEqual(calculate_order_total(10, 500, True, False, True), 4250)

    def test_rejects_non_positive_quantity(self):
        self.assertRaises(ValueError, calculate_order_total, 0, 500, False, False, False)


class ClassifyOrderSizeTests(TestCase):
    def test_small(self):
        self.assertEqual(classify_order_size(2), 'small')

    def test_medium(self):
        self.assertEqual(classify_order_size(7), 'medium')

    def test_bulk(self):
        self.assertEqual(classify_order_size(50), 'bulk')


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        Product.objects.create(name='Widget', price_cents=500)

    def test_product_list(self):
        response = self.client.get('/catalog/products/')
        self.assertEqual(response.status_code, 200)

    def test_quote(self):
        response = self.client.get('/catalog/quote/?quantity=2&unit_price_cents=500&is_member=1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('900' in response.content)
