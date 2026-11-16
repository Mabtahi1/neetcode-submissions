class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapval = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapval:
                return [mapval[diff], i] 
            
            mapval[n] = i
