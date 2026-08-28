class Solution {
public:
    bool isValid(string s) {
        std::stack<char> brack;
        std::unordered_map<char, char> pair { 
        {')', '('} , 
        {'}', '{'} , 
        { ']' , '['}  };

        for( char c: s)
        {
            if(c == '{' || c == '[' || c== '(')
            {
                brack.push(c);
           } else{    
                if(brack.empty() || brack.top() != pair[c] )
                {
                    return false;
                }
                brack.pop();
                
            }
            
        }

       return brack.empty();
    }
};
