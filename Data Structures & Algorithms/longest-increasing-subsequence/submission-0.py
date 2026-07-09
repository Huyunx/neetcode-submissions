class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[]
        dp.append(1)
        ans=1
        for i in range(1,len(nums)):
            dp.append(0)
            bestdpindex=i
            for j in range(0,i):
                if(nums[j]<nums[i]):
                    if(dp[j]>dp[bestdpindex]):
                        bestdpindex=j
            dp[i]=dp[bestdpindex]+1
            ans=max(dp[i],ans)
        return ans
