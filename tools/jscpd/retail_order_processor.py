"""jscpd duplication fixture (Python 3.6) - retail order path."""


def process_retail_order(order_id, quantity, unit_price, discount_pct):
    if quantity <= 0:
        raise ValueError('quantity must be positive')
    subtotal = quantity * unit_price
    discount = subtotal * (discount_pct / 100.0)
    total = subtotal - discount
    tax = total * 0.08
    grand_total = total + tax
    return {
        'order_id': order_id,
        'subtotal': subtotal,
        'discount': discount,
        'tax': tax,
        'grand_total': grand_total,
    }
