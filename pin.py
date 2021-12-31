class Pin:
    def __init__(self, gate_label):
        self.gate_label = gate_label
        self.voltage = 0

    def __str__(self):
        return f"PIN {self.gate_label} -> {self.voltage}"
    
