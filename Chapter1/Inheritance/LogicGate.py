class LogicGate(object):
    """This class is the base class for all logic gates and
        has two characteristics, label and an output line as
        these are the only common ones."""

    def __init__(self, n):
        self.label = n
        self.output = None

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    def getLabel(self):
        return self.label
