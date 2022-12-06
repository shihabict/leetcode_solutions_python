# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head

        for i in range(n):

            p1 = p1.next
            if p1 is None:
                head = head.next
                return head

        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return head


if __name__ == '__main__':
    # head = [1, 2, 3, 4, 5]
    # n = 2
    # head = [1]
    # n = 1
    head = [1, 2]
    n = 1
    ll = Solution()
    res = ll.removeNthFromEnd(head, n)
    print(res)
