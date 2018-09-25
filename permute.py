#Program That accepts a positive integer n >= 2
#And returns n permute 2 and all of the permutations of the set

#Christopher Calmes
#03/06/2018

n = eval(input("Enter a positive integer >= 2: "))
if n < 2:
    print("Bad input")
    exit()

perm = []

#main Loop
for x in range(n):
    for y in range(n):
        if x != y:
            perm.append((x+1,y+1))

will_print = True

#ouput handling
if len(perm) >= 20:
    want_print = input("The output will be very large, do you wish to print? Y/N: ")
    if want_print.lower() == 'n':
        will_print = False

if will_print:
    for elem in perm:
        print (elem[0],elem[1]) #access elements in tuple
    else:
        exit()
