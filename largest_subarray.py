class LongestSubString:
    def large_sub_String(self, s):
        sub_string_list = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = (s[i:j])
                print(0)
        return sub_string_list


if __name__ == '__main__':
    s = 'abcda'
    long_array = LongestSubString()
    print(long_array.large_sub_String(s))
    print(len(long_array.large_sub_String(s)))
