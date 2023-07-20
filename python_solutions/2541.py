class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Solution Overview
        # if we focus on index then we see that it applying the operation on same index on both array won't help us to make the element equal (it is kind of redundant operation)
        # also if the difference between these two number (number's at same index)is multiple of k then only we can make the two arrays equal.
        # our strategy would be to choose i,j such that num1[i] < nums2[i] and nums[j] < nums[j]
        # now if we consider i only then we see that there are some number of k's we need to add to nums1 in order to make it equal to nums2
        # same can be done for j as well
        # now these from i and j the required number of k's should be equal

        nums1_req_ks = 0
        nums2_req_ks = 0
        for idx in range(len(nums1)):
            if nums1[idx] == nums2[idx]:
                continue
            # number's are not equal and k = 0
            if k == 0:
                return -1
            diff = abs(nums1[idx]-nums2[idx])
            if diff%k == 0:
                if nums1[idx] > nums2[idx]:
                    nums2_req_ks += diff//k
                else:
                    nums1_req_ks += diff//k
            else:
                # if difference is not multiple of k then return -1
                return -1
        return nums1_req_ks if nums1_req_ks == nums2_req_ks  else -1

