class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> muns(nums.begin(),  nums.end());
        int longer = 0;
        for(int num : muns)
        {
          
            if(muns.find(num-1) == muns.end()) 
            {
               int length = 1;
               while(muns.find(num + length) != muns.end())
               {
                ++length;
               }

               longer = max(longer, length);
            } 
        }
        return longer;
    }
};
