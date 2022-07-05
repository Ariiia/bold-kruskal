from read_graph import read_graph, V

def find(root_group, i):
    #to which group v belongs
    if root_group[i] != i:
        return find(root_group, root_group[i])
    return i

def union(group, sub_v, a, b):
    #unite two groups check which is longer and eat other
    if sub_v[a] < sub_v[b]:
        group[a] = b
        sub_v[b]+=1
        sub_v[a]=0
    elif sub_v[a] > sub_v[b]:
        group[b] = a
        sub_v[a]+=1
        sub_v[b]=0
    else:
        group[b] = a
        sub_v[a] += 1

def seq_MST(graph):
    mst = []
    total_cost = 0
    edge_count = 0 #i - graph index, e - edge count
    graph_it = 0
    
    #seq sorting

    graph = sorted(graph)

    group = []
    sub_v = []
    for each in range(V):
        
        group.append(each) #how much subvertices it has
        sub_v.append(0)


    while edge_count < V - 1:
        cost, A, B = graph[graph_it]
        graph_it += 1
        x = find(group, A)
        y = find(group, B)
        #if group parents do not match, add edge between
        if x != y:
            edge_count += 1
            mst.append([cost, A, B])
            total_cost += cost
            union(group, sub_v, x, y)
    return mst, total_cost

def output(mst, total_cost):
    for edge in mst:
        print(edge)
    print(total_cost)

if __name__ == "__main__":
    graph,E,V = read_graph()
    print(graph)
    #зробити замір
    mst, total_cost = seq_MST(graph)
    #зробити замір
    output(mst, total_cost)
