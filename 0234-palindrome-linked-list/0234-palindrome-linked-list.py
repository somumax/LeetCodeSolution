# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        traversal = []
        curr = head 
        while curr:
            traversal.append(curr.val)
            curr = curr.next
        for i in range(len(traversal) // 2):
            if (traversal[i] != traversal[len(traversal) - 1 - i]):
                return False
        return True
        
        