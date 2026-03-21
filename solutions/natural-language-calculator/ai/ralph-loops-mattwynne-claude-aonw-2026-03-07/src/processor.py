import operator

from utils import parse_number

OPERATORS = {
    'plus': operator.add,
    'minus': operator.sub,
    'times': operator.mul,
    'divided by': operator.truediv,
}

RESULT_PREFIX = 'the result of '

def normalize_line(line):
    return line.lower()

def process_line(line):
    line = normalize_line(line)
    return format_result(evaluate_expression(line))

def format_result(result):
    if result == int(result):
        return int(result)
    return round(result, 2)

def evaluate_expression(expression):
    expression = expression.strip()
    if expression.startswith(RESULT_PREFIX):
        expression = expression[len(RESULT_PREFIX):]

    for op_name, op_func in OPERATORS.items():
        for separator in [f', {op_name} {RESULT_PREFIX}', f' {op_name} {RESULT_PREFIX}']:
            if separator in expression:
                parts = expression.split(separator)
                left_val = evaluate_expression(parts[0])
                right_val = evaluate_expression(parts[1])
                return op_func(left_val, right_val)

    if ', ' in expression:
        parts = expression.split(', ')
        left = parts[0]
        rest = parts[1]
        left_val = evaluate_expression(left)
        for op_name, op_func in OPERATORS.items():
            if rest.startswith(op_name + ' '):
                right_val = evaluate_expression(rest[len(op_name) + 1:])
                return op_func(left_val, right_val)

    for op_name, op_func in OPERATORS.items():
        separator = f' {op_name} '
        if separator in expression:
            parts = expression.split(separator)
            left_val = evaluate_expression(parts[0])
            right_val = evaluate_expression(parts[1])
            return op_func(left_val, right_val)

    return parse_number(expression)

calc_simple = evaluate_expression
