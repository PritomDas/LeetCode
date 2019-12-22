class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u"]
        s1 = "" #declaring an empty variable that will contain the modified string
        
        '''looping between every character in "S" and cross check if those aren't also            present in "vowels" and printing only those characters'''
        for characters in S:
            if characters not in vowels:
                s1 += characters
        return(s1)