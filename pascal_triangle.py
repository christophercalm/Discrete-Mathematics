# Christopher
# This is a program to output pascal's triangle given n number of rows

import math

#define my own combination function
def comb(n, r):
    return (int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r))))


def main():

    rows = eval(input("Enter the number of rows: "))
    # rows 0 to rows - 1
    for i in range(rows):
        #values 0 to i
        for j in range(i + 1):
            print(comb(i,j), end = " ")
        #newline
        print("\n")

main()
