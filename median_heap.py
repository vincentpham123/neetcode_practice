class MedianFinder:

    def __init__(self):
        self.smallHeap, self.bigHeap = [], []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.smallHeap, num * -1)
        # once i add to smallHeap, i need to make sure that it is smaller than the bigHeap

        if self.smallHeap and self.bigHeap and (self.smallHeap[0]*-1 > self.bigHeap[0]):
            heapq.heappush(self.bigHeap,heapq.heappop(self.smallHeap)*-1)

        # i then need to check the lengths

        if len(self.smallHeap) > len(self.bigHeap) +1:
            heapq.heappush(self.bigHeap, heapq.heappop(self.smallHeap)*-1)
        if len(self.bigHeap) > len(self.smallHeap) +1:
            heapq.heappush(self.smallHeap, heapq.heappop(self.bigHeap)*-1)
    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.bigHeap):
            return self.smallHeap[0] * -1
        if len(self.smallHeap) < len(self.bigHeap):
            return self.bigHeap[0]

        return (self.bigHeap[0] + self.smallHeap[0]*-1)/2

