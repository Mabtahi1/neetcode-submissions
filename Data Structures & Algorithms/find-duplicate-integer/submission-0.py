class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapnum = {}

        for num in nums:
            if num in mapnum:
                return num

            mapnum[num] = 1
            
                