"""Cognitive complexity fixture for complexipy: deeply nested decision logic."""


def classify_transaction(amount, is_international, is_new_customer, flagged):
    if amount > 10000:
        if is_international:
            if is_new_customer:
                if flagged:
                    return "high_risk_review"
                else:
                    return "international_new_customer"
            else:
                return "international_review"
        else:
            if flagged:
                return "domestic_flagged"
            else:
                return "domestic_review"
    else:
        if is_new_customer and flagged:
            return "small_flagged"
        return "approved"
