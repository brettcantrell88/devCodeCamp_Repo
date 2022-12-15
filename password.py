correct_password = "Password123"
password_confirmed = False
current_attempts = 0
number_of_attempts = 5
while password_confirmed == False:
    user_password = input("Please enter your password. ")
    current_attempts += 1
    if user_password == correct_password:
        print("You've successfully logged in.")
        password_confirmed = True
    elif current_attempts == number_of_attempts:
        print("You've reached the max number of attempts, bye.")
        password_confirmed = True
    else:
        print("Incorrect password, please try again.")


