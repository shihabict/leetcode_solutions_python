from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []

        if not n:
            return self.result
        
        self.backtrack_parenthesis([],n,n,self.result)
        return self.result

    def backtrack_parenthesis(self,s,opening,closing,result):
        if opening==closing==0:
            result.append(''.join(s))

        if closing>0 and opening<closing:
            s.append(')')
            self.backtrack_parenthesis(s,opening,closing-1,result)
            s.pop()

        if opening>0:
            s.append('(')
            self.backtrack_parenthesis(s,opening-1,closing,result)
            s.pop()
        # return result





if __name__ == '__main__':
    outpt = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    n = 3
    sol = Solution()
    res = sol.generateParenthesis(n)
    print(res)