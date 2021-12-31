from and_gate import AndGate
from xor_gate import XorGate
from or_gate import OrGate

class FullAdder:
    def __init__(self):
        self.xor_gate1 = XorGate()
        self.xor_gate2 = XorGate()
        self.and_gate1 = AndGate()
        self.and_gate2 = AndGate()
        self.or_gate = OrGate()

    @property
    def output(self):
        return self.xor_gate2.output, self.or_gate.output

    def set_pins(self, voltage_a, voltage_b, voltage_c):
        self.xor_gate1.set_pins(voltage_a, voltage_b)
        self.xor_gate2.set_pins(self.xor_gate1.output, voltage_c)
        self.and_gate1.set_pins(self.xor_gate1.output, voltage_c)
        self.and_gate2.set_pins(voltage_a, voltage_b)
        self.or_gate.set_pins(self.and_gate1.output, self.and_gate2.output)

    def __str__(self):
        sum_bit, carry_bit = self.output
        return f"FULL ADDER |{self.xor_gate1.pin_a.voltage} {self.xor_gate1.pin_b.voltage}| -> CARRY: {carry_bit} SUM: {sum_bit} "