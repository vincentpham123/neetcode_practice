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

        q = collections.deque([(self.root,0)])

        while q:
            node, i = q.popleft()
            # i have my index and node
            # i now need to check the word[i]

            if i == len(word):
                return True
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