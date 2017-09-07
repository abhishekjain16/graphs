from heap import Heap

def run(filename, src, dest):
  graph = generate_graph(filename)
  print graph
  dijkstra(graph, src, dest)

def generate_graph(filename):
  f = open(filename, "r")
  lines = f.readlines()
  lines = [x.strip() for x in lines]
  lines.pop(0)
  graph = {}
  for line in lines:
    line = line.split("\t")
    source = line[0]
    destination = line[1]
    weight = int(line[2])

    if source not in graph:
      graph[source] = [(destination, weight)]
    else:
      graph[source].append([destination, weight])
    if destination not in graph:
      graph[destination] = []
  return graph


def dijkstra(graph, src, dest):
  vertices = graph.keys()
  Q = Heap(len(vertices))
  parent = {}

  for vertex in vertices:
    if vertex == src:
      Q.insert((vertex, 0))
    else:
      Q.insert((vertex,float('inf')))

  while not Q.isEmpty():
    u, wt_u = Q.pop()
    if u == dest:
      printPath(parent, src, dest)
      break
    else:
      lst = graph[u]
      for tup_v in lst:
        v, wt_v = tup_v
        if wt_u + wt_v < Q.minHeap[Q.findIndex(v)][1]:
          new_wt = wt_u + wt_v
          parent[v] = u
          Q.decreaseKey(v, new_wt)

def printPath(parent, src, dest):
  if src == dest:
    print src
    return
  else:
    printPath(parent, src, parent[dest])
    print dest

run("Graph.txt", "4", "0")
