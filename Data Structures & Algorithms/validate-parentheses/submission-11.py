class Solution:
    def isValid(self, s: str) -> bool:
      check = []
      mapping = {")" : "(", "]" : "[", "}" :"{"}
      
      for c in s:
        if c in mapping:
            if check and check[-1] == mapping[c]:
                check.pop()
            else:
                return False
        else:
            check.append(c)
            
      return True if not check else False
        