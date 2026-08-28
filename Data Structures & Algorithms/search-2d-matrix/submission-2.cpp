class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int low = 0;
        int high = (matrix.size()-1) * matrix[0].size() + matrix[0].size() -1;

        while(low <= high){
            int mid = (low + high)/2;

            if(matrix[mid/matrix[0].size()][mid%matrix[0].size()] == target){
                return true;
            }

            if(matrix[mid/matrix[0].size()][mid % matrix[0].size()] > target){
                high = mid -1;
            }
            else if(matrix[mid/matrix[0].size()][mid % matrix[0].size()] < target){
                low = mid + 1;
            }
        }

        return false;
    }
};
