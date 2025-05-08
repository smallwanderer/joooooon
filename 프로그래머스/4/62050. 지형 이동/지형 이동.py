direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def valid_c(y, x, length):
  return 0 <= y < length and 0 <= x < length

def find(node, parent):
  root = node
  while parent[root] != root:
    root = parent[root]

  while parent[node] != root:
    next_node = parent[node]
    parent[node] = root
    node = next_node

  return root

def union(node1, node2, parent):
  root1 = find(node1, parent)
  root2 = find(node2, parent)

  if root1 == root2:
    return False
  parent[root2] = root1
  return True

def make_edge_data(land):
  edge = []
  length = len(land)
  for y in range(length):
    for x in range(length):
      for dy, dx in direction:
        ny, nx = y+dy, x+dx
        if valid_c(ny, nx, length):
          edge.append([ny*length+nx, y*length+x, abs(land[ny][nx] - land[y][x])])
  edge.sort(key=lambda x: x[2])
  return edge

# Kruskal
def solution(land, height):
  import sys
  sys.setrecursionlimit(100000)
  edges = make_edge_data(land)
  length = len(land)
  parent = list(range(length * length))
  answer = 0

  for node1, node2, weight in edges:
    if union(node1, node2, parent):
      if weight > height:
        answer += weight

  return(answer)