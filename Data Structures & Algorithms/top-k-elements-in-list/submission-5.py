class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={

        }
        n=len(nums)
        numwithf=[]
        for i in range(n+1):
            numwithf.append([])

        for i in nums:
            if(i not in f):
                f[i]=1
            else:
                f[i]+=1
            
        for i in f:
            numwithf[f[i]-1].append(i)
        count=0
        ans=[]
        for i in range(n-1,-1,-1):
            if(len(numwithf[i]) != 0):
                ans.extend(numwithf[i])
                count+=len(numwithf[i])
            if(count == k):
                break
        return ans

            
