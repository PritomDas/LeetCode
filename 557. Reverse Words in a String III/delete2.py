#internal content reverser using reversed
string = "i love you"
list1 = string.split(" ")
list2 = []

for i in list1:
    str1 = reversed(i)
    list2.append("".join(str1))
    str2 = ' '.join(list2)
print(str2)
