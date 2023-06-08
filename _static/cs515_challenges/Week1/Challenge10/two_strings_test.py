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
        self.correct(self.get_stdout(["a","b"]), "a,b")

    def test_challenge_2(self):
        self.correct(self.get_stdout(["10","sixty six"]), "10,sixty six")

    def test_challenge_3(self):
        self.correct(self.get_stdout(["hello","there"]), "hello,there")
        
    def test_challenge_4(self):
        self.correct(self.get_stdout(["once upon a time","in fairyland"]), "once upon a time,in fairyland")
    fileRunner.close()
    
unittest.main(exit=False)