from machine import TuringMachine
from machine import Tape

def read_machine(file_path):
	with open(file_path) as file:
		line = file.readline().split()

		number_of_states = int(line[1])
		states = []
		alphabet = []
		transitions = dict()


		for index in range(number_of_states):
			line = file.readline().split()
			states.append(line[0])

			if len(line) > 1:
				if line[1] == '+':
					accept_state = line[0]

				if line[1] == '-':
					reject_state = line[0]

		line = file.readline().split()
		
		alphabet_size = int(line[1])

		for index in range(alphabet_size):
			alphabet.append(line[2 + index])

		line = file.readline().split()

		while line != []:
			transitions[(line[0], line[1])] = (line[2], line[3], line[4])
			line = file.readline().split()	

		return TuringMachine(states[0], accept_state, reject_state, transitions)

def read_tape(file_path):
	with open(file_path) as file:
		line = file.readline().split()
		
		return Tape(list(line[0]))
