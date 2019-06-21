from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_mid(left1, right1, left2, right2, index):
            if right1 == left1:
                return nums2[left2 + index - 1]
            if left2 == right2:
                return nums1[left1 + index - 1]
            mid = int(index / 2)
            if mid == 0:
                return min(nums1[left1], nums2[left2])
            if mid <= right1 - left1 and index - mid <= right2 - left2:
                index_1, index_2 = left1 + mid - 1, left2 + index - mid - 1
            else:
                if mid > right1 - left1:
                    index_1, index_2 = right1 - 1, left2 + index - right1 + left1 - 1
                else:
                    index_1, index_2 = left1 + index - right2 + left2 - 1, right2 - 1
            if nums1[index_1] < nums2[index_2]:
                index -= index_1 + 1 - left1
                left1 = index_1 + 1
                right2 = index_2 + 1
            elif nums1[index_1] > nums2[index_2]:
                index -= index_2 + 1 - left2
                right1 = index_1 + 1
                left2 = index_2 + 1
            else:
                return nums1[index_1]
            return get_mid(left1, right1, left2, right2, index)

        len1 = len(nums1)

        len2 = len(nums2)
        if (len1 + len2) % 2 != 0:
            index = (len1 + len2) // 2 + 1
            return float(get_mid(0, len1, 0, len2, index))
        else:
            index = (len1 + len2) // 2
            return (get_mid(0, len1, 0, len2, index) +
                    get_mid(0, len1, 0, len2, index + 1)) / float(2)


if __name__ == '__main__':
    so = Solution()
    re = so.findMedianSortedArrays([1, 2, 4], [3])
    print(re)
