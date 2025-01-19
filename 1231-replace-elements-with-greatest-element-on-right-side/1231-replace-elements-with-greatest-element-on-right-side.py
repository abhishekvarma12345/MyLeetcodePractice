class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_right = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = greatest_right
            greatest_right = max(greatest_right, temp)
        return arr