# ---------------------------------- Algorithm 1 --------------------------------- #
# ------- Make this section with comments to let the second algorithm work ------- #

import matplotlib.pyplot as plt
from networkx import *

vertices = []
times = 0

def isGraphConnected(edge):
    """An algorithm to know if the graph is connected or no"""
    counter = 0

    pointers = []

    isGraphConnected = True

    for i in range(len(edge)):
        if edge[0][0] == edge[i][0] or edge[0][0] == edge[i][1]:
            #print("{} and {} are connected".format(edge[0] , edge[i]))
            if edge[i][0] not in pointers:
                pointers.append(edge[i][0])
            
            if edge[i][1] not in pointers:
                pointers.append(edge[i][1])
            #print(pointers)

        elif edge[0][1] == edge[i][1] or edge[0][1] == edge[i][0]:
            #print("{} and {} are connected".format(edge[0] , edge[i]))
            if edge[i][0] not in pointers:
                pointers.append(edge[i][0])
            if edge[i][1] not in pointers:
                pointers.append(edge[i][1])
        else:
            #print("{} and {} are nooot connected".format(edge[0] , edge[i]))
            counter+=1

    
    def rePeat():
        global times
        for k in range(len(edge)):
            for p in range(len(pointers)):
                if (pointers[p] == edge[k][0]):
                    if edge[k][1] not in pointers:
                        pointers.append(edge[k][1])
                    if times<3:
                        times = times+1
                        rePeat()
                if pointers[p] == edge[k][1] :
                    if edge[k][0] not in pointers:
                        pointers.append(edge[k][0])
                    if times<3:
                        times = times+1
                        rePeat()
    rePeat()

    unConnected = 0
    for m in range(len(edge)):
        unConnected = 0
        for n in range(len(pointers)):
            if (edge[m][0] == pointers[n]) or (edge[m][1] == pointers[n]):
                continue
            else:
                unConnected+=1
        if unConnected == len(pointers):    
            isGraphConnected = False
            break
        print(pointers)


    if isGraphConnected:
        print("Graph is Connected")
    else:
        print("Graph is Not Connected")

edges = []

x = None
counter = 1

while True:
    x = input("enter vertex 1 of edge("+str(counter)+") :-")
    y = input("enter vertex 2 of edge("+str(counter)+") :-")

    vertices.append(x)
    vertices.append(y)
    
    counter+=1
    try:
        x = int(x)
        y = int(y)
    except:
        break
    
    edges.append((x,y))
    print(edges)

isGraphConnected(edges)


g = Graph()
g.add_edges_from(edges)
draw(g)
plt.show()


# ------------------- Algorithm 2 ------------------- #
# ------- remove the comments to make it work ------- #


#import matplotlib.pyplot as plt
#import matplotlib
#from networkx import draw, Graph
#import networkx
#from networkx.algorithms.components.connected import is_connected

#edges = []

#allnums = []

#NodesCheck = []
#toReplace = 0
#ifThere = False

#isConnected = True

#x = None

#while True:
    #x = eval(input("enter vertex 1 of edge:-"))   
    #if x == "x":
        #break
    #for i in allnums:
        #if i == x:
            #ifThere = True
            #break
    #if ifThere == False:
        #allnums.append(x)
    #else:
        #ifThere = False

    #y = eval(input("enter vertex 2 of edge:-"))
    #for i in allnums:
        #if i == y:
            #ifThere = True
            #break
    #if ifThere == False:
        #allnums.append(y)
    #else:
        #ifThere = False
        
    #edges.append([x,y])
    #print(edges)

#g = Graph()
#g.add_edges_from(edges)
#networkx.draw(g)
#plt.show()

#for i in range(len(edges)):
    #for j in range(len(edges)):
        #if edges[0][0] == edges[j][0] or edges[0][0] == edges[j][1]:
            #if edges[0][0] == edges[j][0]:
                #NodesCheck.append(edges[j][1])
                #toReplace = edges[0][0]
                #edges[j][1] = edges[0][0]
            #else:
                #NodesCheck.append(edges[j][0])
                #toReplace = edges[0][0]
                #edges[j][0] = edges[0][0]
    #for m in NodesCheck:
        #for k in range(len(edges)):
            #if m == edges[k][1]:
                #edges[k][1] = toReplace
            #elif m == edges[k][0]:
                #edges[k][0] = toReplace
    #NodesCheck = []
    
#for msm in range(len(edges)):
    #if edges[0][0] != edges[msm][0] or edges[0][0] != edges[msm][1]:
        #isConnected = False

#print(edges)
#print(NodesCheck)

#if isConnected:
    #print("The graph is connected")
#else:
    #print("The graph is not connected")