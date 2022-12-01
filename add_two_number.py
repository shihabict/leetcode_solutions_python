class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_val = 0
        carry = root = ListNode(0)
        while l1 or l2 or sum_val:
            if l1: sum_val += l1.val; l1 = l1.next
            if l2: sum_val += l2.val; l2 = l2.next
            carry.next = carry = ListNode(sum_val % 10)
            sum_val //= 10
        return root.next


sol = Solution()
print(sol.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
