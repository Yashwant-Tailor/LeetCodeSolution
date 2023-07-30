class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # Solution Overview
        # just check for every possbile number which can fulfill the required condition
        for i in range(num+1):
            curr_num = i
            curr_rev_num = int(str(curr_num)[::-1])
            curr_sum = curr_num + curr_rev_num
            if num == curr_sum:
                return True
        return False
