class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        is_ap = True
        for i in range(2, len(arr)):
            is_ap = is_ap and (arr[i] - arr[i - 1] == diff)
        return is_ap
