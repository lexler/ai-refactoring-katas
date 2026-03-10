import sys

from calculator import calculate


def main(input_file=None):
    if input_file is None:
        if len(sys.argv) < 2:
            print("Usage: natural_language_calculator.py <input_file>")
            return 1
        input_file = sys.argv[1]

    try:
        expressions = read_expressions(input_file)
    except OSError as e:
        print(f"Could not read '{input_file}': {e}")
        return 1

    try:
        results = calculate_all(expressions)
    except ValueError as e:
        print(f"Invalid expression: {e}")
        return 1

    out_file = output_filepath(input_file)
    try:
        write_results(out_file, results)
    except OSError as e:
        print(f"Could not write '{out_file}': {e}")
        return 1

    print(f"Results written to {out_file}")
    return 0


def read_expressions(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def calculate_all(expressions):
    return [calculate(expr) for expr in expressions]


def output_filepath(input_filepath):
    return input_filepath.replace('.txt', '_results.txt')


def write_results(filepath, results):
    with open(filepath, 'w') as f:
        for result in results:
            f.write(str(result) + '\n')


if __name__ == "__main__":
    sys.exit(main())
