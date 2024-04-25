'''Ford Fulkerson Algo: This algo is to find the maximum data can be flow between source to destination.
'''
from collections import deque
import sys
class maxFlow:
    
    def bfs(self,graph,parent,s,d):
        n = len(graph)
        vis = [False]*n
        que = deque([])
        que.append(s)
        vis[s]=True
        parent[s]=-1
        while que:
            u = que.popleft()
            for indx,val in enumerate(graph[u]):
                if not vis[indx] and val>0:
                    parent[indx]=u
                    vis[indx]=True
                    if indx == d:
                        return True
                    que.append(indx)
        return False
    
    def FordFulkerson(self,graph,s,d):
        parent = [-1]*len(graph)
        maxFlow = 0
        while self.bfs(graph,parent,s,d):
            flow = sys.maxsize
            u=d
            while parent[u] != s:
                flow = min(flow,graph[parent[u]][u])
                u=parent[u]
            maxFlow+=flow

            u=d
            while parent[u] != s:
                graph[parent[u]][u]-=flow
                graph[u][parent[u]]+=flow
                u=parent[u]
            print(graph,parent)
        return maxFlow
                    
if __name__ == "__main__":
    graph = [
        [0,3,7,0,0,0],[0,0,0,3,4,0],[0,5,0,0,3,0],[0,0,0,0,3,2],[0,0,0,0,0,6],[0,0,0,0,0,0]
    ]
    obj = maxFlow()
    print(obj.FordFulkerson(graph,0,5))
