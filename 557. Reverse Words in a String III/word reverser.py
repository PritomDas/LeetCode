string = "i love you so much"

print("reverse using splicing:-")
string2 = string[::-1]
print(string2)

print("reverse using inbuilt function:-")
string3 = reversed(string)
print("".join(string3))

print("reverse using loop:-")
string4 = ""
i = len(string)-1
while i>=0:
    string4 = string4 + string[i]
    i -= 1
print(string4)

string_splitter = string.split()
x = []
y = []
#splicing method
for char in string_splitter:
    x.append(char[::-1])
print("")
print(x)
print(" ".join(x))

#using inbuilt reversed method
for char in string:
    y.append(char[::-1])
print("new beginning")
print(y)
print(" ".join(y))