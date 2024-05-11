'''
Minimum spanning tree is the tree formed by the edges of the graph that have properties
1. E = V-1 (edges will be vertices-1)
2. Travelling cost will be minimum
3. Acyclic
'''

class MST:
    def __init__(self,edges,n):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]
        self.mst = []
        self.edges=edges # w,u,v tuple

    def find(self,v):
        if self.parent[v] == v:
            return self.parent[v]
        else:
            result = self.find(self.parent[v])
            self.parent[v] = result
            return result
    def union(self,u,v):
        if self.rank[v] > self.rank[u]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u]+=1
   
    def Kruskals(self):
        self.edges.sort()
        e=1
        res = []
        for w,u,v in self.edges:
            pu = self.find(u)
            pv = self.find(v)
            if pv == pu:
                continue
            self.union(pu,pv)
            res.append([w,u,v])
            e+=1
            if e == len(self.rank)-1:
                break
        

