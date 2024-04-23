
'''
Bipertite: Basically this algorithm is to check whether graph can be divided into two disjoint sets where among the same set there should not be any
relation but each node of one set should have relation to the other set node
1. Can be use to detect cycle
'''
def dfs(graph,colorList,color,v):
  '''
  type graph: defaultdict(list)
  type colorList: list
  type color: int
  type v: int
  rtype: bool
  '''
  ans = True
  if colorList[v] == -1:
    colorList[v] = color
    for u in graph[v]:
      ans&=dfs(graph,colorList,1-color,u)
    return ans
  else:
    return colorList[v] == color


    
def isBipartite(graph):
  '''
  type graph: defaultdict(list)
  rtype: bool
  '''
  n=len(graph) ## Assuming that graph key will have all the vertices
  colorList = [-1 for i in range(n)]
  for i in range(n):
    if colorList[i]==-1:
      if not dfs(graph,colorList,0,i):
        return False
  return True


'''
Detect Cycle in Undirected Graph
manage vis set as well parent variable
if adjecent element is visited and that element is node parent then cycle is detected
'''


'''
Detect Cycle in directed Graph
Unlike directed graph if you have reached to node which is already visited it does not guarantee that the nodes is creating cycle
It will only happen if there is a any edge coming to ancestors. 
                1
              /   /|\
            \|/     \
            2         4 <------ 5        cycle
              \      /|\
              \|/   /
                  3
                  
                1
              /   \
            \|/     \|/
            2         4 <------ 5        no cycle
              \      /|\
              \|/   /
                  3
'''
def checkCycle(adj,vis,recStack,node):
  '''
  type adj: list(list)
  type vis: list(boo)
  type recStack: list(bool)
  type node: int
  rtype: bool
  '''
  vis[node] = True
  recStack[node] = True
  for v in adj[node]:
    if not vis[node]:
      if checkCycle(adj,vis,recStack,v):
        return true
    else recStack[v] is True:
      return True
  recStac[node] = False 
  return False
  


