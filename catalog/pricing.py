"""Order pricing logic for the storefront. Real business logic, not a demo
fixture: views.py calls into this module for actual request handling, and
the analysis tools under quality/ point at it directly.

Uses Python 3.6 syntax: variable annotations (PEP 526) and f-strings
(PEP 498), both new in 3.6.
"""
from typing import Optional

MEMBER_DISCOUNT_PCT: int = 10
COUPON_DISCOUNT_PCT: int = 15
BULK_THRESHOLD: int = 10
BULK_DISCOUNT_PCT: int = 5


def calculate_order_total(quantity: int, unit_price_cents: int, is_member: bool,
                           has_coupon: bool, is_bulk_eligible: bool,
                           coupon_code: Optional[str] = None) -> int:
    """Compute an order total in cents.

    Four independent boolean inputs (membership, coupon, bulk eligibility,
    and the bulk quantity threshold) combine into the discount decision -
    a genuine target for mutation-style testing.
    """
    if quantity <= 0:
        raise ValueError(f'quantity must be positive, got {quantity}')
    if unit_price_cents < 0:
        raise ValueError(f'unit_price_cents must be non-negative, got {unit_price_cents}')
    if has_coupon and coupon_code is None:
        raise ValueError('coupon_code is required when has_coupon is True')

    subtotal = quantity * unit_price_cents

    discount_pct = 0
    if is_member and has_coupon:
        discount_pct = MEMBER_DISCOUNT_PCT + COUPON_DISCOUNT_PCT
    elif is_member:
        discount_pct = MEMBER_DISCOUNT_PCT
    elif has_coupon:
        discount_pct = COUPON_DISCOUNT_PCT

    if is_bulk_eligible and quantity >= BULK_THRESHOLD:
        discount_pct += BULK_DISCOUNT_PCT

    discount = (subtotal * discount_pct) // 100
    return subtotal - discount


def classify_order_size(quantity: int) -> str:
    """Structural-complexity target for duplication/complexity tools.

    Plain if/elif - Python 3.6 has no match statement (added in 3.10).
    """
    if quantity <= 0:
        return 'invalid'
    elif quantity < 5:
        return 'small'
    elif quantity < BULK_THRESHOLD:
        return 'medium'
    elif quantity < 100:
        return 'bulk'
    else:
        return 'wholesale'
