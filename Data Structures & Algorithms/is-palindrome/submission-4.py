class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=0
        y=len(s)-1
        while True:
            if(x>=y):
                break
            if (not s[x].isalnum()):
                x+=1
                continue
            if( not s[y].isalnum()):
                y-=1
                continue
            
            if(s[x].lower()!=s[y].lower()):
                return False
            x+=1
            y-=1
        return True
