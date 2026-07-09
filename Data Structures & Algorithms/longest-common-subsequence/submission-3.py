class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #from i to end of text1 and from j to end of text2
        dp={}
        
        def dfs(i,j):
            if(i==len(text1)):
                return 0
            if(j==len(text2)):
                return 0
            if((i,j) in dp):
                return dp[(i,j)]
            if(text1[i]==text2[j]):
                dp[(i,j)]=dfs(i+1,j+1)+1
                return dp[(i,j)]
            else:
                dp[(i,j)]=max(dfs(i+1,j),dfs(i,j+1))
                return dp[(i,j)]

        return dfs(0,0)