from read_graph import read_graph, V, E, THREADS
from par import par_MST
from seq import seq_MST
import time


if __name__ == "__main__":
    graph,E,V = read_graph()
    
    print( """
        1. Sequential.
        2. Parallel
    """
    )
    seq_time = 0
    par_time = 0
    n=10.0

    name = 'sequential'
    start_s = time.perf_counter()

    mst, total_cost = seq_MST(graph)

    end_s = time.perf_counter() 
    seq_time +=end_s - start_s
    # print(mst)
    print(f"The execution time of {name} algo (Vertices = {V}, Edges = {E}) is: \n {(end_s - start_s):0.6f} seconds\
            \n Total cost of the tree is: \n {total_cost}")

    name = 'parallel'
    
    start_p = time.perf_counter()
    mst, total_cost = par_MST(graph)
    # print(mst)
    end_p = time.perf_counter() 
    par_time += end_p - start_p
    print(f"The execution time of  {name} algo (Vertices = {V}, Edges = {E}) is: \n {(end_p - start_p):0.6f} seconds.\
            \n Total cost of the tree is: \n {total_cost}")

    with open("res_file.txt", 'a') as f:
        line = f"Threads: {THREADS}\t Average time sequential: {(seq_time/n):0.6f} \t Average time parallel: {(par_time/n):0.6f} \t Vertices: {V}\t Edges:{E}"
        f.write(line)
        f.write('\n')


