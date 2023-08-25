class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Solution Overview
        # first let's thing about a simple problem
        # given and index can we tell that the height of the mountain , with peak being at this index
        # to answer this question we need some values ......
        # to find the height of mountain with peak fixed at index i , we need length of increasing sequence ending at index i in sub array nums[0:i+1] , and length of maximum decreasing sequence starting from index i in sub array nums[i:]
        # using this problem we can calculate the height of the mountain with peak fixed at index i , from this we can easily derived the numbers to be removed to make this mountain array
        # if we do the above operations for each index in the nums array , and our answer would be minimum among all the answers from each index
        nums_len = len(nums)
        inc_seq_len = [0 for i in range(nums_len)]
        dec_seq_len = [0 for i in range(nums_len)]
        for idx in range(0,nums_len):
            for idx2 in range(0,idx):
                if nums[idx] > nums[idx2]:
                    inc_seq_len[idx] = max(inc_seq_len[idx],inc_seq_len[idx2] +1)
        for idx in range(nums_len-1,-1,-1):
            for idx2 in range(idx+1,nums_len):
                if nums[idx] > nums[idx2]:
                    dec_seq_len[idx] = max(dec_seq_len[idx],dec_seq_len[idx2]+1)
        ans = nums_len
        for idx in range(1,nums_len-1):
            len_mountain_arr = inc_seq_len[idx] + 1 + dec_seq_len[idx]
            if len_mountain_arr < 3 or inc_seq_len[idx] == 0 or dec_seq_len[idx] == 0:
                continue
            elm_rm_cnt = nums_len - len_mountain_arr
            ans = min(ans , elm_rm_cnt)
        return ans
