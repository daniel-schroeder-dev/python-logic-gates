from or_gate import OrGate
from not_gate import NotGate
from connector import Connector

class NorGate:
    def __init__(self):
        self.or_gate = OrGate()
        self.not_gate = NotGate()
        self.connector = Connector()
    
    @property
    def output(self):
        self.connector.connect(self.or_gate.output, self.not_gate.pin_a)
        return self.not_gate.output

    @property
    def pin_a(self):
        return self.or_gate.pin_a

    @property
    def pin_b(self):
        return self.or_gate.pin_b

    def set_pins(self, voltage_a, voltage_b):
        self.or_gate.pin_a.voltage = voltage_a
        self.or_gate.pin_b.voltage = voltage_b

    def __str__(self):
        return f"NOR |{self.or_gate.pin_a.voltage} {self.or_gate.pin_b.voltage}| -> {self.output}"