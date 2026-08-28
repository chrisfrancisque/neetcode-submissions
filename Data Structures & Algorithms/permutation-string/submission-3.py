import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_key = {char: 0 for char in string.ascii_lowercase}
        s2_key = {char: 0 for char in string.ascii_lowercase}

        l = 0
        for r in range(len(s1)):
            s1_key[s1[r]]+=1
            s2_key[s2[r]]+=1
        
        if s1_key == s2_key:
            return True
        
        for r in range(len(s1), len(s2)):
            s2_key[s2[l]]-=1
            s2_key[s2[r]]+=1

            if s1_key == s2_key:
                return True

            l+=1

        return False



