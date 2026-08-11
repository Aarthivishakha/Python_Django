"""Combined Coverage.py + Beniget fixture: branch coverage and a dead
definition in the same minimal file."""


def evaluate_order(total, is_member):
    unused_note = "not used"
    if total > 100:
        discount = 0.1
    else:
        discount = 0.0
    if is_member:
        discount += 0.05
    return total * (1 - discount)
