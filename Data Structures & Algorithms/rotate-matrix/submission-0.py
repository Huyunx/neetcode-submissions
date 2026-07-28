import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=len(matrix)
        r=math.floor(l/2)
        for i in range(r):
            for j in range(i,l-i-1):
                a,b=i,j
                ini=matrix[a][b]
                matrix[a][b]=matrix[l-1-b][a]
                a,b=l-1-b,a
                matrix[a][b]=matrix[l-1-b][a]
                a,b=l-1-b,a
                matrix[a][b]=matrix[l-1-b][a]
                a,b=l-1-b,a
                matrix[a][b]=ini


        