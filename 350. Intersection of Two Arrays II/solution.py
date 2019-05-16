class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = list()
        nums1_dict = dict()
        for num in nums1:
            if num in nums1_dict:
                nums1_dict[num] += 1
            else:
                nums1_dict[num] = 1
        for key in nums2:
            if key in nums1_dict and nums1_dict[key] > 0:
                result.append(key)
                nums1_dict[key] -= 1
        return result
