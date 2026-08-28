class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int res = 0;
        unordered_set<char> track;

        for(int r = 0; r < s.size(); ++r){
            while(track.find(s[r]) != track.end()){
                track.erase(s[l]);

                l++;
            }
            track.insert(s[r]);
            res = max(res, r-l + 1);
        }

        return res;
    }
};
