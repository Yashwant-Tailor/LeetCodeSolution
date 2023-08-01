class Solution:
    def find_comb(self,curr_elm,req_elm_count,res,curr_comb,n):
        if req_elm_count == 0:
            res.append(curr_comb)
            return
        if curr_elm > n:
            return
        curr_comb1 = curr_comb.copy()
        self.find_comb(curr_elm+1,req_elm_count,res,curr_comb,n)
        curr_comb1.append(curr_elm)
        self.find_comb(curr_elm+1,req_elm_count-1,res,curr_comb1,n)
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Solution Overview 
        # Use backtracking to find all possible solutions
        res = []
        self.find_comb(1,k,res,[],n)
        return res
