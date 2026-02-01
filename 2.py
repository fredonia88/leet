# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def build_linked_list(data_list):
    if not data_list:
        return

    dummy = ListNode()
    current_node = dummy
    for n in data_list:
        current_node.next = ListNode(int(n))
        current_node = current_node.next

    return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_list = [l1.val]
        l1_new = l1.next
        while l1_new:
            l1_list.insert(0, l1_new.val)
            l1_new = l1_new.next
        
        l2_list = [l2.val]
        l2_new = l2.next
        while l2_new:
            l2_list.insert(0, l2_new.val)
            l2_new = l2_new.next

        l1_int = int(''.join([str(i) for i in l1_list]))
        l2_int = int(''.join([str(i) for i in l2_list]))
        total = str(l1_int + l2_int)[::-1]

        return build_linked_list(total)

x = Solution()
l1 = build_linked_list([2,4,3])
l2 = build_linked_list([5,6,4])
result = x.addTwoNumbers(l1, l2)
while result: 
    print(result.val, '->', result.next)
    result = result.next