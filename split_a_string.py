class Solution:
    def balancedStringSplit(self, s):
        result = 0
        counter = 0
        for char in s:
            if char == "R":
                counter+=1
            if char == "L":
                counter -=1
            if counter == 0:
                result+=1
        return result

        # while len(s)>0:
        #     s = s[1:]
        #     print(s)
        #     print(s.count("R"))
        #     print(s.count("L"))
        #     if s.count("R") == s.count("L"):
        #         result+=1
        return result

sol = Solution()
print(sol.balancedStringSplit('RLRRLLRLRL'))
