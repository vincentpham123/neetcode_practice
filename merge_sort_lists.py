class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        middle = self.find_middle(head)

        left_half = head
        right_half = middle.next
        middle.next = None 
        # breaking the two halves 

        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)

        return self.mergeLists(left_sorted,right_sorted)

    def find_middle(self, head):
        slow = fast = head 

        # the idea is that fast will go throught the list twice as fast. 
        # when it reaches the end, slow should be in the middle 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeLists(self, left, right):
        dummy = ListNode()

        current = dummy

        while left and right:
            
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next 
        if left:
            current.next = left
        if right:
            current.next = right
        return dummy.next