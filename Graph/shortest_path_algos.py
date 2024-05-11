
'''
Dijkstra
To find the minimum distance between the source to other nodes in the weighted graph
'''
from collections import defaultdict, deque
from heapq import *
import sys
def dijkstra(adj,source):
  '''
  type adj: dict of list
  type source: int
  '''
  dis = defaultdict(int)
  heap = []
  vis = set()
  dict[source] = 0
  heappush(heap,(0,source))
  while heap:    #-----> o(V)
    curr, distance = heappop(heap)
    if curr in vis:
      continue
    vis.add(curr)
    for neighbor,weight in adj[curr]:   #----> o(E)
      if neighbor not in dis or dis[neighbor]>weight+dis[curr]:
        dis[neighbor] = weight+dis[curr]   
        heappush(heap,(dis[neighbor],neighbor)) #----> o(logV)
  '''
  Total complexity is (v + E*logV)
  it cant support negative weight edges
  if nodes are not present in dis that means they are  unreachable from source
                 1
             5/    \10
            2  ---  3
        2 /     -8
         4 
          s=1 
        the shortest path of 4 should be 4 but it will be 7 hence Dijkstra does not work with negative edges.
  '''

'''
*Bellman-ford algorithm* 
1. The algorithm overcomes the problem of dealing with negative edges
2. It helps to detect -ve cycle is the graph.
Algorithm stats that to get the shortest path from src to all the nodes of the graph we need to relax the all edges n-1 
where n is number of vertices, why n-1 ?? eg 1----->2------>3------->4------>5 since we wont be knowing the sequence of the edges 
                                                1       1       1       1
it will take n-1 time to relax all the edges optimally  [0, inf, inf, inf, inf] in first itration if edges are starting from right then only 1st vertex will
get 1 value in first iteration then 2nd in second iteration so on.
'''

def bellmanFord(edges,N,src):
  '''
  type edges: list[list]
  type N: int
  type src: int
  rtype: list
  '''
  dis = [sys.maxsize for i in range(N)]
  dis[src] = 0
  for _ in range(N-1):
    for u,v,w in edges:
      if dis[u] + w < dis[v]:
        dis[v]=dis[u]+w
  ''' Now to detect the negative cycle we need to iterate one more time and it value is stil getting decreased then thats means there is a loop '''
  for u,v,w in edges:
    if dis[u]+w < dis[v]:
      return []
  return dis   

  ''' time complexity is v*E '''

'''
Floyd warshall
1. Wont work with the negative cycle graph
2. Will work with positive and negative edges
3. algorithm is capable of find shorted path of all pairs but Djk and bellman wont work for all
4. Uses dp approach, intution is simple, two vertices can be connected through multiple intermediat edges so find optimal path from i to k then k to j
'''

def floydWarshall(graph,N):
  '''
  type graph: list[list]
  type N: int
  rtype: list[list]
  '''
  dist =  [[sys.maxsize for j in range(N)] for i in range(N)]

  for i in range(N):
    for j in range(N):
      if i == j:
        dist[i][j]=0
      elif graph[i][j] != 0:
        dist[i][j] = graph[i][j]

  for k in range(N):
     for i in range(N):
       for j in range(N):
         if dist[i][j] > dist[i][k] + dist[k][j] and dist[i][k]!=sys.sizemax and dist[k][j]!=sys.sizemax:
           dist[i][j] = dist[i][k] + dist[k][j]
  return dist
''' Floyd Warshall is works good in dense edge graph because it will be running atmost v*v*v '''



