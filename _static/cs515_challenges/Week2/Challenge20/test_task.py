import unittest, types, sys
from io import StringIO
import challenge as task


class TaskTest(unittest.TestCase):
    # Test the function with a specific input
    def get_stdout(self, input_list):
        # Save the original stdout and replace it with StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        task.print_numbers(input_list)
        # Retrieve the captured output and restore the original stdout
        captured_output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        return captured_output
    
    def correct(self, test_output, expected_output):
        self.assertEqual(str(test_output).strip(), str(expected_output).strip())
    
    def test_sample1(self):
        self.correct(self.get_stdout([2,5,36,53,31]), "2\n5\n53\n31\n")
    def test_sample2(self):
        self.correct(self.get_stdout([3,6,9,12,5,2,1]), "5\n2\n1\n")
    

unittest.main(exit=False)