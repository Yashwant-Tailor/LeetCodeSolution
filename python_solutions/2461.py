class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # maintain hashmap to track the count of elements in current length k interval

        elm_cnt = {}
        curr_sum = 0
        max_sum = 0
        for idx , num in enumerate(nums):
            curr_sum += num
            if num in elm_cnt:
                elm_cnt[num] += 1
            else:
                elm_cnt[num] = 1
            if idx >= k:
                del_elm = nums[idx-k]
                curr_sum -= del_elm
                elm_cnt[del_elm] -= 1
                if elm_cnt[del_elm] == 0:
                    elm_cnt.pop(del_elm)
            if idx >= k-1 and len(elm_cnt) == k:
                max_sum = max(max_sum,curr_sum)
        return max_sum
                

