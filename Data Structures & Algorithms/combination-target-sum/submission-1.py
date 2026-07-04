class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(target,i,curr):
            if(i==len(nums)):
                return
            if(target==0):
                ans.append(curr[:])
                return
            if(target<0):
                return
            dfs(target,i+1,curr)
            curr.append(nums[i])
            dfs(target-nums[i],i,curr)
            curr.pop()
                
            return 
        dfs(target,0,[])
        return ans


