class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()

        for num in nums:
            if num in map:
                return True
                break
            
            map.add(num)
        return False            