class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0 for i in range(len(temperatures))]
        stack=[]
        stack.append(0)
        for i in range(1,len(temperatures)):
            t=temperatures[i]

            while(stack and t>temperatures[stack[-1]]):
                j=stack[-1]
                ans[j]=i-j
                stack.pop()
            stack.append(i)
        return ans
