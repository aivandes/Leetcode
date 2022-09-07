class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []
        half = (len(nums1) + len(nums2))

        
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                a.append(nums1.pop(0))
            else:
                a.append(nums2.pop(0))
        
        a += nums1 + nums2
        print(a)
        return a[half // 2] if half % 2 != 0 else (a[half //2] + a[(half - 1) // 2]) / 2
