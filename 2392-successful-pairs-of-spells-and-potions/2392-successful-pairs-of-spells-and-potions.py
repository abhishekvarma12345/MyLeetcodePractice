class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def binary_search(potions, spell: int, success: int):
            n = len(potions)
            left = 0
            right = n - 1
            while left <= right:
                mid = (left+right)//2
                if ((mid > 0) and (spell*potions[mid - 1] < success <= spell*potions[mid])) or (mid==0 and success<=spell*potions[mid]):
                    return mid
                elif success <= spell*potions[mid]:
                    right = mid - 1
                elif success > spell*potions[mid]:
                    left = mid + 1
            return n
        
        ans = []
        n = len(potions)
        for spell in spells:
            ans.append(n-binary_search(potions, spell, success))
        return ans



