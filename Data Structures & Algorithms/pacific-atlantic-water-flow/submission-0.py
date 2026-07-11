class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        canreachP={}
        canreachA={}
        rows=len(heights)
        cols=len(heights[0])
        def dfs(i,j,prev,canreach):
            if((i,j) in canreach):
                return
            if(i<0 or j<0 or i>=rows or j>=cols):
                return
            if(heights[i][j]<prev):
                return 
            else:
                canreach[(i,j)]=True
                dfs(i+1,j,heights[i][j],canreach)
                dfs(i,j+1,heights[i][j],canreach)
                dfs(i,j-1,heights[i][j],canreach)
                dfs(i-1,j,heights[i][j],canreach)

                return

        for i in range (cols):
            dfs(0,i,-1,canreachP)
            dfs(len(heights)-1,i,-1,canreachA)
        for j in range(rows):
            dfs(j,0,-1,canreachP)
            dfs(j,cols-1,-1,canreachA)
        ans=[]
        for i in range(rows):
            for j in range(cols):
                if ((i,j) in canreachA) and ((i,j) in canreachP) and (canreachP[(i,j)] and canreachA[(i,j)]):
                    ans.append([i,j])
        return ans


        