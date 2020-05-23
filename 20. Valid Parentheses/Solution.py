#Approach 1 : Stack (this I tried to implement by using the explanation by Sachin 
#https://www.youtube.com/watch?v=3tCDOo-HwZo
class Solution:
    def isValid(self, s: str) -> bool:
        #the algorithm
        '''I will use stack data structure
        every open brackets will be pushed in stack
        every close brackets will be popped out of the stack
        during every pop, I will compare the popped elem with the last elem in the stack
        if they form pair then continue checking others orelse just return false'''
        
        #making a stack object
        # or maybe even an empty list might work
        mystack = []
        
        #boolean flag
        balanced = True
        
        #to keep track of index for the stack
        index = 0
        
        while index < len(s) & balanced:
            #this gets the current element stored inside the index location
            elem = s[index]
            
            #if the current elem is anywhere same as the open brackets...
            if elem in "([{" :
                #then push inside stack
                mystack.push(elem)
            #if current elem is not in open brackets then do the following conditions...
            else :
                #if our given string itself is empty
                if s.empty() :
                    #set the flag to false
                    balanced = False
                    
                #assuming its not empty, neither is a fall bracket then pop out the last entry in stack
                #also storing this popped elem inside a variable
                else :
                    top = mystack.pop()
                    
                    '''calling the "pair" function to compre between this "top" and the latest closed bracket that I have encountered'''
                    if not pair(top, elem):
                        balanced = False
            #now check for all other indexes
            index += 1
            
            #after all this process if we reach an empty stack while flag was true throughout the process
        if mystack.empty() :
            return True
        else :
            return False
            

#this is the "pair" function to check between the top and the current elem
def pair(elem1 , elem2) :

    #() pair formation
    if elem1=="(" & elem2==")":
        return True

    #[] pair formation
    elif elem1=="[" & elem2== "]":
        return True

    #{} pair formation
    elif elem1=="{" & elem2=="}":
        return True
        
        
 #The code still needs to be debugged 
 
 
 #another variant which is more intuitve by using dictionary as a hash map concept
 class Solution:
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
 
