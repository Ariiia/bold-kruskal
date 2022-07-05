import random
V = 10000
E = 50000


graph = []
vertices = list()
for i in range(0, V):
    vertices.append(i)
    
random.shuffle(vertices)
vertices_copy = vertices.copy()

used_vertices = list()
used_vertices.append(vertices[0])
counter = 1

#till V-1 make edges
while counter < V:
    counter+=1
    #ending with new vertice
    x = vertices.pop()
    #starting from existent one
    y = random.choice(used_vertices)
    used_vertices.append(x)
    weight = random.randint(1,100)
    graph.append(str(x) + ' '+ str(y)+ ' ' + str(weight))
    

#add cycles to the minimal connected graph till E number
vertices = vertices_copy.copy()
edge_counter = V-1
while edge_counter < E:
    edge_counter += 1
    x = random.choice(vertices)
    y = random.choice(vertices)
    if x == y:
        edge_counter -=1
        continue
    weight = random.randint(1,20)
    graph.append(str(x) + ' ' + str(y)+ ' ' + str(weight))

# print(graph)

file = "input_graph_"+str(V)+"_"+str(E)+".txt"        
with open(file, 'w') as f:
    for line in graph:
        f.write(line)
        f.write('\n')



