class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char,char> brackets {
            {')' , '('},
            {'}', '{'},
            {']' , '['} };
        
        std::stack<char> stac;

        for(char c : s){
            if((c== ')' || c == '}' || c == ']')){
                if(stac.empty()){
                    return false;
                }
                else if(stac.top() == brackets[c]){
                    stac.pop();
                }
                else{
                    return false;
                }


            }
            else{
                stac.push(c);
            }

        }

        return stac.empty();

    }
};
