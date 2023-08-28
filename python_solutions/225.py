class MyStack:

    def __init__(self):
        from collections import deque
        self.elm_q = deque()
        self.temp_q = deque()
    def append_q(self,q1,q2):
        while len(q1) > 0:
            q2.append(q1.popleft())

    def push(self, x: int) -> None:
        self.temp_q.append(x)
        self.append_q(self.elm_q,self.temp_q)
        self.append_q(self.temp_q,self.elm_q)

    def pop(self) -> int:
        return self.elm_q.popleft()
        

    def top(self) -> int:
        return self.elm_q[0]
        

    def empty(self) -> bool:
        return len(self.elm_q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
