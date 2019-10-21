class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result, count = 0, 0      
        for c in s:
            if c == 'L':
              count += 1   
            elif c == 'R':
                count-=1
                
            if count == 0:
                result += 1
                
        return result