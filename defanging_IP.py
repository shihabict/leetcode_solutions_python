class Solution:
    def defangIPaddr(self, address):
        address = address.split('.')
        return "[.]".join(address)



sol = Solution()
print(sol.defangIPaddr("255.100.50.0"))