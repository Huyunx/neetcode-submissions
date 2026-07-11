class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for i in prerequisites:
            adj[i[0]].append(i[1])
        visited={}
        visitedoverall={}
        def can(node):
            if(node in visited and visited[node]):
                return False
            visited[node]=True
            visitedoverall[node]=True
            ans=True
            for i in adj[node]:
                if not can(i):
                    return False
            visited [node]=False
            return True
        for i in range(numCourses):
            if i not in visitedoverall:
                if(not can(i)):
                    return False
        return True
        