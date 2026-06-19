class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr=1
        count=0
        n=pr
        for i in nums:
            if(i==0):
                count+=1
            pr*=i
            if(i!=0):
                n*=i
        ans=[]
        if(count >1):
            return [0]*len(nums)
        else:
            for i in nums:
                if(i==0):
                    ans.append(int(n))
                else:
                    ans.append(int(pr/i))
            return ans