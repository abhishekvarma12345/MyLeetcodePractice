class Solution:
    def isPalindrome(self, s: str) -> bool:
        def brute():
            # Approach1:
            # Take each character and convert to lowercase, append if it is alphanumeric
            # Take the reverse and verify if original=reversed.
            alphanum_str = ""
            for char in s:
                char_lower = char.lower()
                if char_lower.isalnum():
                    alphanum_str += char_lower
            
            return alphanum_str == alphanum_str[::-1]
        
        def optimized():
            # Approach2:
            # Two pointers: start pointer-p1, end pointer-p2
            # Increase start pointer forward until we find alphanum character
            # Decrease end pointer from the back until we find alphanum character
            # compare by lowercasing characters at p1 and p2
            # If there is a mismatch then return False
            # If both pointers meet then exit return True

            p1 = 0
            p2 = len(s) - 1
            while p1 < p2:

                while p1 < p2 and not s[p1].isalnum():
                    p1 += 1
                
                while p1 < p2 and not s[p2].isalnum():
                    p2 -= 1
                
                if s[p1].lower() != s[p2].lower():
                    return False

                p1 += 1
                p2 -= 1

            return True
        
        return optimized()

