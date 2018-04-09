"""This module has a function called to_str which takes two inputs number and
    base and return a string of the number in the given base"""
def to_str(number, base):
    """This function takes two inputs number and base and return a string of the
    number in the given base"""
    conversion_string = "0123456789ABCDEF"

    if number < base:
        return conversion_string[number]
    else:
        return to_str(number//base, base) + conversion_string[number%base]

print(to_str(10, 2))
