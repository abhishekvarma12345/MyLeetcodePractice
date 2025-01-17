class MinStack:

    def __init__(self):
        # Initialize main stack and minimum stack
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        # push to the main stack
        self.stack.append(val)
        # update minimum stack if necessary
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # remove from main stack
        if self.stack:
            # If element to be popped is the minimum
            # remove from minimum stack
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()
        
    def top(self) -> int:
        # return top of the main stack
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        # return top of the minStack
        if self.minStack:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()