def get_userpassword():
    try:

        user_password = (input("enter your password : "))
        if user_password == 123456 :
            print("access granted")
        else :
            print("access denied")
    except ValueError :
        print("invalid input, enter a valid password")
    except Exception as e :
        print("an error occurred :", e)
        get_userpassword()
        return user_password
get_userpassword()
