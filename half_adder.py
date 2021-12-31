from and_gate import AndGate
from xor_gate import XorGate

class HalfAdder:
    def __init__(self):
        self.xor_gate = XorGate()
        self.and_gate = AndGate()

    @property
    def output(self):
        return self.xor_gate.output, self.and_gate.output

    def set_pins(self, voltage_a, voltage_b):
        self.xor_gate.set_pins(voltage_a, voltage_b)
        self.and_gate.set_pins(voltage_a, voltage_b)

    def __str__(self):
        sum_bit, carry_bit = self.output
        return f"HALF ADDER |{self.and_gate.pin_a.voltage} {self.and_gate.pin_b.voltage}| -> CARRY: {carry_bit} SUM: {sum_bit} "