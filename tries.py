class TrieNode:
    def __init__(self):
        self.children ={}
        # key: char
        # value: node
        self.end = False
        # this will signify if we are at the end of word
class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root 

        for c in word:
            # we need to iterate through the word

            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            index = ord(c) - ord('a')
            # this will return between [0:25]
            if cur.children[index] == None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root 

        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                return False
            cur = cur.children[index]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root

        for c in prefix:
            index = ord(c) - ord('a')

            if cur.children[index]== None:
                return False
            cur = cur.children[index]
        return True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        #dfs logic
        #we need to get to the end
        # we know if we run into a '.'

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c= word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.end
        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        # try with BFS

        def search(self, word: str) -> bool:
        
        q = collections.deque([(self.root,0)])

        while q:
            node, i = q.popleft()
            # i have my index and node
            # i now need to check the word[i]

            if i == len(word):
                if node.end:
                    return True
                continue
            if word[i]=='.':
                for child in node.children.values():
                    q.append((child,i+1))
            else:
                if word[i] in node.children:
                    q.append((node.children[word[i]],i+1))
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.ref = 0

        #self.ref will be used to mark that the word has been found

    def addWord(self, word):
        curr = self
        curr.ref += 1

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.ref += 1
        curr.isWord=True 
    def removeWord(self, word):
        cur = self
        cur.ref -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.ref -= 1
        # used to keep track of the words associated with each node
    
        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])

        res, visited = set(), set()

        def dfs(r, c, node, word):

            if (
                r < 0 or
                c < 0 or
                r == ROWS or
                c == COLS or
                board[r][c] not in node.children or
                node.children[board[r][c]].ref < 1 or
                (r, c) in visited 

            ):
                return 
            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord:
                node.Word = False
                res.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
            #backtracking
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return list(res)