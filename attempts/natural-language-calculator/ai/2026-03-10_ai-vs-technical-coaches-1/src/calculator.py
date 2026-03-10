import operator
from number_words import parse_number

OPERATIONS = {
    'plus': operator.add,
    'minus': operator.sub,
    'times': operator.mul,
    'divided by': operator.truediv,
}

SIMPLE_OPERATIONS = [
    (f' {op_name} ', op_func)
    for op_name, op_func in OPERATIONS.items()
]

COMPOUND_OPERATIONS = [
    (f'{sep}{op_name} the result of ', op_func)
    for op_name, op_func in OPERATIONS.items()
    for sep in (', ', ' ')
]


def calculate(expression):
    expression = normalize_expression(expression)

    delimiter, op_func = find_operation(expression, COMPOUND_OPERATIONS)
    if delimiter:
        result = evaluate_compound_operation(expression, delimiter, op_func)
    else:
        result = evaluate_expression(expression)

    return format_result(result)


def normalize_expression(expression):
    return expression.lower().removeprefix('the result of ')


def find_operation(expression, patterns):
    for delimiter, op_func in patterns:
        if delimiter in expression:
            return delimiter, op_func
    return None, None


def evaluate_compound_operation(expression, delimiter, op_func):
    parts = expression.split(delimiter)
    return op_func(evaluate_expression(parts[0]), evaluate_expression(parts[1]))


def evaluate_expression(expression):
    expression = expression.strip()

    if ', ' in expression:
        return apply_comma_precedence(expression)

    delimiter, op_func = find_operation(expression, SIMPLE_OPERATIONS)
    if delimiter:
        return evaluate_simple_operation(expression, delimiter, op_func)

    return parse_number(expression)


def format_result(result):
    if result == int(result):
        return int(result)
    return round(result, 2)


def apply_comma_precedence(expression):
    parts = expression.split(', ')
    left_val = evaluate_expression(parts[0])
    rest = parts[1]
    for op_name, op_func in OPERATIONS.items():
        prefix = op_name + ' '
        if rest.startswith(prefix):
            right_val = parse_number(rest[len(prefix):])
            return op_func(left_val, right_val)
    raise ValueError(f"Unknown operation after comma: '{rest}'")


def evaluate_simple_operation(expression, delimiter, op_func):
    parts = expression.split(delimiter)
    return op_func(parse_number(parts[0]), parse_number(parts[1]))
