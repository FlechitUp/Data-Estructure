#Depth First Search into a Graph
v = 8  # number of vertices
vis = [0]*v #Array of explored nodes
adLi = [[0,1,3,7],[0,0,2,5,6],[0,1,4,5],[0,0],[0,2,5,6],[0,1,4],[0,4,1,7],[0,0,6]]  #Adjacency list

# Adjacent list has this structure:
#[ [0], [0], ... ,[0] ]  #This row keeps the count of explored nodes of each node
#   1    0         0     # node 1 is adjacent to node 0, 0 is adjacent to node 1, ... , 0 is adjacent to the last node
#   3    2         6
#   7    5
#        6      

def DFS(start_v):
    print(start_v)
    vis[start_v] = 1
    
    pt = adLi[start_v][0]
    for i in range(pt+1, len(adLi[start_v])):
        val_i = adLi[start_v][i]
        if (vis[val_i]==0 and start_v != val_i and adLi[val_i][0]<len(adLi[val_i])): # last condition determines if is fully explored
            adLi[val_i][0]+=1
            DFS(val_i)
            
            
DFS(0)
