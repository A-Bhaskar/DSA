'''
Q. Given a grid of m boys and n girls, where grid[i][j] = 1 
represents that ith boy can invite girl jth girl to party. 
Each boy can invite only one girl and each girl can accept 
only one invitation. Find the most invitations that can be accepted.
{{1,1,1},
{1,0,1},
{0,0,1}}
'''
'''
This is a bipartite graph and this question can be done using ford fulkerson but that will take (m+n+2)*(m+n+2) memory
intution:  Check for all boys if he can invite a girl and girl is available then return True
if not then check for the possibility of the boy who has already matched with the girl can invite other girl
'''

def dfs(graph,matchList,vis,u):
    if vis[u]:
        return False
    vis[u] = True

    for idx,val in enumerate(graph[u]):
        if val > 0 and ( matchList[idx] < 0 or dfs(graph,matchList,vis,matchList[idx])):
            matchList[idx] = u
            return True
    return False

def GetMatches(graph):
    numOfBoys = len(graph)
    numOfGirls = len(graph[0])
    matchList = [-1]*numOfGirls
    totalMatches = 0
    for u in range(numOfBoys):
       vis = [False]*numOfBoys
       if dfs(graph,matchList,vis,u):
           totalMatches+=1
    return totalMatches


if __name__ == "__main__":
    matchGraph = [[1,0,1,0],
              [1,0,0,0],
              [0,0,1,0],
              [1,1,1,0]]
    print(GetMatches(matchGraph))
    pass
