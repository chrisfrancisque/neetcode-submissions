# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        head = ListNode()
        dummy = head

        track = []
        heapq.heapify(track)

        for index, node in enumerate(lists):
            if node:
                heapq.heappush(track, (node.val, index, node))
        

        while track:
            curr, index, node = heapq.heappop(track)

            head.next = ListNode(curr)
            head = head.next

            if node.next:
                node = node.next
                heapq.heappush(track, (node.val, index, node))

        
        return dummy.next



        