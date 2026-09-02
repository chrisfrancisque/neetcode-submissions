# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        k = len(lists)
        heap = []

        for index in range(k):
            if lists[index] is not None:
                head_val = lists[index].val
                heapq.heappush(heap, (head_val, index))

                lists[index] = lists[index].next
        

        merged_list = ListNode(None, None)

        tail = merged_list

        while heap:
            element, index = heapq.heappop(heap)
            tail.next = ListNode(element, None)

            tail = tail.next

            if lists[index]:
                val_to_add = lists[index].val
                heapq.heappush(heap, (val_to_add, index))
                lists[index] = lists[index].next
            
        

        

        return merged_list.next
