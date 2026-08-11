class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
  
        def dfs(skobi,zbor,num):
            if(zbor<0):
                return 
            opened=(zbor+num)//2
            if(opened>n or opened-zbor>n):
                return
            if(num==2*n and zbor==0):
                ans.append(skobi)
            dfs(skobi+'(', zbor+1,num+1)
            dfs(skobi+')',zbor-1,num+1)
            return 
        dfs('',0,0)
        return ans