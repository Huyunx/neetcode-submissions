class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return True
        end_reachablefrom=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(end_reachablefrom-i<=nums[i]):
                end_reachablefrom=i
        if(end_reachablefrom==0):
            return True
        else:
            return False