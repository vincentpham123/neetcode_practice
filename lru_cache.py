# the trick to this problem is determining how to keep track of the least recently used key value pair
# could do a queue that keeps track, however that would require extra variables 
# a better data structure to use is linked list
# can minipulate the order of things with minimum effort
class Node:
    def __init__(self, key, value):
        self.key = key
        # this is allow us to access the node in the hashmap
        self.value = value 
        # this will give us access to the value when we access the node from the hashmap 

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 

        self.cache = {}
        # cache will store key: nodes!
        self.left, self.right = Node(0,0), Node(0,0)
        # this will be the end points for the linkedlike
        #left.next will designate the least recently used, while right.prev will designate the most recently used
        self.left.next = self.right
        self.right.prev = self.left
        # nothing inbetween in the beginning

    # i now need functions to remove from the linked list, and insert

    def remove(self, node):
        # when i remove, i need to remove the node from the lis 
        previous_node, next_node = node.prev, node.next 

        previous_node.next = next_node 
        next_node.prev = previous_node 
        # the node has now been removed from the linked list 
    def insert(self, node):
        # when i insert a new one, it has to become the prev to the right pointer 
        # so i need to update 4 directional values 
        previous_right, right_node = self.right.prev, self.right

        previous_right.next = right_node.prev = node

        node.prev, node.next = previous_right, right_node
    def get(self, key: int) -> int:
        # when get, i nede to return the val from the node if its in the cache

        if key in self.cache:
            # when i am getting a value, it moves up the linked list 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value 
            # this will return the value 

            # i still need to set the left and right nodes
        return -1 

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            # if the key exists, i need to remove from the linked list
            # reason: to insert the new key value pair 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # inputting the new cache 

        # i also need to check the cache's capacity
        if len(self.cache) > self.cap:
            # if this is the case, i remove the least recently used which is next to the left
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)