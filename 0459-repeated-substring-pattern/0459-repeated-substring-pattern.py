class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        cur_str = ""
        for char in s:
            cur_str += char
            if cur_str*(len(s)//len(cur_str)) == s and len(cur_str) != len(s):
                return True
        return False

        