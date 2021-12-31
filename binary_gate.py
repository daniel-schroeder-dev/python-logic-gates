from logic_gate import LogicGate
from pin import Pin

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.pin_a = Pin(label)
        self.pin_b = Pin(label)
    
    def __str__(self):
        return f"{self.label:3} GATE |{self.pin_a.voltage:<2} {self.pin_b.voltage:<2}| -> {self.output}"

    def set_pins(self, voltage_a, voltage_b):
        self.pin_a.voltage = voltage_a
        self.pin_b.voltage = voltage_b