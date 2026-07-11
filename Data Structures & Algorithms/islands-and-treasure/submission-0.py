from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque([])
        visited=[[False for i in range (len(grid[0]))] for i in range (len(grid))]
        INF = 2147483647
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if(grid[i][j]==0):
                    q.append((i,j))
                   
        level=0
        while q:
            l=len(q)
            for i in range(l):
                a=q[0][0]
                b=q[0][1]
                if(a<0 or b<0 or a>=len(grid) or b>=len(grid[0]) or visited[a][b] or grid[a][b]==-1):
                    q.popleft()
                    continue
                grid[a][b]=level
                visited[a][b]=True
                q.popleft()
                q.append((a+1,b))
                q.append((a-1,b))
                q.append((a,b+1))
                q.append((a,b-1))
            level+=1