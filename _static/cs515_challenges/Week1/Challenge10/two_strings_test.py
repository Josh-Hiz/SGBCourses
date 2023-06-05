import subprocess
import sys 
def test_case(contents,expected_output):
    process = subprocess.Popen([sys.executable, '_static/cs515_challenges/Week1/Challenge10/challenge.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    output, error = process.communicate(input=contents)

    if error:
        print("Error:", error)
        return False
    
    processed_output = str(output).strip().lower()
    processed_expected_output = str(expected_output).strip().lower()
    
    if processed_output == processed_expected_output:
        print(f"Test Case '{expected_output}': PASSED")
        return True
    else:
        print("Test Case FAILED")
        print("Expected Output:")
        print(expected_output)
        print("Actual Output:")
        print(output)
        return False

if __name__ == "__main__":
    test_case("a\nb","a,b")
    test_case("10\nsixty six","10,sixty six")
    test_case("hello\nthere","hello,there")
    test_case("once upon a time\nin fairy land","once upon a time,in fairy land")