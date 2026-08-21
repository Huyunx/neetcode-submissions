class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        l=0
        r=n*m-1
        while True:
            mid=(l+r)//2
            i=mid//m
            j=mid%m
            #n*i+j
            if(l>r):
                return False
            if(matrix[i][j]==target):
                return True
            if(matrix[i][j]<target):
                l=mid+1
            if(matrix[i][j]>target):
                r=mid-1
            