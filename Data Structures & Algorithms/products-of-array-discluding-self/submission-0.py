class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero = nums.count(0)

        if zero > 1:
            return [0] * len(nums)

        prod = 1

        for x in nums:
            if x != 0:
                prod *= x

        for i in range(len(nums)):
            if zero == 1:
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            else:
                nums[i] = prod // nums[i]

        return nums