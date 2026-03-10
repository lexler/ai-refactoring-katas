import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import calculate, evaluate_expression


class TestEvaluateExpression(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate_expression('one plus three'), 4)
        self.assertEqual(evaluate_expression('five plus five'), 10)

    def test_subtraction(self):
        self.assertEqual(evaluate_expression('eight minus two'), 6)
        self.assertEqual(evaluate_expression('ten minus one'), 9)

    def test_multiplication(self):
        self.assertEqual(evaluate_expression('three times three'), 9)
        self.assertEqual(evaluate_expression('six times five'), 30)

    def test_division(self):
        self.assertEqual(evaluate_expression('six divided by two'), 3)
        self.assertAlmostEqual(evaluate_expression('three divided by nine'), 0.333, places=2)

    def test_single_number_returns_itself(self):
        self.assertEqual(evaluate_expression('five'), 5)
        self.assertEqual(evaluate_expression('10'), 10)

    def test_precedence_with_comma(self):
        self.assertEqual(evaluate_expression('four plus one, minus five'), 0)
        self.assertEqual(evaluate_expression('three times three, divided by two'), 4.5)
        self.assertEqual(evaluate_expression('two times three, plus one'), 7)
        self.assertEqual(evaluate_expression('five plus two, times three'), 21)


class TestCalculate(unittest.TestCase):

    def test_simple_addition(self):
        self.assertEqual(calculate('one plus three'), 4)

    def test_simple_subtraction(self):
        self.assertEqual(calculate('eight minus two'), 6)

    def test_division_with_decimal(self):
        result = calculate('three divided by nine')
        self.assertEqual(result, 0.33)
        self.assertIsInstance(result, float)

    def test_division_returning_integer(self):
        result = calculate('six divided by two')
        self.assertEqual(result, 3)
        self.assertIsInstance(result, int)

    def test_comma_precedence_minus(self):
        self.assertEqual(calculate('the result of four plus one, minus five'), 0)

    def test_comma_precedence_divided(self):
        self.assertEqual(calculate('The result of three times three, divided by two'), 4.5)

    def test_compound_minus(self):
        self.assertEqual(calculate('six times five minus the result of nine times two'), 12)

    def test_compound_both_sides(self):
        self.assertEqual(calculate('the result of ten plus three, minus the result of one plus seven'), 5)

    def test_compound_both_sides_plus(self):
        self.assertEqual(calculate('the result of two plus three, plus the result of one plus four'), 10)

    def test_compound_plus(self):
        self.assertEqual(calculate('six plus the result of two times three'), 12)

    def test_compound_both_sides_times(self):
        self.assertEqual(calculate('the result of two plus three, times the result of one plus one'), 10)

    def test_compound_times(self):
        self.assertEqual(calculate('three times the result of two plus two'), 12)

    def test_compound_divided(self):
        self.assertEqual(calculate('six divided by the result of one plus one'), 3)

    def test_compound_both_sides_divided(self):
        self.assertEqual(calculate('the result of ten plus two, divided by the result of one plus one'), 6)

    def test_comma_precedence_with_compound_divisor(self):
        self.assertEqual(calculate('six plus four, divided by the result of one plus one'), 5)

    def test_case_insensitive(self):
        self.assertEqual(calculate('ONE PLUS THREE'), 4)
        self.assertEqual(calculate('The Result Of Three Times Three, Divided By Two'), 4.5)

    def test_strips_result_of_prefix(self):
        self.assertEqual(
            calculate('the result of one plus three'),
            calculate('one plus three'))

    def test_zero_operations(self):
        self.assertEqual(calculate('zero plus five'), 5)
        self.assertEqual(calculate('ten minus zero'), 10)
        self.assertEqual(calculate('zero times five'), 0)

    def test_division_by_non_zero(self):
        self.assertEqual(calculate('ten divided by two'), 5)
        self.assertEqual(calculate('ten divided by three'), 3.33)

    def test_same_number_operations(self):
        self.assertEqual(calculate('five plus five'), 10)
        self.assertEqual(calculate('five minus five'), 0)
        self.assertEqual(calculate('five times five'), 25)
        self.assertEqual(calculate('five divided by five'), 1)


if __name__ == '__main__':
    unittest.main()
