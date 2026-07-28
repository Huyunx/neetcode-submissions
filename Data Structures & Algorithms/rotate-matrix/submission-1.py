class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def reverse(mat):
            for i in range(int(len(mat)/2)):       
                mat[i],mat[len(mat)-i-1]=mat[len(mat)-i-1],mat[i]
        def transpose(mat):#reflection along diagonal is essentially changing i,j axes
            for i in range(len(mat)):
                for j in range(i,len(mat)):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

        reverse(matrix)
        transpose(matrix)