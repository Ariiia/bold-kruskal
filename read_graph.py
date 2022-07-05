V = 100000
E = 150000
THREADS = 8


test = "graph_ex.txt"
filename = "input_graph_"+str(V)+"_"+str(E) +".txt"
def read_graph():
    global E, V
    lines = []
    graph = []
    vertices = []
    with open(filename) as f:
        lines = f.readlines()
    E = len(lines)
    print(E)
    
    for line in lines:
        x, y, cost = line.split(" ")
        cost = cost.strip('\n') 
        graph.append([int(cost),int(x),int(y)])
    V = V
    return graph, E, V   


if __name__ == "__main__":
    graph, E, V = read_graph()
    print(graph)

    print(E, V)
    