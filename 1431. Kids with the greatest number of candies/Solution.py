# this code is giving me the output correctly

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #calling the inbuilt max function to find the largest element from the list
        MAX = max(candies)
        
        #making an empty list that will store the final answer for this problem
        output = []
        
        #comparing MAX with each element from the list candies
        #simultaneously appending either true or false based on the condition to output list
        for index in range(len(candies)):
            if candies[index] + extraCandies >= MAX:
                output.append("True")
            else:
                output.append("False")
        return output   
    
    #this code works
    class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        MAX = max(candies)
        for index in range(len(candies)):
            if candies[index] + extraCandies >= MAX:
                yield True
            else:
                yield False
