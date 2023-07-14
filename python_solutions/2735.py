class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        # Solution Overview
        # keep the minimum value we can get after k shifts for a number which was initially at position i
        # so minimum would be the nums[i : i+x] (we are assuming that i+x < len(nums)) if that is not the case then just take the mod of length

        min_val = [num for num in nums]
        ans = None
        n = len(nums)
        for shift in range(0,n):
            curr_cost = x * shift
            for i in range(0,n):
                # first update the minimum we can get after performing the shift for the number at the index i
                min_val[i] = min(min_val[i], nums[(i+shift)%n])
                # we will pick this chocolate with minimum cost
                curr_cost += min_val[i]
            # update the answer if with 'shift' many rotations we can minimize the total cost
            ans = curr_cost if ans is None else min(ans,curr_cost)
        return ans
