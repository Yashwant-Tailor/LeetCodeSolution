class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Solution Overview
        # find all the equal number and their indices, then iteratively calculate the arr[i]

        ind_hashmap = {}
        for idx,num in enumerate(nums):
            if num in ind_hashmap:
                ind_hashmap[num].append(idx)
            else:
                ind_hashmap[num] = []
                ind_hashmap[num].append(idx)
        arr = []
        for num,idx_list in ind_hashmap.items():
            left_sum = []
            right_sum = []
            l_sum = 0
            r_sum = 0
            for idx in range(len(idx_list)):
                if idx > 0:
                    l_sum += idx * abs(idx_list[idx]-idx_list[idx-1])
                    r_sum += idx * abs(idx_list[len(idx_list)-1-idx]-idx_list[len(idx_list)-idx])
                left_sum.append(l_sum)
                right_sum.append(r_sum)
            right_sum.reverse()
            for idx in range(len(left_sum)):
                sum_i = left_sum[idx] + right_sum[idx]
                arr.append((sum_i,idx_list[idx]))
        arr.sort(key = lambda x : x[1])
        arr = [arr[i][0] for i in range(len(arr))]
        return arr
