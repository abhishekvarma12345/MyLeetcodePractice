class Trie:

    def __init__(self):
        self.hash_map = {"*": 0}

    def insert(self, word: str) -> None:
        initial_map = self.hash_map
        for char in word:
            if char not in self.hash_map:
                self.hash_map[char] = {"*":0}
            self.hash_map = self.hash_map[char]
        self.hash_map["*"] = 1
        self.hash_map = initial_map
    
    def search(self, word: str) -> bool:
        initial_map = self.hash_map
        found = True
        for char in word:
            if char in self.hash_map:
                self.hash_map = self.hash_map[char]
            else:
                found = False
                break
        found = found and self.hash_map["*"]
        self.hash_map = initial_map

        if found:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        initial_map = self.hash_map
        found = True
        for char in prefix:
            if char in self.hash_map:
                self.hash_map = self.hash_map[char]
            else:
                found = False
                break
        
        self.hash_map = initial_map

        if found:
            return True
        else:
            return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)