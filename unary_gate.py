from logic_gate import LogicGate 
from pin import Pin

class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = Pin(label)

    def __str__(self):
        return f"{self.label:3} GATE |{self.pin_a.voltage:<5}| -> {self.output}"
