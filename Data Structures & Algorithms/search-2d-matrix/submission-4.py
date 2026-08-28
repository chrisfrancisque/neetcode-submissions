class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index_flat = len(matrix) * len(matrix[0]) - 1

        l = 0
        r = index_flat

        while(l <= r):
            mid = (l+r) // 2
            print(f'mid ={mid}')

            if matrix[mid//len(matrix[0])][mid%len(matrix[0])] < target:
                l = mid + 1
                print(f'l = {mid}')
            elif matrix[mid//len(matrix[0])][mid%len(matrix[0])] > target:
                r = mid - 1
                print(f'r = {mid}')
            elif matrix[mid//len(matrix[0])][mid%len(matrix[0])] == target:
                return True
            
        
        return False
            



        