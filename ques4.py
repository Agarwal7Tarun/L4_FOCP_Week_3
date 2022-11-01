BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password=input("Enter password: ")
if password in BAD_PASSWORDS:
    print("You cannot have this password!")
else:
    password_check=input("Confirm Password: ")
    if password==password_check:
        print("Password Set!")
    else:  
        print("Sorry! Wrong password try again")