MR_LEEMANS_USERNAME = 'pleeman'
MR_LEEMANS_PASSWORD = 'abcd1234'

def loginWasSuccessful():
    username = input("Hello, please enter your username: ")
    if username == MR_LEEMANS_USERNAME:
        counter = 0
        while counter < 3:
            password = input("Hello Mr. Leeman, please enter your password: ")
            if password == MR_LEEMANS_PASSWORD:
                return True
            else:
                counter = counter + 1

    return False

# main program starts here
if loginWasSuccessful():
    print("Correct username and password")
else:
    print("Incorrect username or password")
