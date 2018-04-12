def ordinal_hashing(string, table_size):
    sum = 0
    for item in string:
        sum += ord(item)

    return sum % table_size

def ordinal_hashing_with_weight(string, table_size):
    sum = 0
    for i, item in enumerate(string):
        sum += ((i+1) * ord(item))

    return sum % table_size

print("Normal ordinal value calculation without weight")
print(ordinal_hashing("cat", 11))

print("Ordinal value calculation with weight")
print(ordinal_hashing_with_weight("cat", 11))
