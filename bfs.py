#Breath  First Search into a Graph
v = 8  # number of vertices
steps = [float('+inf')]*v #Array of steps for exploring nodes
adLi = [[1,2,3],[],[5],[4,5,7],[6],[6],[],[6]]  #Adjacency list of a directed graph

def BFS(start_v):
    cola = []
    cs=0
    cola.append(start_v)
    steps[start_v] = 0
    
    while(len(cola)>0):  #not cola.empty
        p = cola.pop(0)
        #print(p)
        #input()
        cs = steps[p]+1
        for i in (adLi[p]):
            if steps[i] == float('+inf'):
                cola.append(i) #if steps [i] == -1
                steps[i] = min(steps[i], cs)
          
    #Steps return the minimum steps to reach each node
    for i in range(len(steps)):
        print(i, steps[i])

BFS(0)
