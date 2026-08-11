from mcdc_decision import classify_score


def test_all_combinations():
    assert classify_score(80, True, False) == "pass_with_credit"
    assert classify_score(80, False, True) == "pass_with_credit"
    assert classify_score(80, False, False) == "standard"
    assert classify_score(70, True, True) == "standard"
