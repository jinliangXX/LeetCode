from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        one = m - 1
        two = n - 1
        for now in range(m + n - 1, -1, -1):
            if two < 0:
                nums1[now] = nums1[one]
                one -= 1
                continue
            if one < 0:
                nums1[now] = nums2[two]
                two -= 1
                continue
            if nums1[one] >= nums2[two]:
                nums1[now] = nums1[one]
                one -= 1
            else:
                nums1[now] = nums2[two]
                two -= 1
