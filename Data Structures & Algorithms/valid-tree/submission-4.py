class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj={}
        visited={}
        for i in edges:
            adj[i[0]]=adj.get(i[0],[])
            adj[i[0]].append(i[1])
            adj[i[1]]=adj.get(i[1],[])
            adj[i[1]].append(i[0])
        if not adj and n==1:
            return True
        def dfs(node,prev):#->bool ,dfs tells us if contain cycle
            if(node in visited):
                return False
            visited[node]=True
            for i in adj[node]:
                if(i==prev):
                    continue
                if not dfs(i,node):
                    return False
            return True
        ans=dfs(0,-1)
        if len(visited) != n:
            return False
        return ans