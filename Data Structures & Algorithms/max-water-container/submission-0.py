class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x=0
        y=len(heights)-1
        m=0
        while x<y:
            area =min(heights[y],heights[x])*(y-x)
            if(area>m):
                m=area
            left=heights[x]
            right=heights[y]
            if(left<right):
                x+=1
            else:
                y-=1
        return m