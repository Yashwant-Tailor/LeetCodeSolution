class Solution:
    def __init__(self):
        self.prime_nums = [2,3,5,7,11,13,17,19,23,29]
        self.prime_num_bit_pos = {
            2 : 0,
            3 : 1,
            5 : 2,
            7 : 3,
            11 : 4,
            13 : 5,
            17 : 6,
            19 : 7,
            23 : 8,
            29 : 9
        }
    def get_binary_rep_of_prime_fac(self,num):
        # return -1 if the prime factorization of the number is having some prime power's greater than 1 (we have that prime number present at least two times)

        if num == 1:
            # for special case handling
            return 0
        res_bin_rep = 0
        for prime_num in self.prime_nums:
            fac_count = 0
            while num > 1 and num%prime_num == 0:
                fac_count += 1
                num //= prime_num
            if fac_count > 1:
                return -1
            elif fac_count == 0:
                continue
            set_bit_pos = self.prime_num_bit_pos[prime_num]
            res_bin_rep |= (1<<set_bit_pos)
        return res_bin_rep


    def squareFreeSubsets(self, nums: List[int]) -> int:
        # Solution Overview
        # if we represent the product of the numbers in its prime factorization 
        # then the product is square free integer if and only if we have each prime number power equal to 1 in its prime factorization
        # we know that there are 10 prime numbers in range 1 to 30
        # if we select some primes out of these 10 primes , then we will have a product 
        # we can find the count for this product if we store the state of count till previous index
        from collections import defaultdict
        n = len(nums)
        MOD = int(1e9+7)
        count_of_1 = 0
        total_prime_count = len(self.prime_nums)
        pre_sf_arr_count = [0 for i in range(1<<total_prime_count)]
        pre_sf_arr_count[0] = 1
        for i in range(1,n+1):
            prm_fac_bin_rep = self.get_binary_rep_of_prime_fac(nums[i-1])
            if prm_fac_bin_rep == -1:
                # this number has some prime number in its factorization at least two times ,  it won't be useful in any subarray
                continue
            curr_sf_arr_count = pre_sf_arr_count.copy()
            if nums[i-1] == 1:
                count_of_1 += 1
            else:
                # now iterate over every group and check if we can multiply this number to that group
                for i in range(1<<total_prime_count):
                    if (prm_fac_bin_rep & i) == 0:
                        # we don't have any common prime factor between the group and this number prime factorization
                        # update the count for the new group
                        new_group_bin_rep = prm_fac_bin_rep | i
                        curr_sf_arr_count[new_group_bin_rep] += pre_sf_arr_count[i]
                        curr_sf_arr_count[new_group_bin_rep] %= MOD
            pre_sf_arr_count = curr_sf_arr_count
        ans = 0
        for i in range(1,1<<total_prime_count):
            ans += pre_sf_arr_count[i]
            ans %= MOD
        # we can select any group of 1 and we can create ans many subarray by appending this 1's
        group1_total_count = 1
        curr_2p = 2
        while count_of_1 >0 :
            if count_of_1 & 1:
                group1_total_count *= curr_2p
                group1_total_count %= MOD
            count_of_1 >>= 1
            curr_2p *= curr_2p
            curr_2p %= MOD
        ans  = (ans*group1_total_count)%MOD
        # these 1's as single group not adding any extra prime number
        ans += group1_total_count - 1 # group1_total_count contains one elment which is not selecting any 1 at all
        ans %= MOD

        return (ans%MOD + MOD)%MOD

