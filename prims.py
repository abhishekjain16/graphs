from heap import Heap

def prims(graph):
  vertices = graph.keys()
  Q = Heap(len(vertices))
  parent = {}
  src = vertices[0]
  output = []

  for vertex in vertices:
    if vertex == src:
      Q.insert((vertex, 0))
    else:
      Q.insert((vertex,float('inf')))
    parent[vertex] = None

  while not Q.isEmpty():
    u, weight = Q.pop()
    if parent[u] != None:
      output.append([u, parent[u]])
    edges = graph[u]
    for edge in edges:
      v, wt_v = edge
      if wt_v < Q.minHeap[Q.findIndex(v)][1]:
        parent[v] = u
        Q.decreaseKey(v, wt_v)
  printPath(output)


def printPath(parent):
  print parent

def run(filename):
  graph = generate_graph(filename)
  prims(graph)

def generate_graph(filename):
  f = open(filename, "r")
  lines = f.readlines()
  lines = [x.strip() for x in lines]
  lines.pop(0)
  vertices = []
  graph = {}
  for line in lines:
    line = line.split(" ")
    point1 = line[0]
    point2 = line[1]
    weight = int(line[2])

    if point1 not in graph:
      graph[point1] = [(point2, weight)]
    else:
      graph[point1].append([point2, weight])

    if point2 not in graph:
      graph[point2] = [(point1, weight)]
    else:
      graph[point2].append([point1, weight])

  return graph


run("Graph.txt")
