class Solution:
    def detectCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                ptr = head

                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr

        return None