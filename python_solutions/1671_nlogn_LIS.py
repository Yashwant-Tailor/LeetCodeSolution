class Solution:
    def get_seq_len(self,curr_seq,num):
        from bisect import bisect_left
        idx = bisect_left(curr_seq,num)
        if idx == len(curr_seq):
            curr_seq.append(num)
        else:
            curr_seq[idx] = num
        return idx
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Solution Overview
        # first let's thing about a simple problem
        # given and index can we tell that the height of the mountain , with peak being at this index
        # to answer this question we need some values ......
        # to find the height of mountain with peak fixed at index i , we need length of increasing sequence ending at index i in sub array nums[0:i+1] , and length of maximum decreasing sequence starting from index i in sub array nums[i:]
        # using this problem we can calculate the height of the mountain with peak fixed at index i , from this we can easily derived the numbers to be removed to make this mountain array
        # if we do the above operations for each index in the nums array , and our answer would be minimum among all the answers from each index
        
        # in our solution to find the increasing or decreasing sequence lenth we are using O(N^2) algorithm but there exits and O(N logN) to find the longest increasing sequence length
        # HERE's the link : https://cp-algorithms.com/sequences/longest_increasing_subsequence.html

        nums_len = len(nums)
        inc_seq_len = [0 for idx in range(nums_len)]
        dec_seq_len = [0 for idx in range(nums_len)]
        curr_seq = []
        for idx in range(nums_len):
            inc_seq_len[idx] = self.get_seq_len(curr_seq,nums[idx])
        curr_seq.clear()
        for idx in range(nums_len-1,-1,-1):
            dec_seq_len[idx] = self.get_seq_len(curr_seq,nums[idx])
        ans = nums_len
        for idx in range(nums_len):
            mountain_arr_len = inc_seq_len[idx] + 1 + dec_seq_len[idx]
            if mountain_arr_len < 3 or inc_seq_len[idx] == 0 or dec_seq_len[idx] == 0:
                continue
            elm_rm_cnt = nums_len - mountain_arr_len
            ans = min(ans,elm_rm_cnt)
        return ans
