#solution using regluar expression
import re
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

#solution using for loop
class Solution:
    def myAtoi(self, s: str) -> int:
            if len(s) == 0: return 0
            ans = 0
            sign = 1
            number_started = False
            minNum = (-1) * (2 ** 31)
            maxNum = (2 ** 31 -1)
            
            for ch in s:
                
                if number_started == False:                    
                    if ch == ' ':
                        continue
                    if ch =='-':
                        number_started = True
                        sign = -1
                        continue
                    if ch == '+':
                        number_started = True
                        continue
                    if ch.isdigit():
                        number_started = True
                        
                if ch.isdigit():
                    ans = ans*10 + (ord(ch) - ord('0'))
                else:
                    break

            ans = sign * ans 
            
            if ans == 0:
                return 0   
            
            elif ans < minNum:
                return minNum
            
            elif ans > maxNum:
                return maxNum
            
            else:
                return ans
