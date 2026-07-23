class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={}
        for i in prerequisites:
            adj[i[0]]=adj.get(i[0],[])
            adj[i[0]].append(i[1])
        visited={}
        foundcycle=0
        def dfs(node,visiting):
            nonlocal foundcycle
            ans=[]
            if(node in visiting):
                foundcycle = 1
                return []
            if(node in visited and visited[node]):
                return []
            visited[node]=True
            visiting.add(node)
            if(node in adj):
                for i in adj[node]:

                    ans=ans+dfs(i,visiting)
            ans.append(node)
            visiting.remove(node)
            return ans
        ans=[]
        
        for i in range(0,numCourses):
            visiting=set()
            ans=ans+dfs(i,visiting)
            if(foundcycle):
                return []
        return ans
