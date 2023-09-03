class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Solution Overview
        # if we sort the array , and try to see any two consecutive elemnts in the sorted array
        # the observation we can make is that , increasing the larger element is not optimal , we should always try to apply this operation on smaller elemnt and then make it equal to larger element 
        # while doing so other larger element will also increase , we need to add the operation correctly to make all element equal 
        # see solution for more details
        nums.sort()
        op_cnt = 0
        ans = 0
        idx = 1
        while idx < len(nums):
            ans += op_cnt
            ans += abs(nums[idx] - nums[idx-1])
            op_cnt += abs(nums[idx] - nums[idx-1])
            idx += 1
        return ans
        
