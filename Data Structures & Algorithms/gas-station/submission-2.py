class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff=[]
        c=0
        g=0
        for i in range(len(gas)):
            c+=cost[i]
            g+=gas[i]
            
        sum=0
        ans=0
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        if(c>g):
            return -1
        for i,n in enumerate(diff):
            sum+=n
            if(sum<0):
                sum=0
                ans=i+1
        return ans
