# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: break into two halves
        second = slow.next
        slow.next = None

        # Step 3: reverse second half
        prev = None
        curr = second
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        second = prev

        # Step 4: merge alternately
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2