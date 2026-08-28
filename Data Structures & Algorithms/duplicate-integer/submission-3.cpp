#include <iostream>
#include <unordered_set>
#include <vector>



class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> check{};

        for(int i{0}; i<nums.size();  ++i)
        {
            
            

            if(check.count(nums[i]))
            {
                return true;
            } 
            check.insert(nums[i]);
        }

        return false;




    }
};
