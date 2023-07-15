class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Solution Overview
        # simply iterate over every number in range {1,n} (O(N))
        # check that if this number can be partitioned (2^6 * 6)
        ans = 0
        for i in range(1, n+1):
            sq_i = i * i 
            str_sq_i = str(sq_i)
            if len(str_sq_i) == 1:
                ans += sq_i if int(sq_i) == i else 0
            else:
                m = len(str_sq_i)
                can_partitioned = False
                for j in range(0 , 2 ** (m-1)):
                    curr_str = ''
                    curr_partition_sum = 0
                    for k in range(0,m-1):
                        curr_str += str_sq_i[k]
                        # if we have stick separating kth and (k+1)th character
                        if j & (1<<k):
                            curr_partition_sum += int(curr_str)
                            curr_str = ''
                    curr_str += str_sq_i[m-1]
                    curr_partition_sum += int(curr_str)
                    if curr_partition_sum == i:
                        can_partitioned= True
                        break
                if can_partitioned:
                    ans += sq_i
        return ans
