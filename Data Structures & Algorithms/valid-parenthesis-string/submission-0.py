class Solution:
    def checkValidString(self, s: str) -> bool:
        
        l=len(s)
        useempty=0
        if(l%2==1):
            l-=1
            useempty=1
        count={}
        count['(']=0
        count[')']=0
        for i in s:
            if(i!='*'):
                count[i]+=1
        closing=l/2-count[')']
        opening=l/2-count['(']
        num=0

        if(opening<0 or closing <0 ):
            return False
        for i in s:
            if(i=='*'):
                if(useempty):
                    useempty-=1
                    continue
                if(opening):
                    opening-=1
                    num+=1
                else:
                    closing-=1
                    num-=1
            else:
                if(i=='('):
                    num+=1
                else:
                    num-=1
            if(num<0):
                return False
        if(num==0):
            return True
        