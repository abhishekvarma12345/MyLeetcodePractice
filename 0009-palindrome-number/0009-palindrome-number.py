class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        x_reverse = 0
        while x_copy:
            rem = x_copy%10
            x_reverse = 10*x_reverse + rem
            x_copy = x_copy//10
            
        return x == x_reverse