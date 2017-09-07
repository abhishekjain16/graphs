from heap import Heap

def makeTree(ver,inEdges):
    count = 1
    Q = Heap(len(inEdges))
    for edge in inEdges:
        edge = edge.split("\t")
        src = int(edge[0])
        dest = int(edge[1])
        weight = int(edge[2])
        Q.insert((((src, dest), weight)))
    while not Q.isEmpty():
        print("New loop")
        print(Q.minHeap)
        edge,weight = Q.pop()
        print(Q.minHeap)
        # print str(count) + ") " + str(edge[0]) + " " + str(edge[1]) + " " + str(weight)
        count = count + 1

f = open("Graph (1).txt", "r")
lines = f.readlines()
ver = lines.pop(0)[0]
lines = [x.strip() for x in lines]

makeTree(ver,lines)
