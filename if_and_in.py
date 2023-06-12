# number = 7

# user_input = input("Enter 'y' if you would like to play: ").lower()

# if user_input == 'y':
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You are correct")
#     else:
#         print("you are not correct")


# number = 7

# user_input = input("Enter 'y' if you would like to play: ")

# if user_input in ('y', 'Y'):
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You are correct")
#     elif user_number - number in (1, -1):
#         print("you are off by one")
#     else:
#         print("you are not correct")

# number = 7

# user_input = input("Enter 'y' if you would like to play: ")

# if user_input in ('y', 'Y'):
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You are correct")
#     elif abs(user_number - number) == 1:
#         print("you are off by one")
#     else:
#         print("you are not correct")


number = 7

user_input = input("Would you like to play? (Y/n) ")

while user_input != "n":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You are correct")
        break
    elif abs(user_number - number) == 1:
        print("you are off by one")
    else:
        print("you are not correct")
    user_input = input("Would you like to play? (Y/n) ")