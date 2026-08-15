class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        dp=[[0 for j in range(len(word2)+1)]for i in range (len(word1)+1) ]
       
        for i in range (len(word1)+1):
            dp[i][len(word2)]=len(word1)-i
        for i in range (len(word2)+1):
            dp[len(word1)][i]=len(word2)-i
        
  
        
        for i in range(len(word1)-1,-1,-1):

            for j in range(len(word2)-1,-1,-1):
                
                if(word1[i]!=word2[j]):
                    dp[i][j]=min(min(dp[i][j+1],dp[i+1][j]),dp[i+1][j+1])+1
                else:
                    dp[i][j]=dp[i+1][j+1]
               
        return dp[0][0]