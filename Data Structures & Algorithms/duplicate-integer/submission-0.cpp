class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //for loop to iterate through list
        vector<int> observed;
        for(int i = 0; i < nums.size(); i++) {
            //iterate through observed list (change later)
            for(int j = 0; j < observed.size(); j++) {
                //check to see if item has already been observed
                if(nums[i] == observed[j]) {
                    return true;
                }
            }
                //end of for loop, add to the end of list
                //observed[observed.size() - 1] = nums[i];
                observed.push_back(nums[i]);
            }
            return false;
            
        }
    };