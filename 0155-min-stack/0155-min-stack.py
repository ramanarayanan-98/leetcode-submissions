class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not len(self.stack):
            self.stack.append([val,val])
            return
        
        self.stack.append([val,min(val,self.stack[-1][1])])
        # print(self.stack)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if not len(self.stack):
            return None
        
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not len(self.stack):
            return None
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()