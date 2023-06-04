import subprocess

def test_main(input_file, output_file):
    with open(input_file, 'r') as inFile, open(output_file, 'r') as outFile:
        input_data = inFile.read()
        expected_output_data = outFile.read().strip()

        process = subprocess.Popen(['python', '_static/cs515_challenges/Week1/Challenge10/two_strings.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        output_data, _ = process.communicate(input_data)
        output_data = output_data.strip()

        if output_data == expected_output_data:
            return "PASSED"
        else:
            return "FAILED"

if __name__ == "__main__":
    for i in range(1, 3):
        input_file = f"_static/cs515_challenges/Week1/Challenge10/test{i}.in"
        output_file = f"_static/cs515_challenges/Week1/Challenge10/test{i}.out"
        print(f"Test {i}: {test_main(input_file, output_file)}")