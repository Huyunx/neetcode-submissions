class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if(i=='+'):
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
                continue
            if(i=='-'):
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
                continue
            if(i=='*'):
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
                continue
            if(i=='/'):
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
                continue
            stack.append(int(i))
        return stack[0]
