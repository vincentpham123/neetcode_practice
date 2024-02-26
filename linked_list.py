class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyDict = {None: None}

        current = head 

        while current:
            copy = Node(current.val)
            copyDict[current] = copy
            # creating a copy that can be assessed with the dictionary
            current = current.next
        current = head 

        while current:
            copy = copyDict[current]
            copy.next = copyDict[current.next]
            # both of these point to a copy of the old

            copy.random = copyDict[current.random]
            current = current.next 
        return copyDict[head]
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head  = ListNode(None)
        current_1 = l1 
        current_2 = l2 

        carry = 0 
        tail = dummy_head

        while current_1 is not None or current_2 is not None or carry == 1:
            val1 = current_1.val if current_1 else 0 
            val2 = current_2.val if current_2 else 0


            cur_sum = val1 + val2 + carry 

            if cur_sum > 9:
                carry = 1 
            else:
                carry = 0
            new_node_sum = cur_sum % 10 

            new_node = ListNode(new_node_sum)
            tail.next = new_node
            tail = tail.next 

            if current_1:
                current_1 = current_1.next 
            else:
                current_1 = None
            if current_2:
                current_2 = current_2.next 
            else:
                current_2 = None
        return dummy_head.next