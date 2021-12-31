from nand_gate import NandGate
from nor_gate import NorGate
from xor_gate import XorGate
from half_adder import HalfAdder
from full_adder import FullAdder

nand_gate = NandGate()

nand_gate.set_pins(0, 0)
print(nand_gate)

nand_gate.set_pins(0, 1)
print(nand_gate)

nand_gate.set_pins(1, 0)
print(nand_gate)

nand_gate.set_pins(1, 1)
print(nand_gate)

print()

nor_gate = NorGate()

nor_gate.set_pins(0, 0)
print(nor_gate)

nor_gate.set_pins(0, 1)
print(nor_gate)

nor_gate.set_pins(1, 0)
print(nor_gate)

nor_gate.set_pins(1, 1)
print(nor_gate)

print()

xor_gate = XorGate()

xor_gate.set_pins(0, 0)
print(xor_gate)

xor_gate.set_pins(0, 1)
print(xor_gate)

xor_gate.set_pins(1, 0)
print(xor_gate)

xor_gate.set_pins(1, 1)
print(xor_gate)

print()


half_adder = HalfAdder()

half_adder.set_pins(0, 0)
print(half_adder)

half_adder.set_pins(0, 1)
print(half_adder)

half_adder.set_pins(1, 0)
print(half_adder)

half_adder.set_pins(1, 1)
print(half_adder)

print()



full_adder = FullAdder()

full_adder.set_pins(0, 0, 0)
print(full_adder)

full_adder.set_pins(0, 0, 1)
print(full_adder)

full_adder.set_pins(0, 1, 0)
print(full_adder)

full_adder.set_pins(0, 1, 1)
print(full_adder)

full_adder.set_pins(1, 0, 0)
print(full_adder)

full_adder.set_pins(1, 0, 1)
print(full_adder)

full_adder.set_pins(1, 1, 0)
print(full_adder)

full_adder.set_pins(1, 1, 1)
print(full_adder)

print()


