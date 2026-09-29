# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head

        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        curr = head
        while curr.next:
            n1, n2 = curr.val, curr.next.val
            curr.next = ListNode(get_gcd(n1, n2), curr.next)
            curr = curr.next.next
        
        return head

        
        


        