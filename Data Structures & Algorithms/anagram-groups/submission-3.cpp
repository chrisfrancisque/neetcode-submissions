#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;

        for(const auto& s : strs)
        {
            std::string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            res[sortedS].push_back(s);
        }
        std::vector<std::vector<std::string>> result;
        for(auto& pair : res )
        {
            result.push_back(pair.second);
        }

        return result;

        
    }
};
