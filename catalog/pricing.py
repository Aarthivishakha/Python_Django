"""Order pricing logic for the storefront. Real business logic, not a demo
fixture: views.py calls into this module for actual request handling, and
the analysis tools under quality/ point at it directly.

Uses Python 3.12 syntax: a `match` statement (PEP 634), `typing.Self`
(PEP 673) on OrderQuote.from_request, and a PEP 695 `type` alias
statement (new in 3.12) for the Cents domain type.
"""
from dataclasses import dataclass
from typing import Self

type Cents = int

MEMBER_DISCOUNT_PCT = 10
COUPON_DISCOUNT_PCT = 15
BULK_THRESHOLD = 10
BULK_DISCOUNT_PCT = 5


def calculate_order_total(
    quantity: int,
    unit_price_cents: Cents,
    is_member: bool,
    has_coupon: bool,
    is_bulk_eligible: bool,
    coupon_code: str | None = None,
) -> Cents:
    """Compute an order total in cents.

    Four independent boolean inputs (membership, coupon, bulk eligibility,
    and the bulk quantity threshold) combine into the discount decision -
    a genuine target for MC/DC and mutation testing.

    pre: quantity > 0
    pre: unit_price_cents >= 0
    post: __return__ >= 0
    """
    if quantity <= 0:
        raise ValueError(f"quantity must be positive, got {quantity}")
    if unit_price_cents < 0:
        raise ValueError(f"unit_price_cents must be non-negative, got {unit_price_cents}")
    if has_coupon and coupon_code is None:
        raise ValueError("coupon_code is required when has_coupon is True")

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
    """Cyclomatic-complexity target for radon/lizard/cognitive-ast.

    Each branch is a real order-size tier a fulfillment system would need.
    """
    match quantity:
        case q if q <= 0:
            return "invalid"
        case q if q < 5:
            return "small"
        case q if q < BULK_THRESHOLD:
            return "medium"
        case q if q < 100:
            return "bulk"
        case _:
            return "wholesale"


@dataclass
class OrderQuote:
    """Bundles a computed total with its size tier for the quote endpoint.

    from_request is a classmethod returning Self (PEP 673), so a future
    subclass would get back its own type, not a hardcoded OrderQuote.
    """

    total_cents: Cents
    size_tier: str

    @classmethod
    def from_request(
        cls,
        quantity: int,
        unit_price_cents: Cents,
        is_member: bool,
        has_coupon: bool,
        is_bulk_eligible: bool,
        coupon_code: str | None = None,
    ) -> Self:
        total = calculate_order_total(
            quantity, unit_price_cents, is_member, has_coupon, is_bulk_eligible, coupon_code
        )
        return cls(total_cents=total, size_tier=classify_order_size(quantity))
