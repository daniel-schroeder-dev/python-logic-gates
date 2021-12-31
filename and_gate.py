from binary_gate import BinaryGate 

class AndGate(BinaryGate):
    def __init__(self):
        super().__init__("AND")
    
    def calculate_output(self):
        if self.pin_a.voltage is not None and self.pin_b.voltage is not None:
            return self.pin_a.voltage and self.pin_b.voltage
        return None

