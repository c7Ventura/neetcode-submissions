class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in range(len(nums)):
            # add into dictionary if not seen before
            if(nums[i] not in frequency):
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] += 1
        # looping through hashmap to find top k elements and return them
        solution = []
        for i in range(k):
            # find the most frequent key and remove it from freq.
            # Then add it to return list
            most = self.mostFrequentHelper(frequency)
            solution.append(most)
        return solution
                
    def mostFrequentHelper(self, freq: dict[int, int]) -> int:
            # initialize most as the first thing in index
            # getting value of first item in freq. Need key
            most = next(iter(freq))
            for key in freq:
                if freq[key] > freq[most]:
                    most = key
            # remove most from freq + return it.
            freq.pop(most)
            return most 
