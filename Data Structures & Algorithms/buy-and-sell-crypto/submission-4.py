class Solution:
    def maxProfit(self, prices: List[int]) -> int:  

        small = 101
        big = -1

        for num in prices:
            small = min(small, num)

            curr = num - small

            big = max(curr, big)

        
        return big


        
        