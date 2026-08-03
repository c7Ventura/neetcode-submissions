class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        mid = len(nums) // 2
        end = len(nums) - 1

        while start <= end:
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                start = mid + 1
                mid = (start + end) // 2
            
            elif target < nums[mid]:
                end = mid - 1
                mid = end // 2 
        
        # havent found number, return -1
        return -1