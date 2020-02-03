test1 = "HELLO"
tes2 = "heLLo"
test3 = 12345
test4 = "Hel123O"

def lowercases(str):
    str2 = str.lower()
    return(str2)


#using the concepts of ascii and inbuilt function "ord".
#"ord" is similar to "str" inbuilt funtion. 
#"ord" converts any alphabet to it's ascii code
def toLowerCase(self, str: str) -> str:
    for c in str:
        if ord(c) < 97 and ord(c) >= 65:
            str = str.replace(c, chr(ord(c) + 32))
    return str
        
#print(lowercases(test1))
#print(toLowerCase(test1))
