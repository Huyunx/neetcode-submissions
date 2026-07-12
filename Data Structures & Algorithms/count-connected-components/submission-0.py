class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        adj=[[] for i in range(n)]
        ans=0
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        def dfs(node):
            if(node in visited):
                return
            visited.add(node)
            for i in adj[node]:
                dfs(i)
            return
        for i in range(n):
            if(i not in visited):
                ans+=1
                dfs(i)
        return ans

