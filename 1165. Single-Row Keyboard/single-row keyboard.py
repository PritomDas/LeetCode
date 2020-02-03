'''my methodology for solution
1)one good thing that I learned from this problem is that I need to read the questionmore carefully
2)I assumed "keyboard" will contain a fix string like "abscdefghijk..."
3)But actually it can differ if I would have seen example 2 carefully
'''
''' [a] I am gonna make a hashmap for all the characters and indexes of each character in "keyboard"
    [b] declare two variables, one containing time and another for initial keyboard stroke
    [c] a for loop for every "word" given and then applying the formula given on the question to measure time
'''

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {character:index for index,character in enumerate(keyboard)}
        word = keyboard[0] + word 
        time = 0

        for elem in range(len(word)-1):
            time += abs(hashmap[word[elem]] - hashmap[word[elem+1]])
        return time