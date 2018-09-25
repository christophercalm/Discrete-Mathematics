"""
Program to check if a connected graph has a hamiltonian circuit
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

    print(graph)
    print("The number of edges is: "+ (num_edges(graph, rows, cols)))

    theorem_2_nam = ((1/2) * ((rows**2 - (3 * rows)) + 6))
    if num_edges(graph,rows, cols) >= theorem_2_nam:
        print("The graph is a hamiltonian circuit!")
    else:
        print("It cannot be determined by theorem 2 if the graph is a hamiltonian circuit")


def num_edges(graph, rows, cols):
    edges = 0
    for i in range(rows):
        for j in range(cols):
            if graph[i-1][j-1] == 1:
                edges += 1
    return edges // 2

main()

