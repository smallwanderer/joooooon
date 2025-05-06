import sys
sys.setrecursionlimit(1000000)

nodes_count, edges_count = map(int, sys.stdin.readline().split())
parent_node = {x+1 : x+1 for x in range(nodes_count)}

def find(node):
  if parent_node[node] != node:
    parent_node[node] = find(parent_node[node])
  return parent_node[node]

def union(node1, node2):
  node1_root = find(node1)
  node2_root = find(node2)

  if node1_root != node2_root:
    parent_node[node1_root] = node2_root

for _ in range(edges_count):
  node1, node2 = map(int, sys.stdin.readline().split())
  union(node1, node2)

for i in range(1, nodes_count+1):
  find(i)

print(len(set(parent_node.values())))