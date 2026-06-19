class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets=set(nums)
        m=0
        for i in numsets:
            pre=i-1
            if pre not in numsets:
                j=i+1
                while True:
                    if j in numsets:
                        j+=1
                    else:
                        if((j-i))>m:
                            m=j-i
                        break
            else:
                continue
        return m