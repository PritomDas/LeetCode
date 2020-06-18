class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''The algorithm:
        1) Create new string
        2) in that string store in way such that it stores alpha num and lowercase with no spaces
        3) if the reverse of that new string is same as the created string then return true'''

        new_s = "".join(char for char in s if char.isalnum()).lower()
        return new_s == new_s[::-1]
