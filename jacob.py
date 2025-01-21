def get_userpassword():
    password = int(input("Enter your password: "))
    if password == 12345:
        print("Access granted")
    else:
        print("Access denied")

get_userpassword()