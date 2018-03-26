from BinaryGate import BinaryGate

class OrGate(BinaryGate):

    def __init__(self, n):
        #super(OrGate, self).__init__(self, n)
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a==1 or b==1:
            return 1
        else:
            return 0
