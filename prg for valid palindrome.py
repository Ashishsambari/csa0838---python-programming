string_value=input('enter a string :')
s=".join(filter(str.isalpha,string_value))
s=s.lower()
if(s==s[::-1]):
    print(True)
else:
    print(False)
