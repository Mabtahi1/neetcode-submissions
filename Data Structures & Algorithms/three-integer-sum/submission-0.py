class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue    
            l = i + 1
            r = n -1

            while l < r:
                Summ = nums[i] + nums[l] + nums[r]

                if Summ > 0:
                    r -= 1
                elif Summ < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1   
                    while l < r and nums[r] == nums[l-1]:
                        r -= 1   

                    l += 1
                    r -= 1

        return res                      




