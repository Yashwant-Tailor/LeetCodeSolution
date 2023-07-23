class Solution:
    def to_binary_str(self,n):
        s = ''
        if n == 0:
            s = '0'
            return s
        while n > 0:
            if n & 1 :
                s += '1'
            else:
                s += '0'
            n >>= 1
        return s[::-1]

    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # Solution Overview
        # first lest see what will be the decimal value val for a substring
        # as per the given condition 
        # val ^ first = second (take XOR of first on both side)
        # val ^ first ^ first = second ^ first
        # val = second ^ first
        # now we know that 0 <= val <= 10^9 (as per given constraints)
        # --> we will only need to check for substring of size at most 32

        # for every substring we can maintain a hashmap to store the index where it start
        hashmap_ind = {}
        for i in range(len(s)):
            for j in range(i,min(i+32,len(s))):
                if s[i:j+1] not in hashmap_ind:
                    hashmap_ind[s[i:j+1]] = i
        ans = []
        for query in queries:
            first,second = query
            val = first ^ second
            val_binary_str = self.to_binary_str(val)
            if val_binary_str in hashmap_ind:
                li = hashmap_ind[val_binary_str]
                ri = li + len(val_binary_str)-1
                ans.append([li,ri])
            else:
                ans.append([-1,-1])
        return ans

