#pff had huge problem with implementations

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        par=[]
        def ispal(i,j):
            a=i
            b=j
            while(a<b):
                if(s[a]!=s[b]):
                    return False
                a+=1
                b-=1
            return True
        def dfs(i):
            if(i==len(s)):
                ans.append(par.copy())
                return 
            for j in range(i,len(s)):
                if(ispal(i,j)):
                    par.append(s[i:j+1])
                    dfs(j+1)
                    par.pop()
            return 
        dfs(0)
        return ans