class Solution(object):
    def reverseWords(self, s):
       #making two list variables "list1" and "list2"
        list1 = s.split(" ")
        list2 = []
        for element in list1:
            list2.append(element[::-1])
            str2 = ' '.join(list2)
        return(str2)