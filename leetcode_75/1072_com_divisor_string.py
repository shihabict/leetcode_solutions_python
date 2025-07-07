class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd_divisor = [" "]
        if 1 <= len(str1) and len(str2) <= 1000:
            if str1.isupper() and str2.isupper():
                if len(str2) < len(str1):
                    for i in range(len(str2)+1):
                        if str2[:i] in str1 and str2:
                            gcd_divisor.append(str2[:i])
        return gcd_divisor[-1]


if __name__ == '__main__':
    gcd_string = Solution()
    divisor = gcd_string.gcdOfStrings("ABABAB", "ABAB")
    print(divisor)
