WORD_TO_NUMBER = {
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

def parse_number(word):
    word = word.strip().lower()

    if word in WORD_TO_NUMBER:
        return WORD_TO_NUMBER[word]

    try:
        return int(word)
    except ValueError:
        raise ValueError(f"Unknown number: '{word}'")

get_num = parse_number
