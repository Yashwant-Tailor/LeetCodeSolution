class MyStack:

    def __init__(self):
        from collections import deque
        self.elm_q = deque()
        self.elm_cnt = 0
    def append_q(self,elm_cnt,q2):
        while elm_cnt > 0 :
            temp_elm = self.elm_q.popleft()
            self.elm_q.append(temp_elm)
            elm_cnt -= 1

    def push(self, x: int) -> None:
        self.elm_q.append(x)
        self.append_q(self.elm_cnt,self.elm_q)
        self.elm_cnt += 1

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
