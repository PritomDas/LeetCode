nums = [10,2,20,5]

# this is the way I want to proceed
# map the numbers as strings inside the list
#find length of each elements that I converted as strings
#filter out any odd count and keep only even count
#reduce it, and say finally how many even counts were present

result = 0 #this will be the var that will carry the reduce step answer
for elem in nums:
    if (len(str(nums))%2 ==0):
        result += 1
print(result)

