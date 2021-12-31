from nor_gate import NorGate
from connector import Connector

class XorGate:
    def __init__(self):
        self.nor1 = NorGate()
        self.nor2 = NorGate()
        self.nor3 = NorGate()
        self.nor4 = NorGate()
        self.nor5 = NorGate()
        self.connector1 = Connector()
        self.connector2 = Connector()
        self.connector3 = Connector()
        self.connector4 = Connector()
    
    @property
    def output(self):
        self.connector1.connect(self.nor1.output, self.nor4.pin_a)
        self.connector2.connect(self.nor2.output, self.nor4.pin_b)
        self.connector3.connect(self.nor4.output, self.nor5.pin_a)
        self.connector4.connect(self.nor3.output, self.nor5.pin_b)
        return self.nor5.output

    @property
    def pin_a(self):
        return self.nor1.pin_a

    @property
    def pin_b(self):
        return self.nor2.pin_a

    def set_pins(self, voltage_a, voltage_b):
        self.nor1.pin_a.voltage = voltage_a
        self.nor1.pin_b.voltage = voltage_a
        self.nor2.pin_a.voltage = voltage_b
        self.nor2.pin_b.voltage = voltage_b
        self.nor3.pin_a.voltage = voltage_b
        self.nor3.pin_b.voltage = voltage_a

    def __str__(self):
        return f"XOR |{self.nor1.pin_a.voltage} {self.nor2.pin_b.voltage}| -> {self.output}"