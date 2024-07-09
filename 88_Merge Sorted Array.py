class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()

# Below code is only for testing in leetcode it's not needed to submit.
obj = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
obj.merge(nums1, 3, nums2, 3)
print(nums1)
