
'''
Dijkstra
To find the minimum distance between the source to other nodes in the weighted graph
'''
from collections import defaultdict, deque
from heapq import *
def dijkstra(adj,source):
  '''
  type adj: dict of list
  type source: int
  '''
  dist = difaultdict(int)
  heap = []
  vis = set()
  dict[source] = 0
  heappush(heap,(0,source))
  while heap:    -----> o(V)
    curr, distance = heappop(heap)
    if curr in vis:
      continue
    vis.add(curr)
    for neighbor,weight in adj[curr]:   ----> o(E)
      if neighbor not in dis or dis[neighbor]>weight+dis[curr]:
        dis[neighbor] = weight+dis[curr]   
        heappush(heap,(dis[neighbor],neighbor)) ----> o(logV)
  '''
  Total complexity is (v + E*logV)
  it cant support negative weight edges
  if nodes are not present in dis that means they are  unreachable from source
  '''
