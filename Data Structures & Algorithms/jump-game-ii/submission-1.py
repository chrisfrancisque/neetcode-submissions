class Solution:
    def jump(self, nums: List[int]) -> int:

        goal = len(nums) - 1

        if goal == 0:
            return 0
        jumps = 0


        l = 0
        r = 0
        while r < goal:
            farthest = r

            for i in range(l , r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            jumps += 1

            
        
        return jumps

            

                
            


        