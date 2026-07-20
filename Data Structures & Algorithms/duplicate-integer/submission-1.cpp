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
            else {
                return true;
            }
        }
        //nothing returned. No matches.
        return false;
    };
};