class Solution:
    def removeDuplicates(self,nums):
        if len(nums) <= 2:
            return len(nums)
        
        # Pointer for the next position to place the allowed duplicate
        j = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        
        return j

# use below code only for testing don't use it in leetcode
obj = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = obj.removeDuplicates(nums)
print(k)
print(nums[:k])


# OR ####################

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        # Pointer for the next position to place the allowed duplicate
        j = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        
        return j

# use below code only for testing don't use it in leetcode
obj = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = obj.removeDuplicates(nums)
print(k)  
print(nums[:k])
