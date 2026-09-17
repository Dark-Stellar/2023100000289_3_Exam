from string_analyzer import analyze_digits_and_case


def test_standard_string():
    """Mixed letters and numbers."""
    assert analyze_digits_and_case("Hello 2026") == (1, 10)


def test_no_matches_and_empty():
    """Empty string and lowercase-only string must return (0, 0)."""
    assert analyze_digits_and_case("") == (0, 0)
    assert analyze_digits_and_case("python") == (0, 0)


def test_symbols_and_spaces():
    """Whitespace, symbols, uppercase letters, and digits."""
    assert analyze_digits_and_case(" #1 CAT & 9 DOGS ") == (7, 10)