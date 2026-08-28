#include <unordered_map>
#include <string>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       

        std::unordered_map<int, int> compliment;
         
        for(int i = 0; i < nums.size(); ++i)
        {
            int diff = target - nums[i];
            if(compliment.find(diff) != compliment.end())
            {
                return {compliment[diff], i};
            }
            compliment.insert({nums[i],i});
        }
        
        return nums;
    }
};
