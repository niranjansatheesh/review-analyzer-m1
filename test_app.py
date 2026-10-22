from app import classify_review, normalize_review


def test_uppercase_text():
    assert normalize_review("GOOD PRODUCT") == "good product"


def test_leading_trailing_spaces():
    assert normalize_review("   good   product  ") == "good product"


def test_unknown_review():
    assert classify_review("It arrived on Tuesday") == "unknown"


def test_negative_review():
    assert classify_review("Bad quality, broke after a day") == "negative"


if __name__ == "__main__":
    test_uppercase_text()
    test_leading_trailing_spaces()
    test_unknown_review()
    test_negative_review()
    print("All tests passed")
