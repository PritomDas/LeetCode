'''Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your 
function returns 0 when the reversed integer overflows.'''

#short and simple code
def reverse(x):
    ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
    return ans if -2**31 <= ans <= 2**31 - 1 else 0

#same code with explanation and better readability
def int_reverser(test):
    #when input is a positive integer then do the following
    if test >= 0:
        answer = int(str(test)[::-1])
    #when input is a negative integer and to preserve the negative sign and also reverse the int
    else:
        answer = -int(str(-test)[::-1])
    #if input stays within 32 bits signed integers
    if -2**31 <= answer <= 2**31 - 1:
        return answer
    #if input overflows by crossing 32 bits signed integers
    else:
        return 0

#test cases
print(int_reverser(-123))