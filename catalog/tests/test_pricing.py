"""Deliberately partial tests for pricing.py, not padded to full coverage.

classify_order_size's "invalid" and "wholesale" branches are left
untested, and calculate_order_total is never exercised with
has_coupon=True alone or with is_bulk_eligible=True below the bulk
threshold - genuine gaps for the analysis tools to report.
"""
from django.test import TestCase

from catalog.pricing import OrderQuote, calculate_order_total, classify_order_size


class CalculateOrderTotalTests(TestCase):
    def test_no_discount(self):
        self.assertEqual(calculate_order_total(2, 500, is_member=False, has_coupon=False,
                                                is_bulk_eligible=False), 1000)

    def test_member_discount(self):
        self.assertEqual(calculate_order_total(2, 500, is_member=True, has_coupon=False,
                                                is_bulk_eligible=False), 900)

    def test_member_and_coupon_stack(self):
        self.assertEqual(
            calculate_order_total(2, 500, is_member=True, has_coupon=True,
                                  is_bulk_eligible=False, coupon_code='SAVE15'), 750)

    def test_bulk_discount_with_membership(self):
        self.assertEqual(calculate_order_total(10, 500, is_member=True, has_coupon=False,
                                                is_bulk_eligible=True), 4250)

    def test_rejects_non_positive_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(0, 500, is_member=False, has_coupon=False,
                                  is_bulk_eligible=False)

    def test_quantity_is_positional_only(self):
        # quantity/unit_price_cents are positional-only (PEP 570) - passing
        # them by keyword should raise a TypeError.
        with self.assertRaises(TypeError):
            calculate_order_total(quantity=2, unit_price_cents=500, is_member=False,
                                  has_coupon=False, is_bulk_eligible=False)


class ClassifyOrderSizeTests(TestCase):
    def test_small(self):
        self.assertEqual(classify_order_size(2), 'small')

    def test_medium(self):
        self.assertEqual(classify_order_size(7), 'medium')

    def test_bulk(self):
        self.assertEqual(classify_order_size(50), 'bulk')


class OrderQuoteTests(TestCase):
    def test_from_request_returns_matching_type(self):
        quote = OrderQuote.from_request(2, 500, True, False, False)
        self.assertIsInstance(quote, OrderQuote)
        self.assertEqual(quote.total_cents, 900)
        self.assertEqual(quote.size_tier, 'small')
