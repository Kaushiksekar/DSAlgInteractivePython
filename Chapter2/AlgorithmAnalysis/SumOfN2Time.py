import time

def sumOfN2(n):
    start = time.time()

    sum = (n * (n+1))/2

    end = time.time()

    return sum, end - start

print("For 10,000 integers")

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN2(10000))

print("For 100,000 integers")

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN2(100000))

print("For 1,000,000 integers")

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN2(1000000))
