import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            count_hr = 0
            for pile in piles:
                count_hr += math.ceil(pile/k)
            
            if count_hr <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
            
        return res
        


        