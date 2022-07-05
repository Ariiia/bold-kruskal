from read_graph import read_graph, E, V, THREADS
from concurrent.futures import ThreadPoolExecutor
import math
from threading import Event, Lock
#from multithreading 

event = Event()
lock = Lock()


#share group
#global discardable variables: 1 -- discard, 0 -- ok
group = []
main_count = 0
helper_discard = []

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

def par_MST(graph):
    mst = []
    #final cost of the mst 
    total_cost = 0
    global group
    global helper_discard
    sub_v = []

    #sorting    
    graph = sorted(graph)
    
    for each in range(V):
        group.append(each)
        sub_v.append(0) #how much subvertices it has
        
    for each in range(E):
        helper_discard.append(0)

    
    #main_future = executor.submit(main_mst, graph, group, sub_v)
    #main_future = Thread()
    
    with ThreadPoolExecutor(max_workers = THREADS) as executor:
        #chunk data
        
        chunk = int(math.ceil(float(len(graph)) / THREADS))
        print("chunk"+str(chunk))
        #перший чанк віддати мейну
        #main_future = executor.submit(main_mst, graph, group, sub_v)

        main_future = executor.submit(main_mst, graph, group, sub_v)
        futures = [executor.submit(helper_find_cycle, graph[(i+1) * chunk : (i + 2) * chunk],  (i+1) * chunk, (i + 2) * chunk, event) for i in range(THREADS-1)]
        #main_future = executor.submit(main_mst, graph, group, sub_v)
       
        p = 0
        for future in futures:
            p+=1
            if main_count >= (p)*chunk:
                future.cancel()
                event.set()
                event.clear()
        mst, total_cost = main_future.result()

    return mst, total_cost
    
def main_mst(graph, group, sub_v):
    mst = []
    graph_it = 0
    total_cost = 0
    global main_count
    while len(mst) != V - 1:
        main_count+=1

        if helper_discard[graph_it] == 1:
            continue
        cost, A, B,  = graph[graph_it]
        graph_it += 1
        x = find(group, A)
        y = find(group, B)
        #якщо батьки не співпадають, то циклу не буде
        if x != y:
            mst.append([cost, A, B])
            total_cost += cost
            union(group, sub_v, x, y)
        else:
            main_count=-1

    return mst, total_cost
    
def helper_find_cycle(array, start_pos, end_pos, event):
    #do not waste first thread
    global helper_discard
    print(main_count)

    # if event.is_set():
    #     return
    #print("start_pos"+str(start_pos))
    if start_pos != 0:
        for i in range(len(array)):

            cost, A, B = array[i]
        
            x = find(group, A)
            y = find(group, B)
    
            if x == y:
                helper_discard[i+start_pos] = 1
                print(main_count, i+start_pos)

            


def output(mst, total_cost):
    for edge in mst:
        print(edge)
    print(total_cost)


if __name__ == "__main__":
    graph, E, V = read_graph()
    print(graph)
    mst, total_cost = par_MST(graph)
    output(mst, total_cost)
