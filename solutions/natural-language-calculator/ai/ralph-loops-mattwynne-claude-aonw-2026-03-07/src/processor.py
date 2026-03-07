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
    line = line.lower()
    if line.startswith(RESULT_PREFIX):
        line = line[len(RESULT_PREFIX):]
    return line

def process_line(line):
    line = normalize_line(line)
    result = try_nested_result_of(line)
    if result is None:
        result = evaluate_expression(line)
    return format_result(result)

def try_nested_result_of(line):
    for op_name, op_func in OPERATORS.items():
        for separator in [f', {op_name} the result of ', f' {op_name} the result of ']:
            if separator in line:
                parts = line.split(separator)
                left_val = evaluate_expression(parts[0])
                right_val = evaluate_expression(parts[1])
                return op_func(left_val, right_val)
    return None

def format_result(result):
    if result == int(result):
        return int(result)
    return round(result, 2)

def evaluate_expression(expression):
    expression = expression.strip()

    if ', ' in expression:
        parts = expression.split(', ')
        left = parts[0]
        rest = parts[1]
        left_val = evaluate_expression(left)
        for op_name, op_func in OPERATORS.items():
            if rest.startswith(op_name + ' '):
                right_val = parse_number(rest[len(op_name) + 1:])
                return op_func(left_val, right_val)

    for op_name, op_func in OPERATORS.items():
        separator = f' {op_name} '
        if separator in expression:
            parts = expression.split(separator)
            num1 = parse_number(parts[0].strip())
            num2 = parse_number(parts[1].strip())
            return op_func(num1, num2)

    return parse_number(expression)

calc_simple = evaluate_expression
