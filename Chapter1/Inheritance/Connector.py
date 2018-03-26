class Connector:

    def __init__(self, fgate, tgate):
        self.fromGate = fgate
        self.toGate = tgate

        tgate = self.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate "+self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate "+self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()
