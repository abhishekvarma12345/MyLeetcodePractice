from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm = 0
        prefix_sum = [sm:=sm+i for i in nums]

        count = 0
        d = defaultdict(int)
        d[0] = 1
        for subsum in prefix_sum:
            if subsum - k in d:
                count += d[subsum - k]
            d[subsum] += 1
        return count
