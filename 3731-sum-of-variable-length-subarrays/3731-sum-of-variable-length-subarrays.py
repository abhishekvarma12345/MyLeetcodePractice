class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix_sm = [0]
        for i in range(len(nums)):
            prefix_sm.append(prefix_sm[-1]+nums[i])
        
        tot = 0
        for i in range(len(nums)):
            tot += prefix_sm[i+1] - prefix_sm[max(0, i-nums[i])]

        return tot