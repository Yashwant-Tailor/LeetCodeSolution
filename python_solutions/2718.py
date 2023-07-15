class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # Solution Overview
        # let's first solve the simple problem 
        # if every entry in queries is unique --> the (type,index) pair is unique
        # in this case we can update the answer by maintaining the values added till now 
        # Now in given problem if we don't have unique entry then we can take help of hashmap (dictionary) to get the unique entries --> as we know that for a pair of (type,index) the val which will be stayed will be the last entry for this pair and previous entries will be overwritten.

        row_unique = {}
        col_unique = {}
        for idx,query in enumerate(queries):
            qtype,qindex,qval = query
            if qtype == 0:
                row_unique[qindex] = idx
            else:
                col_unique[qindex] = idx
        # it will store the unique queries which will be applied to matrix
        row_idx = {} 
        col_idx = {}
        for qindex,idx in row_unique.items():
            row_idx[idx] = qindex
        for qindex,idx in col_unique.items():
            col_idx[idx] = qindex
        
        # now iterate over queries and apply them in order
        row_num_sum = 0
        col_num_sum = 0
        ans = 0
        for idx,query in enumerate(queries):
            qtype,qindex,qval = query
            curr_sum = 0
            if qtype == 0:
                if idx in row_idx:
                    row_num_sum += qval
                    curr_sum = n * qval - col_num_sum
            else:
                if idx in col_idx:
                    col_num_sum += qval
                    curr_sum = n * qval - row_num_sum
            ans += curr_sum
        return ans
