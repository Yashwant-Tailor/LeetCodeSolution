class MedianFinder:
    # Solution Overview 
    # use two heap to keep track of left half and right half of the stream
    
    def __init__(self):
        self.left_half = []
        self.right_half = []
        self.elm_cnt = 0
        

    def addNum(self, num: int) -> None:
        import heapq as hp
        self.elm_cnt += 1
        if self.elm_cnt%2 == 1:
            if len(self.right_half) == 0:
                hp.heappush(self.left_half,-num)
            elif self.right_half[0] < num:
                right_elm = hp.heappop(self.right_half)
                hp.heappush(self.right_half,num)
                hp.heappush(self.left_half,-right_elm)
            else:
                hp.heappush(self.left_half,-num)
        else:
            if -self.left_half[0] > num:
                left_elm = hp.heappop(self.left_half)
                hp.heappush(self.right_half,-left_elm)
                hp.heappush(self.left_half,-num)
            else:
                hp.heappush(self.right_half,num)
        

    def findMedian(self) -> float:
        if self.elm_cnt%2 == 0:
            return (-self.left_half[0] + self.right_half[0])/2
        else:
            return -self.left_half[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
