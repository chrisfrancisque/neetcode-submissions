class Solution {
public:

    void backtrack(int n, int openC, int closedC, vector<string>& res, 
    string current){
        
        if(openC == closedC && openC == n){
            res.push_back(current);
            return;
        }

        if(openC < n){
            current += '(';
            backtrack(n, openC + 1, closedC, res, current);
            current.pop_back();
        }

        if(closedC < openC){
            current += ')';
            backtrack(n, openC, closedC + 1, res, current);
            current.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string current;
        backtrack(n, 0, 0, res, current);
        return res;
        
    }
};
