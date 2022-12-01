from decimal import Decimal


class Solution:
    def str_to_int(self, s):
        s = s.strip()
        hi = 0
        index = 0
        sign = 1
        if s[0]=='-':
            sign = -1
            index+=1
        elif s[0]=="+":
            sign = 1
            index+=1

        while index<len(s) and s[index].isdigit():
            hi = hi*10+ord(s[index])-ord('0')
            index+=1
        res = hi*sign
        if res in range(-2147483648, 2147483648):
            return res
        elif res < -2147483648:
            return -2147483648
        else:
            return 2147483648-1


if __name__ == '__main__':
    s = "    -42"
    str_int = Solution()
    print(str_int.str_to_int(s))
