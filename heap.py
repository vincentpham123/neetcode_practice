from collections import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k 
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for this problem , a heap can be used to add the two largest, and adding a new rock to the pile

        stones = [-s for s in stones]
        
        heapq.heapify(stones)

        while len(stones)>1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone2 > stone1:
                # since the numbers are negative, if stone2 is greater, that means its less if its positibe
                
                heapq.heappush(stones, stone1-stone2)
        
        stones.append(0)
        return abs(stones[0])
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quicksort
        # is to partition, the list using an array.
        # choose a pivot, have a pointer a theleft
        # as i iterate through the list, i will swap
        k = len(nums)-k
        # this will provide the position of the kth largest number in the array

        left, right = 0 , len(nums)-1 

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
                # this means that k is on the right side of the pivot
                # and we try to sort the right side
            elif pivot > k:
                right = pivot -1 
            else:
                break
        
        return nums[k]

    def partition(self, nums, left, right):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill +=1 
        
        nums[fill], nums[right] = nums[right], nums[fill]
        #the fill is only updated when a number is less than the pivot
        # so where the fill stops, is the location of the pivot in the kinda sorted array
        # that is the reason for this switch

        return fill
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        maxHeap = [-count for count in counts.values()]

        heapq.heapify(maxHeap)


        time = 0 

        q = collections.deque()

        while maxHeap or q:
            time += 1 

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1

                if count:
                    # if it is not 0
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time