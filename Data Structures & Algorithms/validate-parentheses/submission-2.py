class Solution:
    def isValid(self, s: str) -> bool:
        openb={"[","(","{"}
        closeb={"]",")","}"}

        stack=[]
        for n in s:
            if(n in openb):
                stack.append(n)
            else:
                if not stack:
                    return False
                if((stack[-1]=="[" and n=="]") or (stack[-1]=="(" and n==")") or (stack[-1]=="{" and n=="}") ):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        