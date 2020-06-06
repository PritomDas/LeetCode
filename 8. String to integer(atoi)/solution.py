class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        s = re.findall(r"^[+-]{0,1}[0-9]+", s)
        if not s:
            return 0
        t = int(s[0])
        if t > 2**31-1:
            return 2**31-1
        elif t < -2**31:
            return -2**31
        return t
        
'''referenece links:
1)https://docs.python.org/3/library/re.html
2)https://www.tutorialspoint.com/python/string_lstrip.htm#:~:text=Python%20string%20method%20lstrip(),string%20(default%20whitespace%20characters).
'''
