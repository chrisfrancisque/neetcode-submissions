class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> let;
        int l = 0;
        int max = 0;

        for(int r = 0; r < s.size(); ++r)
        {
            while(let.find(s[r]) != let.end())
            {
                let.erase(s[l]);
                ++l;
            }

            let.insert(s[r]);
            max = std::max(max, r-l + 1);
        }

        return max;
    }
};
