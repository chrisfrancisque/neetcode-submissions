#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<vector<std::string>> solution;

        for(int i = 0; i< strs.size(); ++i)
        {
            std::string current = strs[i];
            sort(current.begin(), current.end());

            bool found = false;
            
            for(int j = 0; j< solution.size(); ++j)
            {
                
                std::string key = solution[j][0];
                std::string Skey = key;
                sort(Skey.begin(), Skey.end());

                if(current == Skey)
                {
                    solution[j].push_back(strs[i]);
                    found = true;
                    break;
                }
            }
                if(!found)
                {
                   
                    solution.push_back({strs[i]}) ;
                }
            


        }

        return solution;
    }
};
