#you are worried about having subset difference of larger thatn 2 but 
#s1+s2+t1+s3+t2.... we can essentially just treat s1+s2 as one s1
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}
        if(len(s1)+len(s2)!=len(s3)):
            return False
        def isinterleaving(i,j):
            
            a=False
            b=False
            if(i==len(s1) and j==len(s2)):
                return True
            if((i,j) in dp):
                return dp[(i,j)]
            if(i<len(s1) and s1[i]==s3[i+j]):    
                a=isinterleaving(i+1,j)
            if(j<len(s2) and s2[j]==s3[i+j]):
                b=isinterleaving(i,j+1)
            dp[(i,j)] = a or b
            return dp[(i,j)]
        return isinterleaving(0,0)
        