class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevGroup = dummy

        while True:
            check = prevGroup.next
            count = 0

            while count < k and check:
                check = check.next
                count += 1

            if count < k:
                break

            prev = None
            curr = prevGroup.next
            groupHead = curr

            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            prevGroup.next = prev
            groupHead.next = curr
            prevGroup = groupHead

        return dummy.next