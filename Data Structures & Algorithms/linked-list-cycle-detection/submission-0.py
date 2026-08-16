# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, visited = False):
        self.val = val
        self.next = next
        self.visited = visited


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # iterate through list
        current = head

        while current != None:
            # cycle detected
            if current.visited:
                return True

            # no cycle detected
            current.visited = True
            current = current.next

        return False
            
