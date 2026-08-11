"""MC/DC fixture: a compound boolean decision for pymcdc to analyze."""


def classify_score(score, is_bonus, is_premium):
    if score >= 75 and (is_bonus or is_premium):
        return "pass_with_credit"
    return "standard"
