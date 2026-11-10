class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_time(piles, k):
            totaltime = 0
            for p in piles:
                totaltime += math.ceil(p/k)
            return totaltime    
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            
            
            if total_time(piles, k) <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

        

