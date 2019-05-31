
v = 8
v_Dist = [(8000000,-1)]*v
visited = [False]*v
AdjMatr = [[0,21,12,3,0,2],[21,0,0,0,0,0],[12,0,0,4,0,0],[3,0,4,0,1,0],[0,0,0,1,0,5],[2,0,0,0,5,0]]


def printPath(start_v, end_v):
    tam = int(v_Dist[end_v][0])
    prev_node = v_Dist[end_v][1]
    print(end_v)
    print(prev_node)
    while(prev_node!=start_v):
    #for i in range(tam):
        end_v = v_Dist[prev_node][1]
        prev_node = v_Dist[end_v][1]
        print(prev_node)
    #print(start_v)

def Dijkstra(start_v):
    cola = []
    cola.append(start_v)
    minDis = 0
    v_Dist[0] = minDis, start_v
    #v_Dist[0][1] = start_v
    
    
    while(len(cola) >0):
        p = cola.pop(0)
        visited[p]= True
        minDis = v_Dist[p][0]
        
        for i in range(0, len (AdjMatr[p])):
            if (AdjMatr[p][i] != 0 and v_Dist[i][0]> minDis+AdjMatr[p][i]):
                v_Dist[i] = minDis+AdjMatr[p][i], p
                cola.append(i)
                #v_Dist[i][1] = p
                
             
Dijkstra(0)
printPath(0,4)

#v_Dist[0][1] = 5
print(v_Dist)
