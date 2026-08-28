#include <vector>
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);

        for(int i = 1; i < n; ++i)
        {
            res[i] = res[i-1] * nums[i-1];
        }

        int current = 1;

        for(int i = nums.size() -1; i >= 0; --i)
        {
            res[i] *= current;
            current *= nums[i];
        }
        
        return res;

    }
};
