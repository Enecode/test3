def get_userpassword():
    """
    This function prompts the user to enter a password and checks if it matches the expected password.
    If the password is correct, it prints "Access granted". Otherwise, it prints "Access denied".
    
    """
    password = int(input("Enter your password: "))
    if password == 12345:
        print("Access granted")
    else:
        print("Access denied")

get_userpassword()