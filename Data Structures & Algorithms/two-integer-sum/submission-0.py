class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     for i in range(len(nums)): 
        # second pointer pointing at end of list
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                    return [i, j]
                # cant add an item at same index. No other case.
     return [-1, -1]
            
