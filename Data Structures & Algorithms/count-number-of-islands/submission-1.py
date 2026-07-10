class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if(not grid):
            return 0
        ans=0
        def merge(a,b):
            nonlocal ans
            if(a==len(grid) or a<0 or b<0 or b==len(grid[0]) or grid[a][b]=='0'):
                return
            if(grid[a][b]=='1'):
                ans-=1
                grid[a][b]='0'
            merge(a+1,b)
            merge(a,b+1)
            merge(a-1,b)
            merge(a,b-1)
            return
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    ans+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    ans+=1
                    merge(i,j)
        return ans