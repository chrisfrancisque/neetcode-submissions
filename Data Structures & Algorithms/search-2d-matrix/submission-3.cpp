class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int min = 0;
        int max = matrix.size() * matrix[0].size() -1;

        while(min <= max){
            int mid = (min+max)/2;

            if(matrix[mid/matrix[0].size()][mid%matrix[0].size()] == target){
                return true;
            }

            if(matrix[mid/matrix[0].size()][mid%matrix[0].size()] > target){
            max = mid -1;
            }
            else if(matrix[mid/matrix[0].size()][mid%matrix[0].size()] < target){
                min = mid + 1;
            }

        }
        
        return false;
    }
};
