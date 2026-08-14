class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        suma=0
        for i in range(len(nums)):
            suma+=abs(nums[i])
            nums[i]=abs(nums[i]*2)
        target = target+suma
        c=nums[0]
        dp={}
        def numways(targ,frontindex):
            
          
            
            if(targ<0):
                return 0
            if(frontindex>=len(nums)):
                if(targ==0):
                    return 1
                else:
                    return 0
            if (targ,frontindex) in dp:
                return dp[(targ,frontindex)]
            ret= numways(targ-nums[frontindex],frontindex+1)+numways(targ,frontindex+1)
            dp[(targ,frontindex)]=ret
            return ret
        return numways(target,0)


