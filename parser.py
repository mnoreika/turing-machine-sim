import sys

from machine import TuringMachine
from machine import Tape

def read_machine(file_path):
	try:
		with open(file_path) as file:
			line = file.readline().split()

			number_of_states = int(line[1])
			states = []
			alphabet = []
			transitions = dict()
			accept_state = None
			reject_state = None


			for index in range(number_of_states):
				line = file.readline().split()
				states.append(line[0])

				if len(line) > 1:
					if line[1] == '+':
						if (accept_state == None):
							accept_state = line[0]
						else:
							raise ValueError("Turing machine can only have one accept state.")

					if line[1] == '-':
						if (reject_state == None):
							reject_state = line[0]
						else:
							raise ValueError("Turing machine can only have one reject state.")

			line = file.readline().split()
			
			alphabet_size = int(line[1])

			for index in range(alphabet_size):
				alphabet.append(line[2 + index])

			line = file.readline().split()

			while line != []:
				if line[0] in states:
					transitions[(line[0], line[1])] = (line[2], line[3], line[4])
				else:
					print (line[0], states)
					raise ValueError("Error in transision table: transitions are only possible from specified states.")
					sys.exit(1)

				line = file.readline().split()	

			return TuringMachine(states[0], accept_state, reject_state, transitions)
	except Exception as e:
		print("Invalid Turing machine description:")	
		print (e)
		sys.exit(0)	

def read_tape(file_path):
	with open(file_path) as file:
		line = file.readline().split()
		
		return Tape(list(line[0]))
