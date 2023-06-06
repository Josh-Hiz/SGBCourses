import sys
import io
import unittest

print("Check the following inputs:\n'a,b'\n'10,sixty six'\n'hello,there'\n'once upon a time,in a fairyland'\n")

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

class TestTwoStrings(unittest.TestCase):

    def correct(self, stdinput, output):
        self.assertEqual(stdinput, output)
        
    def test_challenge1(self):
        self.correct(capture_stdout(), "a,b\n")
    def test_challenge2(self):
        self.correct(capture_stdout(), "10,sixty six\n")
    def test_challenge3(self):
        self.correct(capture_stdout(), "hello,there\n")
    def test_challenge4(self):
        self.correct(capture_stdout(), "once upon a time,in a fairyland\n")

unittest.main(exit=False)