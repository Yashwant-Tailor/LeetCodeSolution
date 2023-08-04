class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Solution Overview
        # find the primes in the range [left ,right]
        # then check for each consecutive prime the difference and return the first pari with minimum difference , if we don't have any pair then return [-1,-1]

        # segmented seive
        from math import sqrt
        # first mark primes till sqrt(right)
        lim = int(sqrt(right))
        primes_till_lim = []
        mark_prime = [True for i in range(lim+1)]
        if lim > 0:
            mark_prime[0] = False
            mark_prime[1] = False
        # store all primes till sqrt(right)
        for i in range(2,lim+1):
            if mark_prime[i]:
                primes_till_lim.append(i)
                for j in range(i*i , lim+1 , i):
                    mark_prime[j] = False
        is_prime = [True for i in range(left,right+1)]
        # using primes till sqrt(right) mark the composite number in the range [left,right]
        for prime in primes_till_lim:
            for j in range(max(prime*prime , (left+prime-1)//prime * prime),right+1,prime):
                is_prime[j-left] = False
        prime_l_to_r  =[]
        # handle the special case for marking the composite numbers in range [left,right]
        if left == 1:
            is_prime[left-1] = 0
        # find all the primes in range [left,right]
        for i in range(left,right+1):
            if is_prime[i-left]:
                prime_l_to_r.append(i)
        if len(prime_l_to_r)<= 1:
            return [-1,-1]
        # find the minimum difference between two consecutive primes
        min_diff = prime_l_to_r[-1] - prime_l_to_r[0]
        ans = [prime_l_to_r[0],prime_l_to_r[-1]]
        for i in range(1,len(prime_l_to_r)):
            curr_diff = prime_l_to_r[i] - prime_l_to_r[i-1]
            if curr_diff < min_diff:
                min_diff = curr_diff
                ans = [prime_l_to_r[i-1],prime_l_to_r[i]]
        return ans


