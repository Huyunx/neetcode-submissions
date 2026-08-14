class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        def lpsf(i,j):#longest path starting from 
            ret=1
            if((i,j) in dp):
                return dp[(i,j)]
            if(i+1<len(matrix) and matrix[i+1][j]>matrix[i][j]):
                ret=lpsf(i+1,j)+1
            if(i-1>=0 and matrix[i-1][j]>matrix[i][j]):
                ret=max(ret,lpsf(i-1,j)+1)
            if(j-1>=0 and matrix[i][j-1]>matrix[i][j]):
                ret=max(lpsf(i,j-1)+1,ret)
            if(j+1<len(matrix[0]) and matrix[i][j+1]>matrix[i][j]):
                ret=max(lpsf(i,j+1)+1,ret)
            dp[(i,j)]=ret
            return ret
        ans=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans=max(ans,lpsf(i,j))
        return ans