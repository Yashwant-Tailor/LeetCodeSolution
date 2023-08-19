class Solution:
    def isPos(self,initial_pow,pow,k,r):
        stations_cnt = len(initial_pow)
        req_pow = [0 for i in range(stations_cnt)]
        for st_idx in range(stations_cnt):
            req_pow[st_idx] = max(0,pow - initial_pow[st_idx])
        new_initial_pow = [0 for i in range(stations_cnt)]
        st_idx = 0
        curr_pow = 0
        while st_idx < stations_cnt:
            curr_pow += new_initial_pow[st_idx]
            if req_pow[st_idx] > curr_pow:
                req_pow[st_idx] -= curr_pow
                if req_pow[st_idx] > k:
                    return False
                k -= req_pow[st_idx]
                curr_pow += req_pow[st_idx]
                right_idx = st_idx + 2*r + 1
                if right_idx < stations_cnt:
                    new_initial_pow[right_idx] -= req_pow[st_idx]
            req_pow[st_idx] = 0
            st_idx += 1
        return True
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # Solution Overveiw
        # if we fix the maximum possible minimum power , the its easy to check that this can be achievalbe or not with building at most k power stations
        stations_cnt = len(stations)
        initial_pow = [0 for i in range(stations_cnt)]
        for idx,num_pow in enumerate(stations):
            left_idx = max(0,idx-r)
            right_idx = idx + r + 1
            initial_pow[left_idx] += stations[idx]
            if right_idx < stations_cnt:
                initial_pow[right_idx] -= stations[idx]
        curr_pow = 0
        max_pow = -1
        for idx in range(stations_cnt):
            curr_pow += initial_pow[idx]
            initial_pow[idx] = curr_pow
            max_pow = max(max_pow,initial_pow[idx])

        min_pow = 0 
        max_pow = max_pow + k + 1
        while min_pow+1 < max_pow:
            mid_pow = min_pow + (max_pow - min_pow)//2
            if self.isPos(initial_pow,mid_pow,k,r):
                min_pow = mid_pow
            else:
                max_pow = mid_pow
        return min_pow
