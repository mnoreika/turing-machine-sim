import sys

from parser import read_tape
from parser import read_machine

turing_machine = read_machine(sys.argv[1])
tape = read_tape(sys.argv[2])

turing_machine.tape = tape

if (len(sys.argv) > 3 and sys.argv[3] == "-d"):
	turing_machine.debug_on = True

result = turing_machine.simulate()

print (result)

if (len(sys.argv) > 3 and sys.argv[3] == "-t"):
	print (turing_machine.tape.cells)