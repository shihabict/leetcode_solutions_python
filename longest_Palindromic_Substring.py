class Solution:
    def longestPalindrome(self, s):
        result = ['']
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    if result and len(result[-1]) < len(s[i:j]):
                        result.append(s[i:j])
        result.remove('')
        return max(result, key=len)

    def longestPalindrome2(self, s):
        if len(s)<=1:
            return s
        else:
            p = ''
            for i in range(len(s)):
                p1 = self.get_palindrome(s, i, i)
                if len(p1)>len(p): p = p1
                p1 = self.get_palindrome(s, i, i + 1)
                if len(p1) > len(p): p = p1
            return p

    def get_palindrome(self, s, left_p, right_p):
        while left_p >= 0 and right_p < len(s) and s[left_p] == s[right_p]:
            left_p -= 1
            right_p += 1
        return s[left_p + 1:right_p]


if __name__ == '__main__':
    # s = "babad"
    # s = "cbbd"
    s = "bb"
    # s = "boqylncwfahjzvawrojyhqiymirlkfzkhtvmbjnbfjxzewqqqcfnximdnrxtrbafkimcqvuprgrjetrecqkltforcudmbpofcxqdcirnaciggflvsialdjtjnbrayeguklcbdbkouodxbmhgtaonzqftkebopghypjzfyqutytbcfejhddcrinopynrprohpbllxvhitazsjeyymkqkwuzfenhphqfzlnhenldbigzmriikqkgzvszztmvylzhbfjoksyvfdkvshjzdleeylqwsapapduxrfbwskpnhvmagkolzlhakvfbvcewvdihqceecqhidvwecvbfvkahlzlokgamvhnpkswbfrxudpapaswqlyeeldzjhsvkdfvyskojfbhzlyvmtzzsvzgkqkiirmzgibdlnehnlzfqhphnefzuwkqkmyyejszatihvxllbphorprnyponircddhjefcbtytuqyfzjpyhgpobektfqznoatghmbxdouokbdbclkugeyarbnjtjdlaisvlfggicanricdqxcfopbmducroftlkqcertejrgrpuvqcmikfabrtxrndmixnfcqqqwezxjfbnjbmvthkzfklrimyiqhyjorwavzjhafwcnlyqob"
    sol = Solution()
    max_pal = sol.longestPalindrome2(s)
    print(max_pal)
