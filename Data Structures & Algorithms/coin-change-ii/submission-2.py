class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo={}
        def numways(am,lastindex):
            if(am<0):
                return 0 
            if(am==0):
                return 1
            if((am,lastindex) in memo):
                return memo[(am,lastindex)]
            out=0
            for i in range(lastindex,len(coins)):
                out+=numways(am-coins[i],i)
            memo[(am,lastindex)]=out
            return out
        return numways(amount,0)