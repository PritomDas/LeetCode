class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(x in J for x in S)
 
#print(countJewels("aAAbbbb", "aA")) this is for checking if my code works