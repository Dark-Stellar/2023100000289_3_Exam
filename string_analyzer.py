def analyze_digits_and_case(user_input):

    if not isinstance(user_input, str):
        return (0, 0)

    cleaned = user_input.strip()

    if not cleaned:
        return (0, 0)

    uppercase_count = 0
    digit_sum = 0

    for ch in cleaned:
        if ch.isupper():
            uppercase_count += 1
        elif ch.isdigit():
            digit_sum += int(ch)

    if uppercase_count == 0 and digit_sum == 0:
        return (0, 0)

    return (uppercase_count, digit_sum)