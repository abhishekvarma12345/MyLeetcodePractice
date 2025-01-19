class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        inc, dec = False, False
        equal = True
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] < nums[i - 1]:
                    inc = True
                else:
                    dec = True
                equal = False
                break
        
        
        if inc:
            for j in range(i+1, len(nums)):
                inc = inc and (nums[j] <= nums[j - 1])
        if dec:
            for j in range(i+1, len(nums)):
                dec = dec and (nums[j] >= nums[j - 1])
        
        return equal or inc or dec


        