class Solution:
    def interpret(self, command):
        if '()' in command:
            command = command.replace('()','o')
        if '(al)' in command:
            command = command.replace('(al)','al')
        return command



sol = Solution()
print(sol.interpret('(al)G(al)()()G'))

