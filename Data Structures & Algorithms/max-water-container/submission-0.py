class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            currarea = min(heights[l],heights[r]) * (r-l)
            maxarea = max(maxarea, currarea)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxarea        
            