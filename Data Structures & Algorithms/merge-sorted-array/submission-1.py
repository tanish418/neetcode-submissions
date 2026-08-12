class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        l= m
        r = n
        while l>0 and r>0:
            if nums1[l-1]>nums2[r-1]:
                nums1[last] = nums1[l-1]
                l-=1
            else:
                nums1[last] = nums2[r-1]
                
                r-=1
            last-=1    
        while r>0:
            nums1[last] = nums2[r-1]
            r-=1   
            last-=1        