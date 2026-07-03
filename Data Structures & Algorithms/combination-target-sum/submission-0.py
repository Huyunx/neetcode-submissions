class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(target,nums,curr):
            if(not nums):
                return
            if(target==0):
                ans.append(curr[:])
                return
            if(target<0):
                return
            i=nums[0]
            num=nums[:]
            num.remove(i)
            dfs(target,num,curr)
            curr.append(i)
            dfs(target-i,nums,curr)
            curr.pop()
                
            return 
        dfs(target,nums,[])
        return ans


