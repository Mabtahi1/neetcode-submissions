class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_max = []
        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(heap_max,[dist , x, y])
            if len(heap_max) > k:
                heapq.heappop(heap_max)


        res = []
        while heap_max:
            dist,x,y = heapq.heappop(heap_max)
            res.append([x,y])
        return res            