class Fraction:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        newnum = self.num * other.denom + self.denom * other.num
        newdenom = self.denom * other.denom
        return Fraction(newnum, newdenom)

    def __eq__(self, other):
        firstnum = self.num * other.denom
        secondnum = self.denom * other.num
        return firstnum == secondnum

fraction1 = Fraction(3, 5)
fraction2 = Fraction(2, 6)
print(fraction1 + fraction2)
print(fraction1 == fraction2)
fraction1 = Fraction(3, 5)
fraction2 = Fraction(3, 5)
print(fraction1 == fraction2)
