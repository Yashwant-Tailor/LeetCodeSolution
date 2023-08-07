class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # Solution Overview
        # simple iterate over every queries and then check that can we make it equal to any word in dictionary

        ans = []
        for query in queries:
            can_change = False
            for word in dictionary:
                char_diff_count = 0
                for idx in range(len(query)):
                    if query[idx] != word[idx]:
                        char_diff_count += 1
                        if char_diff_count > 2:
                            break
                if char_diff_count <= 2:
                    can_change = True
                    break
            if can_change:
                ans.append(query)
        return ans

