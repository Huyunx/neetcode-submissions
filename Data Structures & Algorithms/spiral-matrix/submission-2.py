#should have done recursion for cleanlyness 
#fuck it
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        l=(min(len(matrix),len(matrix[0]))+1)//2

        #r=int(l/2)+l%2 this was wrong tmd 自己挖的坑不记得了， 带着个“没事到时候不work 我再改” 的想法，结果完全忘了 
        visited={}
        for i in range(l):
            leftend=i
            rightend=len(matrix[0])-i-1
            downend=len(matrix)-i-1
            for j in range(leftend, rightend+1):
                ans.append(matrix[i][j])
            for j in range(i+1,downend+1):
   
                ans.append(matrix[j][rightend])
            if downend > i:  
                for j in range(rightend-1,i-1,-1):
                          
                    ans.append(matrix[downend][j])
            if rightend > i:  
                for j in range(downend-1,i,-1):
                    
                    ans.append(matrix[j][i])

        return ans