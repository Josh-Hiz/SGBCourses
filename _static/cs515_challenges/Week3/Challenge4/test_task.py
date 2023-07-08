import unittest, sys
from io import StringIO
import challenge as task


class TaskTest(unittest.TestCase):
    # Test the function with a specific input
    def get_stdout(self, lst1, lst2):
        # Save the original stdout and replace it with StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        task.predict(lst1, lst2)
        # Retrieve the captured output and restore the original stdout
        captured_output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        return captured_output
    
    def correct(self, test_output, expected_output):
        self.assertEqual(str(test_output).strip(), str(expected_output).strip())
    
    def test_sample1(self):
        self.correct(self.get_stdout([12508, 9969, 310595, 57409],[100, 200, 300]), "[12608, 10069, 310695, 57509]\n[12808, 10269, 310895, 57709]\n[13108, 10569, 311195, 58009]\n")
    def test_sample2(self):
        self.correct(self.get_stdout([12508, 9969, 310595, 57409],[1000, 2000, 3000, 4000]), '[13508, 10969, 311595, 58409]\n[15508, 12969, 313595, 60409]\n[18508, 15969, 316595, 63409]\n[22508, 19969, 320595, 67409]\n')
    def test_sample3(self):
        self.correct(self.get_stdout([12508, 9969, 310595, 57409],[10000]), "[22508, 19969, 320595, 67409]\n")

unittest.main(exit=False)

