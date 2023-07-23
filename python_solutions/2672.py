class Solution:
    def get_curr_pair_count(self,nums_color,idx,n):
        ans = 0 
        if nums_color[idx] == 0:
            return 0
        if idx-1 >=0 and nums_color[idx-1] == nums_color[idx]:
            ans += 1
        if idx+1 < n and nums_color[idx+1] == nums_color[idx]:
            ans += 1
        return ans

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        # Solution Overview
        # keep track of answer[i] and for each query update the answer[i] accordingly
        
        answer = []
        curr_answer = 0
        nums_color = [0 for i in range(n)]
        for idx,query in enumerate(queries):
            index,color = query
            if color == nums_color[index]:
                answer.append(curr_answer)
                continue
            distorted_pair = self.get_curr_pair_count(nums_color,index,n)
            curr_answer -= distorted_pair
            nums_color[index] = color
            newly_added_pair = self.get_curr_pair_count(nums_color,index,n)
            curr_answer += newly_added_pair
            answer.append(curr_answer)
        return answer
