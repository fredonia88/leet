from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode: val={self.val}, next={self.next}"

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        target = length - n
        node = dummy
        for _ in range(target):
            node = node.next
        
        node.next = node.next.next

        return dummy.next
    
def build_linked_list(start: int, end: int) -> ListNode:
    
    dummy = ListNode(0, None)
    head = dummy
    for i in range(start, end+1):
        node = ListNode(i, None)
        head.next = node
        head = head.next

    return dummy.next


if __name__ == '__main__':

    head = build_linked_list(1, 5)

    sol = Solution()
    result = sol.removeNthFromEnd(head, 2)
    print(result)

        