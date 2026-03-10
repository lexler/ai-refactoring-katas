NUMBER_WORDS = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
}


def parse_number(text):
    text = text.strip().lower()

    if text in NUMBER_WORDS:
        return NUMBER_WORDS[text]

    try:
        return int(text)
    except ValueError:
        raise ValueError(f"Unknown number: '{text}'")
