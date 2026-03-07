import operator

from number_parser import parse_number_word

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

def find_nested_operation(line):
    """Try to split line on a nested operation separator like ', plus the result of ' or ' minus the result of '.
    Returns (left_str, right_str, operator_fn) or None if no nested operation found."""
    for op_word, op_fn in OPERATORS.items():
        for separator in [', ' + op_word + ' the result of ', ' ' + op_word + ' the result of ']:
            if separator in line:
                parts = line.split(separator)
                return (parts[0], parts[1], op_fn)
    return None

def format_result(value):
    """Format a numeric result: return int if whole number, otherwise round to 2 decimal places."""
    if value == int(value):
        return int(value)
    else:
        return round(value, 2)

def evaluate(expression):
    """Evaluate a normalized natural language math expression and return a numeric result."""
    try:
        nested = find_nested_operation(expression)
        if nested:
            left_str, right_str, op_fn = nested
            left_val = evaluate_simple_expression(left_str)
            right_val = evaluate_simple_expression(right_str)
            return op_fn(left_val, right_val)
        else:
            return evaluate_simple_expression(expression)
    except (ValueError, ZeroDivisionError) as e:
        raise type(e)(f"Cannot evaluate '{expression}': {e}") from e

def process_line(line):
    expression = normalize_line(line)
    result = evaluate(expression)
    return format_result(result)

def evaluate_simple_expression(expression):
    expression = expression.strip()

    # Handle comma-separated operations (precedence)
    if ', ' in expression:
        parts = expression.split(', ')
        left = parts[0]
        rest = parts[1]
        left_val = evaluate_simple_expression(left)
        for op_word, op_fn in OPERATORS.items():
            prefix = op_word + ' '
            if rest.startswith(prefix):
                right_val = parse_number_word(rest[len(prefix):])
                return op_fn(left_val, right_val)

    # Try to parse as "X <operator> Y" (split only on first occurrence,
    # recursively evaluate the right-hand side for chained operations)
    for op_word, op_fn in OPERATORS.items():
        separator = ' ' + op_word + ' '
        if separator in expression:
            parts = expression.split(separator, 1)
            num1 = parse_number_word(parts[0].strip())
            num2 = evaluate_simple_expression(parts[1].strip())
            return op_fn(num1, num2)

    # Might be just a number
    return parse_number_word(expression)
