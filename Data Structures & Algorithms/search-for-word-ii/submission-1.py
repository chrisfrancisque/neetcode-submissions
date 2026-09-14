class Trie:
    def __init__(self):
        self.children = {}
        self.isEndOf = False
    
    def addWord(self, word) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isEndOf = True
    

    
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            root.addWord(word)
        
        l = len(board)
        w = len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == l or c == w or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEndOf:
                res.add(word)
            
            dfs(r + 1 , c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))
        
        for i in range(l):
            for j in range(w):
                dfs(i, j, root, "")
        
        return list(res)
            






