#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // mapping charCout to list of anagrams
        std::unordered_map<std::string, std::vector<std::string>> res;

        for(const auto& s : strs)
        {
            std::vector<int> count(26,0);

            for(const auto c : s)
            {
                count[c - 'a'] += 1;
            }
        
            std::string key = to_string(count[0]);
            for(int i = 1; i < 26; ++i)
            {
                key += ',' + to_string(count[i]);
            }

            res[key].push_back(s);
        }

            vector<vector<std::string>> result;
            for(const auto& pair : res)
            {
                result.push_back(pair.second);
            }

        return result;


    }
};
