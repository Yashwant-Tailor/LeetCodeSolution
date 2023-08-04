class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.curr_non_value_idx = set() # we can either use queue or hashtable to maintain the index of num which are not equal to value
        self.window_size = 0
        self.curr_idx = 0
        

    def consec(self, num: int) -> bool:
        prev_idx = self.curr_idx
        self.window_size += 1
        if num != self.value:
            self.curr_non_value_idx.add(self.curr_idx)
        self.curr_idx += 1
        if self.window_size < self.k:
            return False
        elif self.window_size > self.k:
            self.curr_non_value_idx.discard(prev_idx-self.k)
        return len(self.curr_non_value_idx) == 0


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
