from and_gate import AndGate
from not_gate import NotGate
from connector import Connector

class NandGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()
        self.connector = Connector()

    @property
    def output(self):
        self.connector.connect(self.and_gate.output, self.not_gate.pin_a)
        return self.not_gate.output

    def set_pins(self, voltage_a, voltage_b):
        self.and_gate.pin_a.voltage = voltage_a
        self.and_gate.pin_b.voltage = voltage_b

    def __str__(self):
        return f"NAND |{self.and_gate.pin_a.voltage} {self.and_gate.pin_b.voltage}| -> {self.output}"