"""Deliberately partial tests for pricing.py, not padded to full coverage.

classify_order_size's "invalid" and "wholesale" branches are left
untested, and calculate_order_total is never exercised with
has_coupon=True alone or with is_bulk_eligible=True below the bulk
threshold - genuine coverage/MC/DC gaps for the analysis tools to report.
"""
from django.test import TestCase

from catalog.pricing import calculate_order_total, classify_order_size


class CalculateOrderTotalTests(TestCase):
    def test_no_discount(self):
        self.assertEqual(calculate_order_total(2, 500, False, False, False), 1000)

    def test_member_discount(self):
        self.assertEqual(calculate_order_total(2, 500, True, False, False), 900)

    def test_member_and_coupon_stack(self):
        self.assertEqual(
            calculate_order_total(2, 500, True, True, False, coupon_code="SAVE15"), 750
        )

    def test_bulk_discount_with_membership(self):
        self.assertEqual(calculate_order_total(10, 500, True, False, True), 4250)

    def test_rejects_non_positive_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(0, 500, False, False, False)


class ClassifyOrderSizeTests(TestCase):
    def test_small(self):
        self.assertEqual(classify_order_size(2), "small")

    def test_medium(self):
        self.assertEqual(classify_order_size(7), "medium")

    def test_bulk(self):
        self.assertEqual(classify_order_size(50), "bulk")
