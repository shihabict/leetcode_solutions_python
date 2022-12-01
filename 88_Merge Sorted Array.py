class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(len(nums1)):
            if j >=n:
                break
            if nums1[i]==0:
                nums1[i] = nums2[j]
                j+=1
        nums1.sort()
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
