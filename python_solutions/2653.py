class Solution:
    def get_xth_min(self,neg_num_count, x):
        for i in range(50,0,-1):
            if x <= neg_num_count[i]:
                return i * -1
            else:
                x -= neg_num_count[i]
        return 0
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # Solution Overview
        # using sliding window technique , keep track of all the negative integers in the given subarray.
        # we can take help of array to track the negative integers as the range nums[i] is : -50 <= nums[i] <= 50
        ans = []
        neg_num_count = [0 for i in range(51)]
        for idx , num in enumerate(nums):
            if num < 0 :
                neg_num_count[-1 * num] += 1
            if idx < k-1:
                continue
            xth_min = self.get_xth_min(neg_num_count,x)
            ans.append(xth_min)
            remove_element = nums[idx - (k-1)]
            if remove_element < 0:
                neg_num_count[-1 * remove_element] -= 1
        return ans
