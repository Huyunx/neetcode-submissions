class Solution:
    def isHappy(self, n: int) -> bool:
    
        visited=set()
        visited.add(n)
        while n!=1:
            s=0
            while n!=0:
                a=n%10
                n=n//10
                s+=a**2
            
            n=s
            if(n in visited):
                return False
            visited.add(n)
        return True