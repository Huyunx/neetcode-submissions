class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={
        }
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            n=s[i]
            a=''
            for j in range(i, len(s)):
                a=a+s[j]
                if((a in wordDict) and dp[j+1] ):
                    dp[i]=True
                    break
                dp[i]=False

        return dp[0]