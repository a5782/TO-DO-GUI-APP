password = input("enter a password : ")
#result = []
result = {}
digit = False
uppercase = False
if len(password)>=8:
    #result.append(True)
     result["length"] = True
else:
    #result.append(False)
    result["length"] = False
for i in password:
    if i.isdigit():
        digit = True
#result.append(digit)
result["digit"] = digit
for j in password:
    if j.isupper():
        uppercase = True
#result.append(uppercase)
result["uppercase"] = uppercase
print(result)
print(all(result))
'''
if all(result):
    print("Password is strong")
else:
    print("Password is weak")
'''
if all(result.values()):
    print("Password is strong")
else:
    print("Password is weak")

