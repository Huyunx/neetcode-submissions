class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]       
        self.currmin=2**31 - 1
    def push(self, val: int) -> None:
        self.stack.append(val)
        c=val
        if(self.minstack):
            c=min(self.minstack[-1],val)
        self.minstack.append(c)
        return
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
        return 
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
