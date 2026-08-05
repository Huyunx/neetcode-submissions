class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        def dfs(index,combi):
            if(index>=len(nums)):
                ans.append(combi)
                return
            dfs(index+1,combi+[nums[index]])
            #exclude
            i=0
            while index+1+i<len(nums) and nums[index+i]==nums[i+index+1]:
                i+=1
            
            dfs(index+i+1,combi)
            return
        dfs(0,[])
        return ans
        

