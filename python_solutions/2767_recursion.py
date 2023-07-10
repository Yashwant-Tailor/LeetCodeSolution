class Solution:
    def get_partitions_len(self, sticks_binary_representation, s):
        ans = 0
        curr_partition = ""
        for idx, s_ith in enumerate(s):
            if idx == 0:
                curr_partition += s_ith
            else:
                # check if we have stick on this location
                if 1 & sticks_binary_representation > 0:
                    # we have one partition till left of this index (idx) 'curr_partition'
                    # if its valid partition then increase the count 
                    if self.is_valid_partition(curr_partition):
                        ans += 1
                    else:
                        return False,ans
                    # start new partion starting from idx
                    curr_partition = s_ith
                else:
                    # we don't have any stick here so just append this character to curr_partition
                    curr_partition += s_ith
                sticks_binary_representation >>= 1
        # increase the count if the last partition is valid
        if self.is_valid_partition(curr_partition):
            ans += 1
        else:
            return False, ans
        return True,ans

    def get_decimal_num(self, binary_num):
        res = 0
        for binary_bit in binary_num:
            res <<= 1
            if binary_bit == '1':
                res += 1
        return res

    def is_power_of_5(self, num):
        while num != 1:
            if num % 5 == 0:
                num /= 5
            else:
                return False
        return True

    def is_valid_partition(self, partition):
        # check that it does not contain leading zero
        if partition[0] == '0':
            return False
        # convert binary to decimal
        decimal_num = self.get_decimal_num(partition)
        if self.is_power_of_5(decimal_num):
            return True
        return False

    def minimumBeautifulSubstrings(self, s: str) -> int:
        # Solution_Overview
        # we can use recursion to find the the partition of string
        # and once we have a partition then we can validate that if this partion is having all beautiful substrings.

        # Edge case handling
        if len(s) == 1:
            if s == "0":
                return -1
            else:
                return 1
        s_len = len(s)
        max_number_of_sticks = s_len - 1  # we can partition len(s) numbers using 'sticks' many sticks ; where 0 <= 'sticks' <= len(s) - 1
        ans = None
        # in this for loop , 1's in binary representation of i will represent the sticks
        for i in range(0, 2 ** max_number_of_sticks):
            can_partition,num_of_partitions = self.get_partitions_len(i,s)
            if can_partition:
                if ans is None:
                    ans = num_of_partitions
                else:
                    ans = min(ans, num_of_partitions)
        return -1 if ans is None else ans
