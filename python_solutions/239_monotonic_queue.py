class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution Overview
        # we can maintain a deque to find the largest element in the window of size k
        # the core idea is that if we have a largest element in the window then we don't need the element left to this largest element as these elements won't be used in further any window

        from collections import deque
        win_k = deque()
        max_num = -int(1e5)
        max_arr = []
        for idx , num in enumerate(nums):
            while len(win_k)>0 and win_k[-1][0] <= num:
                win_k.pop()
            win_k.append([num,idx])
            if win_k[0][1] <= idx-k:
                win_k.popleft()
            if idx >= k-1:
                max_arr.append(win_k[0][0])
        return max_arr
                
