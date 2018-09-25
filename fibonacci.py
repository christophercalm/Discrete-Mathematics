#Program that outputs k number of the fibonacci sequence
#Using the recursive and explicit defintions

#Christopher Calmes
#03/20/2018

import math

def fib_recursive(k):
    #base cases
    if k == 0: 
        return 0
    elif k == 1:
        return 1 
    else:
    #recursive part
        return fib_recursive(k-1)+fib_recursive(k-2)
    

def fib_explicit(n):
    return ((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n)/ (2 ** n * math.sqrt(5))


j = eval(input("Enter the number of fibbonaci numbers to output: "))

print("Recursively...")
for i in range (j):
    print(fib_recursive(i))

print("\nExplicitly...\n")
for p in range (j):
    print(int(fib_explicit(p)))

