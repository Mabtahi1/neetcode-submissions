class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if num in map:
                return True
                break
            
            map[num] = 1
        return False            