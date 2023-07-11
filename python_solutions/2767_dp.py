class Solution:
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
        # we will use dynamic programming to calculate the answer for string of length i
        # using this value we will try to update the other possible value

        # Edge case handling
        if len(s) == 1:
            if s == "0":
                return -1
            else:
                return 1
        dp = [[False for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for curr_s_len in range(1, len(s) + 1):
            for curr_num_of_partition in range(1, len(s) + 1):
                curr_partition = ""
                for start_of_curr_partition in range(curr_s_len, 0, -1):
                    curr_partition = s[start_of_curr_partition - 1] + curr_partition
                    if self.is_valid_partition(curr_partition):
                        dp[curr_s_len][curr_num_of_partition] = True if dp[curr_s_len - len(curr_partition)][
                            curr_num_of_partition - 1] else dp[curr_s_len][curr_num_of_partition]
        for i in range(1 , len(s)+1):
            if dp[len(s)][i] :
                return i
        return -1
