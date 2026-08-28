#include <vector>
#include<unordered_map>
#include <numeric>
#include <functional>

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> solution;
        std::unordered_map<int, int> output;

        for(int i = 0; i < nums.size(); ++i)
        {
            std::vector<int> currentNums = nums;
            currentNums.erase(currentNums.begin() + i);

            int product = std::accumulate(currentNums.begin(), currentNums.end(), 1, std::multiplies<int>());
            solution.push_back(product);
        }
        return solution;

    }
};
