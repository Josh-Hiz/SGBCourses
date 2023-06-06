import sys
import io
import unittest

def readCode(file):
    with open(file,"r") as f:
        source_code = f.read()
    return source_code

source_code = readCode("challenge.py")

def capture_stdout():
        
    original_stdout = sys.stdout
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        exec(source_code)
    except Exception as e:
        print(f'An error occurred: {e}', file=sys.stderr)
    
    sys.stdout = original_stdout
    capture_output = buffer.getvalue()
    buffer.close()
    
    return capture_output

class TestChallenge(unittest.TestCase):

    def correct(self, stdinput, output):
        self.assertEqual(stdinput, output)
        
    def test_challenge1(self):
        self.correct(capture_stdout(), "True\n")
    def test_challenge2(self):
        self.correct(capture_stdout(), "True\n")
    def test_challenge3(self):
        self.correct(capture_stdout(), "False\n")

unittest.main(exit=False)