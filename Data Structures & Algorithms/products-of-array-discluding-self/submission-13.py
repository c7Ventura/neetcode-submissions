class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #base case
        if len(nums) == 2:
            return [nums[1], nums[0]]
        # iterate through array once to get complete product
        #NOTE: python does not allow for empty lists. Pre-fill with 0
        prod = [0] * len(nums)
        prod[0] = nums[0]
        product = nums[0]
        containsZero = False
        zeroCount = 0
        # calculate complete product first
        for i in range(1, len(nums)):
            # maybe start at index 1 with index 0 already in?
            # dont allow product to get messed up due to 0 being multiplied into product
            if nums[i] != 0:
                product *= nums[i]
            else: 
                containsZero = True
                zeroCount += 1
            
        # iterate through array second time to divide complete product each time
        for j in range(len(nums)):
            # do not allow for division by zero. Do not change anything.
            # if this is the only zero, we are excluding this, should be original prod.
            if nums[j] == 0 and zeroCount == 1:
                prod[j] = product
            
            if nums[j] != 0:
                prod[j] = product // nums[j]
            
            if nums[j] != 0 and containsZero and zeroCount >= 1:
                prod[j] = 0
        return prod