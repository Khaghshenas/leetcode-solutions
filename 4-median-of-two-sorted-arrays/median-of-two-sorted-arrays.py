class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        p1 = p2 = 0
        n = len(nums1)
        m = len(nums2)

        while p1 < n and p2 < m:
            if nums1[p1] < nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            else:
                merged.append(nums2[p2])
                p2 += 1

        merged.extend(nums1[p1:])
        merged.extend(nums2[p2:])

        total = n + m

        if total % 2 == 0:
            return (merged[total//2] + merged[total//2 - 1]) / 2
        else:
            return merged[total//2]
        