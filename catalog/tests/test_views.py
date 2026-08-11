from __future__ import unicode_literals

from django.test import Client, TestCase

from catalog.models import Product


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        Product.objects.create(name='Widget', price_cents=500)

    def test_product_list(self):
        response = self.client.get('/catalog/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_export_csv(self):
        response = self.client.get('/catalog/products/export/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Widget', response.content)

    def test_quote(self):
        response = self.client.get('/catalog/quote/?quantity=2&unit_price_cents=500&is_member=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'900', response.content)
