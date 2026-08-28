#include <unordered_map>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_map<int, std::unordered_set<char>> row;
        std::unordered_map<int, std::unordered_set<char>> col;
        std::map<std::pair<int, int>, std::unordered_set<char>> square;
        
        for(int i = 0; i<9; ++i)
        {
            for(int j = 0; j < 9; ++j)
            {
                if(board[i][j] == '.')
                {
                    continue;
                }

                std::pair<int, int> squareKey = {i/3, j/3};

                if(row[i].count(board[i][j]) || col[j].count(board[i][j]) || 
                square[squareKey].count(board[i][j]))
                {
                    return false;
                }

                row[i].insert(board[i][j]);
                col[j].insert(board[i][j]);
                square[squareKey].insert(board[i][j]);
            }

        }

        return true;

        
    }
};
