class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ck = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ck] = nums[i]
                ck += 1
        return ck        
        