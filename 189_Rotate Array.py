class Solution:
    def rotate(self, nums,k):
        new_nums = k%len(nums)
        nums[:] = nums[-new_nums:] + nums[:-new_nums]
        return nums   

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7],6))
