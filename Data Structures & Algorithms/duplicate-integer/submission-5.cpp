class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> check ;
        for(int n : nums)
        {
            if(check.count(n)){
                return true;
            }

            check[n]++;
        }
        return false;

    }
};
