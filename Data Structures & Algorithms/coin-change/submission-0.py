class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        dp[0]=0
        def ans(target):
            if(target<0):
                return -1
            if(target in dp):# includes when target == 0 and ans returns dp[0] i.e 1
                return dp[target]
            a=10001
            for i in coins:
                dp[target-i]=ans(target-i)
                heigh=dp[target-i]
                if(heigh != -1 and a>heigh ):
                    a=heigh
            if a==10001:
                return -1

            return a+1
        return ans(amount)