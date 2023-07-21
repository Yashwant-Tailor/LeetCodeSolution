class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Solution Overview
        # there are two solutions
        # Solution1 : using sorted banned 
        #       In this solution we will sort banned array and now from [1,n] we will try to pick numbers such that they are not present and sum of these numbers should not exceed maxSum
        # Solution2 : using hashmap (avoid doing sorting)
        #       In this solution we create a hashmap for each element in banned so that when we pick a number from [1,n] , we will see if this number is present in banned or not . We we will also make sure that sum of the selected element should not exceed maxSum

        hashmap = set()
        for ban_el in banned:
            hashmap.add(ban_el)
        curr_sum = 0
        selected_elem_count = 0
        for i in range(1,n+1):
            if i in hashmap:
                continue
            if curr_sum + i <= maxSum:
                selected_elem_count += 1
                curr_sum += i
        return selected_elem_count
