class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # as the value range for numbers in nums array is small we can use the idea of count sort to store the values

        min_val = min(nums)
        max_val = max(nums)
        count_arr = [0 for idx in range(max_val - min_val + 1)]
        for num in nums:
            count_arr[num-min_val] += 1
        curr_num = max_val
        while k > count_arr[curr_num-min_val]:
            k -= count_arr[curr_num-min_val]
            curr_num -= 1
        return curr_num
