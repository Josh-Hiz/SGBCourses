import unittest, types, sys
from io import StringIO
import challenge as task


class TaskTest(unittest.TestCase):
    # Test the function with a specific input
    def get_stdout(self, input_list):
        # Save the original stdout and replace it with StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        task.print_emails(input_list)
        # Retrieve the captured output and restore the original stdout
        captured_output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        return captured_output
    
    def correct(self, test_output, expected_output):
        self.assertEqual(str(test_output).strip(), str(expected_output).strip())
    
    def test_sample1(self):
        self.correct(self.get_stdout({"ucsd.edu" : ["annie","joseph","savitha"], "gmail.com" : ["ben10","annie","dio"], "aol.com" : ["joseph", "hotmail", "coda"]}), 
                     'annie@ucsd.edu\njoseph@ucsd.edu\nsavitha@ucsd.edu\nben10@gmail.com\nannie@gmail.com\ndio@gmail.com\njoseph@aol.com\nhotmail@aol.com\ncoda@aol.com\n')


unittest.main(exit=False)