class LogicGate:
    def __init__(self, label):
        self.label = label
        self._output = 0
    
    @property 
    def output(self):
        self._output = self.calculate_output()
        return self._output
    
    def calculate_output(self):
        pass
