class Solution:
    def get_elm(self,nums1,nums2,idx):
        left1,right1 = 0,len(nums1)-1
        left2,right2 = 0,len(nums2)-1
        while idx > 0:
            mid1 = left1 + (right1-left1)//2
            mid2 = left2 + (right2-left2)//2
            t_elm_cnt = (mid1-left1+1) + (mid2-left2+1)
            if left1 > right1 :
                return nums2[left2+idx-1]
            if left2 > right2:
                return nums1[idx+left1-1]
            if t_elm_cnt <= idx:
                if nums1[mid1] < nums2[mid2]:
                    idx -= (mid1 - left1 + 1)
                    left1 = mid1 + 1
                else:
                    idx -= (mid2 - left2 + 1)
                    left2 = mid2 + 1
            else:
                if nums1[mid1] < nums2[mid2]:
                    right2 = mid2-1
                else:
                    right1 = mid1-1
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Solution Overview
        # let try to solve a little different problem
        # given two sorted array , can we tell the k th smallest element between these two arrays.
        # we can do that in log(n+m) 
        # the logic would be similar to binary search 
        # WLOG (without loss of generality) , assume min , max element of nums1 are (a,b) and for nums2 (c,d)
        # now find mid idx in both arrays
        # a < nums1[mid1] < b , c < nums2[mid2] < d
        # WLOG , assume numsa[mid1] < nums2[mid2]
        # now if k > mid1 + mid2 , then for sure we can discard the elements [a,nums1[mid1]]
        # and if k < mid1 + mid2 , then for sure we can discard the elements [nums2[mid2],d]

        t_len = len(nums1) + len(nums2)
        idx1,idx2 = (t_len-1)//2,t_len//2
        median_elm1 = self.get_elm(nums1,nums2,idx1+1)
        median_elm2 = median_elm1 if idx1 == idx2 else self.get_elm(nums1,nums2,idx2+1)
        return (median_elm1 + median_elm2)/2
        
