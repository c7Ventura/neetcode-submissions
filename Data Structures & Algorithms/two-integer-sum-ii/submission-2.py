class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i != j:
            if target == numbers[i] + numbers[j]:
                return [i + 1, j + 1]

            # too big, decrement j    
            elif target < numbers[i] + numbers[j]:
                j -= 1
            
            # too small, increment i
            elif target > numbers[i] + numbers[j]:
                i += 1