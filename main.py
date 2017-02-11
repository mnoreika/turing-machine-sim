import sys

from parser import read_tape
from parser import read_machine

turing_machine = read_machine(sys.argv[1])
tape = read_tape(sys.argv[2])

turing_machine.tape = tape

result = turing_machine.simulate()

print (result)
