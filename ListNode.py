class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        node_before_a = list1
        for _ in range(a - 1):
            node_before_a = list1
            for _ in range(a - 1):
                node_before_a = node_before_a.next
