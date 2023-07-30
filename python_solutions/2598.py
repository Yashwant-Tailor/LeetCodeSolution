class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Solution Overview
        # if we take the module of every nums[i] with value then we would have 
        # 0 <= nums[i]%value < value
        # now let's say if we know the count of every remainder (nums[i]%value)
        # then the first non negative integer would be the minimum count out of all remainder
        rem_count = [0 for i in range(value)]
        for num in nums:
            num %= value
            rem_count[(num+value)%value] += 1
        min_count = None
        rem_num = None
        for i in range(value):
            if min_count is None:
                min_count = rem_count[i]
                rem_num = i
            elif min_count > rem_count[i]:
                min_count = rem_count[i]
                rem_num = i
        return rem_num + min_count * value
