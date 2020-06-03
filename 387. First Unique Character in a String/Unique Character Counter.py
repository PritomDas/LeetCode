import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
    
    
    #another solution
    
    from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        #converting into lowercase
        s = s.lower()
        
        #converting into a string type to list
        s = list(s)
        
        #setting a counter map to count occurence of each character
        counterMap = Counter(s)
        
        '''in the countermap: count 0 = no occurence of that alphabet
                              count 1 = that character appeared only once
                              count >1 = multpile occurence of that character'''
        for idx,char in enumerate(s):
            if counterMap[char] == 1:
                return idx
        return -1
