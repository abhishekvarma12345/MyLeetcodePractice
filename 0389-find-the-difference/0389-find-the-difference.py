from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_freq = defaultdict(int)
        for char in t:
            char_freq[char] += 1
        
        for char in s:
            char_freq[char] -= 1
        
        for char in char_freq:
            if char_freq[char]:
                return char

        
        