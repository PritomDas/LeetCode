#Brute Force Approach: Two for loops
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count +=1
            output.append(count)
        return output
        

#Using Bisect module and sorting the array
import bisect
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            count = bisect.bisect_left(sorted_nums, nums[i])
            output.append(count)
        return output
        
        
#To understand the concept of bisect I have used this helpful video:
[https://www.youtube.com/watch?v=Aw0plPtbPmU]
