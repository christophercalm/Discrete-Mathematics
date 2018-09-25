# Christopher Calmes
# 02/10/2018
# Program to compute the greatest common denominator 
# and lowest common multiple.
# Written in python 3.5.3


# Uses euclidean algorithmn to find gcd
def findGcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    else:
        return(findGcd(b, a % b))
                
def main():
    x,y = eval(input("Enter two positive integers separated by a comma: "))
    gcd = findGcd(x,y)
    print("The greatest common denominator of", x, "and", y, "is:", gcd)
    lcm = (x * y) / gcd 
    print("The lowest common multiple is: ", lcm)

if __name__ == "__main__":
    main()
