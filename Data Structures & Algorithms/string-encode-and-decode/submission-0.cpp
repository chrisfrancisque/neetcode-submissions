class Solution {
public:

    string encode(vector<string>& strs) {
        std::string encode;
        for(const string& word : strs)
        {
            encode += to_string(word.size()) + '#' + word;
            
        }

        return encode;

    }

    vector<string> decode(string s) {
        vector<string> decode;

        int i = 0;
        while(i < s.size())
        {
            int j = i;
            while(s[j] != '#')
            {
                ++j;
            }

            int length = stoi(s.substr(i, j-i));
            i = j + 1;
            j = i + length;
            decode.push_back(s.substr(i, length));
            i = j;
        }

        return decode;

    }
};
