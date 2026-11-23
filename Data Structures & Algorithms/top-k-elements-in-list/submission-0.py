class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapval = {}

        for num in nums:
            mapval[num] = 1 + mapval.get(num,0)

        heap = []
        for num in mapval.keys():
            heapq.heappush(heap, (mapval[num], num))

            if len(heap) > k:
                heapq.heappop(heap)    


        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res    