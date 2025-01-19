class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count_neg = 0
        is_zero = False
        for num in nums:
            if num == 0:
                is_zero = True
            if num < 0:
                count_neg += 1
        
        return 0 if is_zero else (1 if count_neg%2 == 0 else -1)

        