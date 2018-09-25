"""
Program to check if a connected graph is regular
Christopher Calmes
05/3/2018
Discrete mathematics
"""

def main():

    cols = eval(input("Enter the number of columns: "))
    rows = eval(input("Enter the number of rows: "))

    # creates empty graph
    graph = [[0 for x in range(cols)] for y in range(rows)]

    for i in range(rows):
        for j in range(cols):
            graph[i][j]= eval(input("Enter the #" + str(i + 1) + " element in row "  + str(j + 1) + ": " ))

    num_edges_in_row = 0

    #first row to compare it to
    for i in range(rows):
        num_edges_in_row += graph[i][0]

    is_regular = True

    # compare each row. If it has the same amount of ones in each other row then it is regular
    for i in range(rows):
        num = 0
        for j in range(cols):
            num += graph[i][j]
        if num != num_edges_in_row:
            is_regular = False
            break

    if is_regular:
        print("This graph is regular")
    else:
        print("This graph is not regular")

main()

