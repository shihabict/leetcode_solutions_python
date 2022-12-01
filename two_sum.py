
class Solution:
    def twoSum(self, nums, target):
        count_pointer = 0
        for i in range(len(nums)):
            count_pointer+=1
            second_value = target - nums[i]
            if second_value in nums[i + 1:]:
                return [i, nums[i + 1:].index(second_value)+count_pointer]


if __name__ == '__main__':
    # nums = [2,7,11,15]
    # target = 9
    # nums = [3, 2, 4]
    # target = 6
    nums = [3, 3]
    target = 6

    sol = Solution()
    res = sol.twoSum(nums, target)
    print(res)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumval = 0
        root = curr = ListNode(0)
        while l1 or l2 or sumval:
            if l1: sumval += l1.val; l1 = l1.next
            if l2: sumval += l2.val; l2 = l2.next
            curr.next = curr = ListNode(sumval % 10)
            sumval //= 10
        return root.next


sol = Solution()
print(sol.addTwoNumbers([2,4,3], [5,6,4]))
