# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even = head
        oddhead = head.next
        odd = oddhead
        while odd and odd.next:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next
        even.next = oddhead
        return head
        