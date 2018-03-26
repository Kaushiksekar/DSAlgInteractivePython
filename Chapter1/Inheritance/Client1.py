from AndGate import AndGate
from OrGate import OrGate
from NotGate import NotGate

andGate = AndGate("And")
print(andGate.getOutput())

orGate = OrGate("Or")
print(orGate.getOutput())

notGate = NotGate("Not")
print(notGate.getOutput())
