class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # sort the list first
        # nums.sort()
        # #print(nums)
        # if len(nums) == 0:
        #     return 0
        
        # count = 1
        # # check whether the curr = nums[i+1] - 1 (should be greater than by 1)
        # for i in range(len(nums)): 
        #     # if so, increment count
        #     curr = nums[i]
        #     # if first time incrementing, need to double count (2 ints observed)
        #     if i+1 < len(nums) and curr == nums[i+1] - 1:
        #         #print("Iteration count: ", i)
        #         #print(curr)
        #         #print(nums[i+1])
        #         count += 1
        # # return output.
        # return count

        #explain new optimized solution + why it is only O(n) at worst.
        numSet = set(nums)
        longest = 0
        # look at each number in set
        for num in numSet:
            # if there is no number -1 than num exists
            # this should be the starting number in the consecutive sequence
            if (num - 1) not in numSet:
                length = 1
                # incrementing the count FROM the inital for loop.
                # Essentially checking how long the +1 streak lasts.
                while (num + length) in numSet:
                    length += 1
                # Comparing longest streak to current streak acheived.
                longest = max(length, longest)
        return longest

        #Explanation: This code is O(n) due to the inner loop essentially picking up whereever the outer loop left off. In an example [2,3,4,5,10,11,12], at the very beginning of the outer loop, starting at 2, a check is done to ensure that this number is a starting index (a value where nothing -1 comes before it). If this is the case, we can increment a streak counter and do a while loop to check whether the sequence can be kept up. This in its worst case, ends up going to N. If this is the case, we know that every number after 2 in the outer for loop exits after evauluating the if statement to be false. This means we only went 1 index into the outer for loop and n-1 operations in the inner loop. This overall results in O(n) time complexity.
        