class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(combi):
            if(len(combi)==len(nums)):
                ans.append(combi)
                return 
            for i in nums:
                if(i not in combi):
                    dfs(combi+[i])
            return 
        dfs([])
        return ans