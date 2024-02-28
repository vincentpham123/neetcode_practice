class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # what is hard about this problem is that the lists can have as many arrays as it wants
        if not lists or len(lists) == 0:
            return None
        # to account for basecases where lists is empty

        while len(lists) > 1:
            mergedList = []

            for i in range(0,len(lists),2):
                # incrementing by 2
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                # if it is out of bonds, set to none
                mergedList.append(self.merge2Lists(list1, list2))
            lists = mergedList
        return lists[0]
        
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1 
        if l2:
            tail.next = l2
        return dummy.next
        