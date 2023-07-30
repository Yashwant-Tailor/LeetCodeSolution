class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # Solution Overview
        # just do as mentioned in the problem statement

        dis_elm = set()
        for num in nums:
            dis_elm.add(num)
            rev_num = int(str(num)[::-1])
            dis_elm.add(rev_num)
        return len(dis_elm)
