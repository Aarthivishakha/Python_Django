"""Order pricing logic for the storefront. Real business logic, not a demo
fixture: views.py calls into this module for actual request handling, and
the analysis tools under quality/ point at it directly.

Written for Python 2.6: no f-strings or type-hint syntax (both Python 3
only), no set/dict comprehensions (added in 2.7), % string formatting,
and old-style `except X as e:` (available since 2.6 via PEP 3110).
"""

MEMBER_DISCOUNT_PCT = 10
COUPON_DISCOUNT_PCT = 15
BULK_THRESHOLD = 10
BULK_DISCOUNT_PCT = 5


def calculate_order_total(quantity, unit_price_cents, is_member, has_coupon,
                           is_bulk_eligible, coupon_code=None):
    """Compute an order total in cents.

    Four independent boolean inputs (membership, coupon, bulk eligibility,
    and the bulk quantity threshold) combine into the discount decision -
    a genuine target for mutation-style testing.
    """
    if quantity <= 0:
        raise ValueError('quantity must be positive, got %r' % quantity)
    if unit_price_cents < 0:
        raise ValueError('unit_price_cents must be non-negative, got %r' % unit_price_cents)
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


def classify_order_size(quantity):
    """Structural-complexity target for duplication/complexity tools.

    Plain if/elif - Python 2.6 has no match statement (added in 3.10).
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
