class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if(i!=0):
                if(nums[i-1]==nums[i]):
                    continue
            target=0-nums[i]
            x=i+1
            y=len(nums)-1
            while True:
                if(x>=y):
                    break
                suma=nums[x]+nums[y]
                if(y!=len(nums)-1):
                    if(nums[y]==nums[y+1]):
                        y-=1
                        continue
                if(suma>target):
                    y-=1
                    continue
                if(x!=i+1):
                    if(nums[x]==nums[x-1]):
                        x+=1
                        continue
                if(suma<target):
                    x+=1
                    continue
                if(suma==target):
                    ans.append([nums[i],nums[x],nums[y]])
                    x+=1
                    y-=1
                    
        return ans