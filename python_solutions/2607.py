class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # Solution Overview
        # length of each subarray of size k will be equal if and only if each group of index%k is having same value 
        # i.e.
        # let's say sum0 = arr[0] + arr[1] + ....... + arr[k-1]
        # now sum1 = arr[1] + arr[2] + ..... + arr[k]
        # sum1 - sum0 = arr[k] - arr[0] 
        # 0 = arr[k] - arr[0]
        # arr[k] = arr[0]
        from math import floor,ceil
        vis = [False for i in range(len(arr))]
        n = len(arr)
        ans = 0
        for i in range(k):
            if not vis[i]:
                group_elm = []
                idx = i
                while not vis[idx]:
                    vis[idx] = True
                    group_elm.append(arr[idx])
                    idx += k
                    idx %= n
                # to perform minimum operation to make all elements equal is equivalent to converting all the numbers in group to median of the group (not average)
                group_elm.sort()
                group_len = len(group_elm)
                if group_len == 1:
                    continue
                floor_median = group_elm[floor(group_len/2)]
                ceil_median = group_elm[ceil(group_len/2)]
                floor_median_op = 0
                ceil_median_op = 0
                for elm in group_elm:
                    floor_median_op += abs(floor_median - elm)
                    ceil_median_op += abs(ceil_median - elm)
                ans += min(floor_median_op,ceil_median_op)
        return ans
