class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy = ListNode()
        # tail = dummy
        #
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next
        #     tail = tail.next
        #
        # if l1:
        #     tail.next = l1
        # elif l2:
        #     tail.next = l2
        #
        # return dummy.next
        sorted_list = []
        i = j = 0
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                sorted_list.append(l1[i])
                i+=1
            else:
                sorted_list.append(l2[j])
                j+=1

        return sorted_list + l1[i:] + l2 [j:]
sol = Solution()
print(sol.mergeTwoLists([1,2,4,6,8], [2,4,5]))
