class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //for loop to iterate through list
        unordered_map<int, int> observed;
        for(int i = 0; i < nums.size(); i++) {
            //if we haven't observed this number, add it. 
            if(!observed.contains(nums[i]))
            // 0 is placeholder for value
                    observed.try_emplace(nums[i], 0);
            // have observed a number, return true.
            else {
                return true;
            }
        }
        //nothing returned. No matches.
        return false;
    };
};

//NOTE: Using hashmap provides O(n) space and time complexity since
// iteration over the list is only done once. The hashmap grows at most 
// the full space of the list, which is O(n).