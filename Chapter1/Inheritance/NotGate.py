from UnaryGate import UnaryGate

class NotGate(UnaryGate):

    def __init__(self, n):
        #super(NotGate, self).__init__(self, n)
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPin()

        if a==0:
            return 1
        else:
            return 0
