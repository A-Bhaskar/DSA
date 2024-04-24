
'''
Disjoint set is the set of grouped element such that there wont be any common element among the different group eg each element will belong to only one group

Disjoint set can be implemented using find and union methods 
find can be have three ways implementation
1. Normal ---> O(n)
2. Ranking ----> O(logn)
3. Path Compression ---> O(alpha) ~ constant
'''

class disjointSet:
    def __init__(self,n,edges):
        '''
        dtype n: int
        dtype edges: list(int)
        '''
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def addEdges(self,edges):
        for u,v in edges:
            '''
             below function will perform in linear 
            '''
            self.union(u,v)

            '''
            log(n)
            '''
            self.unionWithRank(u,v)


    def find(self,node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])
    
    def findWithPathCompression(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findWithPathCompression(self.parent[node]) ## here we are updating the child node to have super parent as parent 
        return self.parent[node]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        self.parent[pu] = pv
    
    def unionWithRank(self,u,v):
        '''
        liner find then it will be log(n)
        '''
        pu = self.find(u)
        pv = self.find(v)

        '''
        if we use path compression find the time complexit will be ~ constant
        '''
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv]>self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pv]+=1
    


'''
   0-2,2-4,5-3,1-4,6-0,5-1
   with linear find
         5 
      0   \  
     /      \ 
    6         \ 
    |
    1          3
   /  \ 
   2   4

   with ranking 
        5
       /  \ 
      3    0  __ 6
         / | \ 
        2  4  1

'''
    