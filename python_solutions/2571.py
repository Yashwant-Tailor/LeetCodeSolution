class Solution:
    def minOperations(self, n: int) -> int:
        # Solutino Overview
        # in binary representation of n
        # if we have two consecutive bit equal to 1
        # then it is optimal to add one 2's power to reduce the '11' into '100' and then use an subtract operation to make it equal to zero
        ans = 0
        while n > 0:
            if n & 1 == 0:
                n >>= 1
                continue
            # find the group of 1's in binary representation of n
            set_bit_count = 0
            while n & 1 == 1:
                set_bit_count += 1
                n >>= 1
            if set_bit_count == 1:
                # use an substract operation to make it equal to zero
                ans += 1
            else:
                # use one add operation to convert this group to 1's (111....111) into (10000...0000){it has size one greater than the group}
                ans += 1
                # after add operation we need to set the next bit
                n |= 1
        return ans
