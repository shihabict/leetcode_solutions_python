# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        if isBadVersion(1):
            return 1
        if isBadVersion(j) and not isBadVersion(j - 1):
            return j
        while i < j:
            mid = (i + j) // 2
            ch1 = isBadVersion(mid)
            ch2 = isBadVersion(mid - 1)
            if ch1 and not ch2:
                return mid
            if not ch1:
                i = mid
            if ch2:
                j = mid


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        if isBadVersion(1):
            return 1
        if isBadVersion(j) and not isBadVersion(j - 1):
            return j
        while i < j:
            mid = (i + j) // 2
            ch1 = isBadVersion(mid)
            ch2 = isBadVersion(mid - 1)
            if ch1 and not ch2:
                return mid
            if not ch1:
                i = mid
            if ch2:
                j = mid
