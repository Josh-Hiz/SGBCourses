import unittest, sys
from io import StringIO
import challenge as task

class TestName(unittest.TestCase):
    def get_stdout(self, lst):
        # Save the original stdout and replace it with StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        task.multiplication_tables(lst)
        # Retrieve the captured output and restore the original stdout
        captured_output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        return captured_output
    
    def correct(self, test_output, expected_output):
        self.assertEqual(str(test_output).strip(), str(expected_output).strip())
    
    def test_challenge_1(self):
        self.correct(self.get_stdout(3), "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]\n")

    def test_challenge_2(self):
        self.correct(self.get_stdout(1), "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n")
    
    def test_challenge_3(self):
        self.correct(self.get_stdout(7),"[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]\n[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]\n[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]\n[6, 12, 18, 24, 30, 36, 42, 48, 54, 60]\n[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]\n")
    
unittest.main(exit=False)


