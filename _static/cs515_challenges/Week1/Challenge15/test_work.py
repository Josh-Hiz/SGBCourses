import sys
import unittest
from unittest import TestCase
from unittest.mock import patch
import work
sys.path.append('Challenge15/')

class TestProgram(TestCase):
    @patch('builtins.input', side_effect=['8 10'])
    def test_is_enough_time(self, mock_input):
        expected_output = "True\n"
        self.assertEqual(work.main(), expected_output)

    @patch('builtins.input', side_effect=['10 8'])
    def test_is_not_enough_time(self, mock_input):
        expected_output = "False\n"
        self.assertEqual(work.main(), expected_output)

unittest.main()