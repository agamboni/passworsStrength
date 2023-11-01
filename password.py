import string

password= input("enter your password: ")
passwordStrength=0
if len(password)>7:
    passwordStrength+=30

contains_uppercase= any(char.isupper() for char in password)
if contains_uppercase:
     passwordStrength+=10

contains_lowercase= any(char.islower() for char in password)
if contains_lowercase:
    passwordStrength+=10

contains_number= any(char.isdigit() for char in password)
if contains_number:
    passwordStrength+=10

for c in password:
    if c in string.punctuation:
        passwordStrength+=10
        break

with open("/Users/agamboni/Desktop/count/100-most-common-passwords.txt", "r") as file:
    passwordList= file.read().splitlines()
hasKey=0
for i in passwordList:
    if i in password:
        hasKey+=1
if hasKey==0:
    passwordStrength+=30
    
print(passwordStrength)
if passwordStrength<40:
    print("weak password")
if 70>passwordStrength>40:
    print("medium password")
if passwordStrength==100:
    print("strong password")