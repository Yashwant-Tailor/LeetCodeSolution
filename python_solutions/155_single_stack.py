class MinStack:

    def __init__(self):
        # Solution Overview
        # keep track of minimum we have so far along with current element
        # for single stack keep track of minimum number history 
        # for more details about the solution visit this page
        # https://www.baeldung.com/cs/stack-constant-time
        self.min_stack = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_val = val
            stack_val = val
        elif self.min_val < val:
            stack_val = val
        else:
            stack_val = val + (val - self.min_val)
            self.min_val = val
        self.min_stack.append(stack_val)

    def pop(self) -> None:
        if self.min_val > self.min_stack[-1]:
            prev_min_val = self.min_val + (self.min_val - self.min_stack[-1])
            self.min_val = prev_min_val
        self.min_stack.pop()

    def top(self) -> int:
        if self.min_val <= self.min_stack[-1]:
            top_val = self.min_stack[-1]
        else:
            top_val = self.min_val
        return top_val
        

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
