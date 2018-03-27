import time

def sumOfN(n):

    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    end = time.time()

    return theSum, end - start

print("For 10,000 integers")

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN(10000))

print("For 100,000 integers")

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN(100000))

print("For 1,000,000 integers")

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN(1000000))
