class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        '''I am going to use the sum of N natural number formula for solving this problem
        This is the approach
        1) Remember that only one number is missing
        2) The N from the formula is bsically the last number present in the given input
        3) I will use the formula to get the real sum when all numbers were present
        4) Then I will find the sum of the given numbers in the input
        5) I will assign a variable that will find the difference of the previous two steps
        6) Return the new answer
        7) Hope this works
        8) I am using int division in python as "//" so that answer does not come as float'''
        
        n = len(nums)
        ans_real = (n*(n+1))//2 
        ans_old = sum(nums)
        output = ans_real - ans_old
        return output
        
