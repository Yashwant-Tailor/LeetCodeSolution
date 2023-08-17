class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # if k is not present in the nums then just return 0
        # otherwise 
        # let's divide the array into two parts 
        # left (nums elements before the index of k)
        # right (nums elements after the index of k)
        # now for each subarray in left and right ending at the index of k , if we know the count of greater and less element then it is easy to calculate that the median would be k or not
        # let's say left has an subarray ending at index of k which has 2 less , 1 greater element than k
        # and right has an subarray ending at index of k which has 2 greater , 1 less element than k
        # now if we consider these two subarray along with k , then its clear that in this subarray(combining left+right) we have 3 greater , 3 less element than k
        # we can maintain a dictionary to keep track of the count of less and greater element
        from collections import defaultdict
        left_diff = defaultdict(lambda: 0)
        right_diff = defaultdict(lambda : 0)
        idx_k = None
        for idx,num in enumerate(nums):
            if num == k:
                idx_k = idx
                break
        if idx_k is None :
            return 0
        # calculate the left_diff
        idx = idx_k - 1
        curr_diff = 0
        while idx >= 0:
            curr_diff += 1 if nums[idx] > k else -1
            left_diff[curr_diff] += 1
            idx -= 1
        # calculate the right_diff
        idx = idx_k + 1
        curr_diff = 0
        while idx < len(nums):
            curr_diff += 1 if nums[idx] > k else -1
            right_diff[curr_diff] += 1
            idx += 1
        ans = (left_diff[0] + 1) * (right_diff[0]+1)
        all_diffs = set(left_diff.keys()).union(set(right_diff.keys()))
        for diff in all_diffs:
            if diff <= 0:
                continue
            neg_diff = -1 * diff
            ans += left_diff[diff] * right_diff[neg_diff] + left_diff[neg_diff] * right_diff[diff]
            neg_diff += 1
            ans += left_diff[neg_diff]*right_diff[diff] + left_diff[diff] * right_diff[neg_diff]
            if diff == 1:
                ans += left_diff[diff] + right_diff[diff]
        return ans


