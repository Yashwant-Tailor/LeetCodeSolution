class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Solution Overview
        # keep track of elements in A and B till index i

        curr_A = set()
        curr_B = set()
        C = []
        prev_ci = 0
        for i in range(len(A)):
            C.append(prev_ci)
            if A[i] in curr_B:
                C[i] += 1
            curr_A.add(A[i])
            if B[i] in curr_A:
                C[i] += 1
            curr_B.add(B[i])
            prev_ci = C[i]
        return C
