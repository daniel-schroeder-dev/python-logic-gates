from unary_gate import UnaryGate

class NotGate(UnaryGate):
    def __init__(self):
        super().__init__("NOT")

    def calculate_output(self):
        if self.pin_a.voltage is not None:
            return int(not self.pin_a.voltage)
        return None