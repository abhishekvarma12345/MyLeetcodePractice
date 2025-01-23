class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        cost1, cost2 = 0, 0
        for i in range(len(arr)):
            cost1 += abs(arr[i] - brr[i])

        arr.sort()
        brr.sort()
        cost2 += k
        for i in range(len(arr)):
            cost2 += abs(arr[i] - brr[i])

        return min(cost1, cost2)


    


