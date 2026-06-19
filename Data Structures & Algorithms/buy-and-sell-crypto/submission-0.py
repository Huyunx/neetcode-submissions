class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mininow=prices[0]
        defecit=0
        largestdeficit=0
        for i,n in enumerate(prices):
            deficit=n-mininow
            if(deficit > largestdeficit):
                largestdeficit=deficit
            if(n<mininow):
                mininow=n
        return largestdeficit
            