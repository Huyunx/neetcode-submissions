class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(a,b):
            return a==b or b=='.'
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[len(s)][len(p)]=True
        for i in range(len(s),-1,-1):
            for j in range(len(p)-1,-1,-1):
                if(i+1<=len(s)):
                    m=match(s[i],p[j])
                if(j!=len(p)-1 and p[j+1]=='*'):
                    dp[i][j]=dp[i][j+2] or (i+1<=len(s) and m and dp[i+1][j+2]) or (i+1<=len(s) and m and dp[i+1][j])
                else:
                    if(i+1<=len(s)):
                        dp[i][j]=match(s[i],p[j]) and dp[i+1][j+1]
        return dp[0][0]
           
             

