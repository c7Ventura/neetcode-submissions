class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Runtime: nLogm --> checking each list, then binary search
        # binary search within correct list.
        # find each list length
        for i in range(len(matrix)):
            # check range of list first?
            # could be in this range. Check list
            if matrix[i][0] <= target <= matrix[i][-1]:
            # if not suspected to hold target, skip?
                start = 0
                end = len(matrix[i]) - 1
                mid = (start + end) // 2 
                while start <= end:
                    mid = (start + end) // 2
                    if target == matrix[i][mid]:
                        return True
                    elif matrix[i][mid] > target:
                        end = mid - 1
                    elif matrix[i][mid] < target:
                        start = mid + 1
        return False