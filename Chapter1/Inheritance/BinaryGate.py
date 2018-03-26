from LogicGate import LogicGate

class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None # similar to line 1 and line 2
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
