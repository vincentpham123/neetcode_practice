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

class MedianFinder:

    def __init__(self):
        self.small, self.big = [], []

        # these will be two heaps that are equal in length
        # self.small is a max heap

    def addNum(self, num: int) -> None:
        # when do i add to the big, when the length of the small is greater than 
        
        if self.big and num > self.big[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -1 * num)
        

        
        if len(self.small) > len(self.big) + 1:
            heapq.heappush(self.big,
                heapq.heappop(self.small) * -1
            )

        if len(self.big) > len(self.small) + 1:
            heapq.heappush(self.small,
                heapq.heappop(self.big) * -1
            )

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return self.small[0] * -1 
        
        if len(self.small) < len(self.big):
            return self.big[0]

        return ((self.small[0]*-1)+self.big[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()