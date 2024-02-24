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