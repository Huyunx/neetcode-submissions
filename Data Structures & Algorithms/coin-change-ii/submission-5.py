class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[]
        dp.append(1)
        
        for am in range(1,amount+1):
            if(am-coins[0]<0):
                dp.append(0)
            else:
                dp.append(dp[am-coins[0]])
        
        for i in range(1,len(coins)):
            c=coins[i]
            for am in range(1,amount+1):
                a=0
                b=dp[am]
                if(am-c>=0):
                    a=dp[am-c]
                dp[am]=a+b
        return dp[amount]