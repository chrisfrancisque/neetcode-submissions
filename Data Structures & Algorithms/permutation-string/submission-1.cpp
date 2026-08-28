class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char, int> count;
        std::unordered_map<char, int> check;

        if(s1.size() > s2.size())
        {
            return false;
        }

        for(int i = 0; i < s1.size(); ++i)
        {
            char c = s1[i];
            char s = s2[i];
            ++count[c];
            ++check[s];
        }

        int l = 0;
        int r = s1.size();

        while(r < s2.size())
        {
            if(count == check)
            {
                return true;
            }


            if(--check[s2[l]] == 0)
            {
                check.erase(s2[l]);
            }
            
             ++check[s2[r]];
            ++l;
            ++r;
           
        }

        return check == count;
    }
};
