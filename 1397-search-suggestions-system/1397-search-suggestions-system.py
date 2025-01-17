from collections import deque
class Trie:
    def __init__(self):
        self.hash_map = {"*": 0}
    
    def insert(self, word: str) -> None:
        initial_map = self.hash_map
        cur_str = ""
        for char in word:
            cur_str += char
            if cur_str not in self.hash_map:
                self.hash_map[cur_str] = {"*": 0}
            self.hash_map = self.hash_map[cur_str]
        self.hash_map["*"] = 1
        self.hash_map = initial_map

    def search(self, prefix: str) -> list[str]:
        initial_map = self.hash_map
        cur_str = ""
        for char in prefix:
            cur_str += char
            if cur_str in initial_map:
                initial_map = initial_map[cur_str]
            else:
                return []
        
        suggestions = []
        q = deque([initial_map])
        if initial_map["*"] == 1: suggestions.append(cur_str)
        while q:
            node = q.popleft()
            for key in node:
                if key != "*":
                    if node[key]["*"] == 1:
                        suggestions.append(key)
                    q.append(node[key])
        return suggestions
                
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        obj = Trie()
        for prod in products:
            obj.insert(prod)
        
        ans = []
        cur_str = ""
        for char in searchWord:
            cur_str += char
            ans.append(sorted(obj.search(cur_str))[:3])
        
        return ans


        