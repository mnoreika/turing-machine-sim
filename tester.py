import sys

from parser import read_tape
from parser import read_machine

def runTest(input, expected_output, machine):
	print (input)

turing_machine = read_machine(sys.argv[1])
test_file = sys.argv[2]

with open(test_file) as file:
	line = file.readline().split()

	while True:
		result = runTest(line[0], line[1])

		print(result)

		line = file.readline().split()