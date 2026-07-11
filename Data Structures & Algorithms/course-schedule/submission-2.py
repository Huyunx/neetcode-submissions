class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for i in prerequisites:
            adj[i[0]].append(i[1])
        visited={}
        visitedoverall={}
        def can(node):
            if(node in visitedoverall):
                return visitedoverall[node]
            if(node in visited and visited[node]):
                return False
            visited[node]=True
            
            ans=True
            for i in adj[node]:
                if not can(i):
                    visitedoverall[node]=False
                    return False
            visited [node]=False
            visitedoverall[node]=True
            return True
        for i in range(numCourses):
            if i not in visitedoverall:
                if(not can(i)):
                    return False
        return True
        