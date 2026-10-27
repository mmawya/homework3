password = input("enter your password:")

if (len(password)>= 8 and
    any(char.isdigit() for char in password) and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(not char.isalnum() for char in password)):

    print("strong password.")
else:
    print("weak password.")