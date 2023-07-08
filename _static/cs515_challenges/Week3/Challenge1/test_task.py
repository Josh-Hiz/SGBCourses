import sys
from io import StringIO
import unittest

challengeFile = 'challenge.py'
fileRunner = open(challengeFile)
code = fileRunner.read()

class TestName(unittest.TestCase):
    def get_stdout(self, inputs):
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        test_inputs = inputs
        sys.stdin = StringIO('\n'.join(test_inputs))
        sys.stdout = StringIO()      
        exec(code)
        script_output = sys.stdout.getvalue()
        sys.stdin = original_stdin
        sys.stdout = original_stdout
        return script_output
    
    def correct(self, test_output, expected_output):
        self.assertEqual(str(test_output).strip(), str(expected_output).strip())
    
    def test_challenge_1(self):
        self.correct(self.get_stdout(["25"]), "Enter a floating point number: The square root of 25.0 is 5.0.")

    def test_challenge_2(self):
        self.correct(self.get_stdout(["lol","-1","10.0"]), "Enter a floating point number: 'lol' is not a floating point number.\nEnter a floating point number: '-1.0' doesn't have a (real) square root.\nEnter a floating point number: The square root of 10.0 is 3.1622776601683795.\n")

    fileRunner.close()
    
unittest.main(exit=False)