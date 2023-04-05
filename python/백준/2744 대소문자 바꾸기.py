string = input()
string2 =''
for i in string:
    if i.isupper():
        string2 += i.lower()
    else:
        string2 += i.upper()
print(string2)