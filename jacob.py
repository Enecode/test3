def get_userpassword ():
    try:

        user_password = int(input("enter your password :"))
        if user_password == 12345 :
         print("Access granted")
        else :
           print("access denied")
    except ValueError :
       print("Invalid input, please enter a valid password")
       get_userpassword()
       return user_password
get_userpassword()




