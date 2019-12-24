#internal content reverser using splicing
string = "i love you"
l = string.split(" ")
l1 = []
for element in l:
    l1.append(element[::-1])
    string_variable = " ".join(l1)
print(string_variable)