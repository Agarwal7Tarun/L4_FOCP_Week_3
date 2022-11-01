password=input("Enter Password: ")
if ((len(password)>=8)and(len(password)<=12)):
    password_check=input("Confirm Password: ")
    if password==password_check:
        print("Password Set!")
    else:  
        print("Sorry! Wrong password try again")
else:
    print("Sorry you entered less than 8 characters or more than 12 characters")
