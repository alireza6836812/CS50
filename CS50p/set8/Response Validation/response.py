import validators

myinput = input("What's your email address? ")
myinput = validators.email(myinput)
if myinput:
    print("Valid")
else:
    print("Invalid")
