# this code is not giving me the output correctly

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        #making an empty list that will store the final answer for this problem
        output = []
        
        #calling the inbuilt max function to find the largest element from the list
        MAX = max(candies)
        
        #comparing MAX with each element from the list candies
        #simultaneously appending either true or false based on the condition to output list
        for elem in candies:
            if (elem + extraCandies) >= MAX:
                output.append("true")
            else:
                output.append("false")
        
        #return the final list
        return output
