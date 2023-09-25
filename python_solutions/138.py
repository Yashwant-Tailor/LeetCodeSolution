"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Solution Overview
        # copy the list and maintain the prev and corresponding new ids of object in the hashmap so that we can quickly find the random node ids
        c_head = None
        c_tail = None
        curr_node = head
        id_map = {}
        while curr_node is not None:
            new_node = Node(curr_node.val)
            if c_head is None:
                c_head = new_node
                c_tail = new_node
            else:
                c_tail.next = new_node
                c_tail = new_node
            id_map[id(curr_node)] = new_node
            curr_node = curr_node.next
        curr_node = head
        c_tail = c_head
        while curr_node is not None:
            random = curr_node.random
            if random is None:
                c_tail.random = None
            else:
                random_id = id(curr_node.random)
                new_random_node = id_map[random_id]
                c_tail.random = new_random_node
            c_tail = c_tail.next
            curr_node = curr_node.next
        return c_head
