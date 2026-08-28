class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stak;
        std::unordered_map<char, char> brak {
            {']', '['},
            {'}', '{'},
            {')', '('}
        };

        for(char c : s){
            if(c == '(' || c == '{' || c == '['){
                stak.push(c);
            }
            else if(stak.empty() || stak.top() != brak[c]){
                return false;
            }
            else if(stak.top() == brak[c]){
                stak.pop();
            }
           
        }

        return stak.empty();
        
    }
};
