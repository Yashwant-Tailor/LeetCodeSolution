class Solution:
    def candy(self, ratings: List[int]) -> int:
        l_idx = 0
        r_idx = len(ratings)-1
        l_candy = 0
        r_candy = 0
        l_rating = -1
        r_rating = -1
        candy = [0 for idx in range(len(ratings))]
        for itr in range(len(ratings)):
            l_candy = l_candy+1 if ratings[l_idx]>l_rating else 1
            r_candy = r_candy+1 if ratings[r_idx]>r_rating else 1
            candy[l_idx] = max(candy[l_idx],l_candy)
            candy[r_idx] = max(candy[r_idx],r_candy)
            l_rating = ratings[l_idx]
            r_rating = ratings[r_idx]
            l_idx += 1
            r_idx -= 1
        return sum(candy)
        
