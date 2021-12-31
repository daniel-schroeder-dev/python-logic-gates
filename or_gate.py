from binary_gate import BinaryGate

class OrGate(BinaryGate):
    def __init__(self):
        super().__init__("OR")
    
    def calculate_output(self):
        if self.pin_a.voltage is not None and self.pin_b.voltage is not None:
            return self.pin_a.voltage or self.pin_b.voltage
        return None
