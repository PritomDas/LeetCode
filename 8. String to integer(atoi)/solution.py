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
            
            
  #similar to the solution of used in the first approach,also make sure to watch the refernce videos of this solution 
MAPPING = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}

MAX_INT = 2**31-1
MIN_INT = -(2**31)

class Solution:
    def myAtoi(self, string: str) -> int:
        s = string.lstrip(' ')
        if not s:
            return 0
        
        sign = -1 if s[0] == "-" else 1
        if sign != 1 or s[0] == "+":
            s = s[1:]
            
        res = 0
        for c in s:
            if c not in MAPPING:
                return self.limit(res * sign)
            
            res *= 10
            res += MAPPING[c]
            
        return self.limit(res * sign)
    
    def limit(self, x: int) -> int:
        if x > MAX_INT:
            return MAX_INT
        if x < MIN_INT:
            return MIN_INT
        return x
    
    #https://www.youtube.com/watch?v=qxIprnPrVZA
