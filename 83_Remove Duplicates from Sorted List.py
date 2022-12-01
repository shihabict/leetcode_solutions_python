# class Solution:
#     def deleteDuplicates(self, head):
#         sorted_list = []
#         for i in head:
#             if i not in sorted_list:
#                 sorted_list.append(i)
#         return sorted_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        sorted_list = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return sorted_list

if __name__ == '__main__':
    # sol = Solution()
    # print(sol.deleteDuplicates([1, 1, 2, 4, 4, 5, 6, 2]))
    head = [1, 1, 2]
    sol = Solution()
    print(sol.deleteDuplicates(head))
