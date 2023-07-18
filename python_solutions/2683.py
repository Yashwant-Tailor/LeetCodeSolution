class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Solution Overview
        # if we take XOR of all elements in array derived then it will become zero
        # as we will have every number occuring two times in our XOR

        xor = 0
        for num in derived:
            xor ^= num
        return True if xor == 0 else False
