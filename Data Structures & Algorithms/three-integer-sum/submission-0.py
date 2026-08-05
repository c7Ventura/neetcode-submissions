class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ansSet = []

        # sort array
        nums.sort()

        # CHANGED: instead of using i and j as the moving pointers,
        # i is now the fixed number we are checking.
        for i in range(len(nums) - 2):

            # ADDED: Skip duplicate fixed numbers to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # ADDED: left and right are the two pointers searching for
            # the remaining two numbers that sum with nums[i] to make 0.
            left = i + 1
            right = len(nums) - 1

            # CHANGED: We move left and right until they meet.
            while left < right:

                # CHANGED: Calculate the sum using the fixed number
                # and the two moving pointers.
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    # add ans into array
                    ans = [nums[i], nums[left], nums[right]]
                    ansSet.append(ans)

                    # ADDED: Move both pointers after finding a valid triplet
                    # so we can search for other possible combinations.
                    left += 1
                    right -= 1

                    # ADDED: Skip duplicate values so we do not add
                    # the same triplet multiple times.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                # CHANGED: If the sum is too large, decrease the right pointer
                # because the array is sorted.
                elif sum > 0:
                    right -= 1

                # CHANGED: If the sum is too small, increase the left pointer
                # because the array is sorted.
                elif sum < 0:
                    left += 1

        return ansSet