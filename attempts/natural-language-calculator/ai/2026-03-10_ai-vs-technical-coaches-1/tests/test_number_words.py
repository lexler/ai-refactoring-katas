import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from number_words import parse_number


class TestParseNumber(unittest.TestCase):

    def test_word_numbers(self):
        self.assertEqual(parse_number('zero'), 0)
        self.assertEqual(parse_number('one'), 1)
        self.assertEqual(parse_number('five'), 5)
        self.assertEqual(parse_number('ten'), 10)

    def test_word_numbers_case_insensitive(self):
        self.assertEqual(parse_number('One'), 1)
        self.assertEqual(parse_number('FIVE'), 5)
        self.assertEqual(parse_number('TEN'), 10)

    def test_digit_strings(self):
        self.assertEqual(parse_number('0'), 0)
        self.assertEqual(parse_number('5'), 5)
        self.assertEqual(parse_number('10'), 10)

    def test_whitespace_handling(self):
        self.assertEqual(parse_number('  five  '), 5)
        self.assertEqual(parse_number('\ttwo\n'), 2)

    def test_invalid_word_raises_error(self):
        with self.assertRaises(ValueError):
            parse_number('eleven')
        with self.assertRaises(ValueError):
            parse_number('abc')


if __name__ == '__main__':
    unittest.main()
