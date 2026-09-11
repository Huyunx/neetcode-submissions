class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans=0
        stack=[]
        
        for i,h in enumerate(heights):
            extensionindex=i
            while stack and h<stack[-1][1]:
                startindex=stack[-1][0]
                area=(i-startindex)*stack[-1][1]
                ans=max(ans,area)
                extensionindex=startindex
                stack.pop()
            
            stack.append((extensionindex,h))
        while stack:
            i,h=stack[-1]
            area=(len(heights)-i)*h
            ans=max(ans,area)
            stack.pop()
        return ans