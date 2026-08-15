class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[]
        for i in range(0,len(t)):
            dp.append(0)
        dp.append(1)
        
        for j in range(len(s)-1,-1,-1):
            origiplusone=1
            for i in range(len(t)-1,-1,-1):
                a=dp[i]
                if(s[j]==t[i]):
                    dp[i]=dp[i]+origiplusone
                    
                origiplusone=a
                
        return dp[0]