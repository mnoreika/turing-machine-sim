class Tape():

	def __init__(self, cells):
		self.cells = cells
		self.head = 0

	def write(self, symbol):
		self.cells[self.head] = symbol

	def read(self):
		if self.head == len(self.cells):
			self.cells.append("_")


		return self.cells[self.head]

	def move_left(self):
		if self.head > 0:
			self.head -= 1
		else:
			self.head = 0

	def move_right(self):
		self.head += 1	

	def move(self, direction):
		if (direction == 'L'):
			self.move_left()

		if (direction == 'R'):
			self.move_right()		


class TuringMachine():
	def __init__(self, start_state, accept_state, reject_state, transitions):
		self.start_state = start_state
		self.accept_state = accept_state
		self.reject_state = reject_state
		self.transitions = transitions

	def transition(self):
		input = (self.current_state, self.tape.read())

		output = self.transitions[input]

		self.current_state = output[0]

		self.tape.write(output[1])

		self.tape.move(output[2])

	def simulate(self):
		self.current_state = self.start_state
		
		while True:
			self.transition()

			if self.current_state == self.accept_state:
				return "ACCEPTED"

			if self.current_state == self.reject_state:
				return "REJECTED"





