username= input("Enter a username: ")

number_of_strings= len(username)

number_of_spaces= username.count(" ")

number_of_digits= username.isdigit()

if number_of_strings>12 or number_of_spaces>0 or number_of_digits>0:
    print("Invalid username")

else:
    print("Username confirmed!")    