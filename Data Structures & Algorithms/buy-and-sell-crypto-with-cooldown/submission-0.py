class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        #to do memo, should skip 
        memo={}
        def profit(state, frontindex,prevsold):#1->bought one,0->no stock in potfolio|+1 buy,+0 cooldown,-1|sell| 1>=state>=0
            nonlocal ans
            if(frontindex==len(prices)):
                return 0
            if((state,frontindex,prevsold) in memo):
                return memo[(state,frontindex,prevsold)]
            if(state==1):
                sellprof=profit(state-1,frontindex+1,1)+prices[frontindex]
                coolprof=profit(state,frontindex+1,0)
                memo[(state,frontindex,prevsold)]=max(sellprof,coolprof)
                return memo[(state,frontindex,prevsold)]
            elif (state==0):
                buyprof=profit(state, frontindex+1,0)
                coolprof=buyprof
                if(prevsold!=1):
                    buyprof=profit(state+1,frontindex+1,0)-prices[frontindex]

                memo[(state,frontindex,prevsold)]= max(buyprof,coolprof)
                return memo[(state,frontindex,prevsold)]
        ans=profit(0,0,0)
        return ans
            
                            

            


