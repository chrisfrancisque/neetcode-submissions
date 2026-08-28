class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

 

        queue = deque()
        length = 0

        for letter in s:
            while letter in queue:
                queue.popleft()
            
            queue.append(letter)
            length = max(length, len(queue))
        
        return length
                

        


        
        