class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # Solution Overview
        # if we sort the array and process the queries in sorted order then we can iteratively calculate the answer
        nums.sort()
        new_queries = [(queries[i],i) for i in range(len(queries))]
        new_queries.sort(key=lambda x : x[0])
        # for first query calculate the answer by find the diffs from every nums[i]
        greater_elm_count = 0 
        less_elm_count = 0
        curr_query_op = 0
        idx = 0
        curr_query_num = new_queries[idx][0]
        answer = []
        nums_idx = 0
        for num in nums:
            curr_query_op += abs(num-curr_query_num)
            if curr_query_num >= num:
                less_elm_count += 1
                nums_idx += 1
            else:
                greater_elm_count += 1
        answer.append((curr_query_op,new_queries[idx][1]))
        idx += 1
        # now for each further query[i] update the previous answer[i-1]
        while idx < len(new_queries):
            prev_query_num = curr_query_num
            prev_less_elm_count = less_elm_count
            curr_query_num = new_queries[idx][0]
            while nums_idx < len(nums) and curr_query_num >= nums[nums_idx]:
                curr_query_op -= abs(nums[nums_idx]-prev_query_num)
                curr_query_op += abs(curr_query_num - nums[nums_idx])
                nums_idx += 1
                less_elm_count += 1
                greater_elm_count -= 1
            query_num_diff = abs(curr_query_num-prev_query_num)
            curr_query_op += (prev_less_elm_count - greater_elm_count) * query_num_diff
            answer.append((curr_query_op,new_queries[idx][1]))
            idx += 1
        answer.sort(key=lambda x : x[1])
        answer = [answer[i][0] for i in range(len(answer))]
        return answer
