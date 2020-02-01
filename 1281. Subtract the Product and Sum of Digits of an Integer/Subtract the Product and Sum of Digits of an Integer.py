class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        #declaring the variables that I will be needing
        product_of_digits = 1
        sum_of_digits = 0
        
        #we will convert the "n" from integer to string
        for i in str(n):
            product_of_digits *= int(i)
            sum_of_digits += int(i)
        return( product_of_digits - sum_of_digits)
        
        