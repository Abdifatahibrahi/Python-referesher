# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_in_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_in_seconds}")

# user_age_in_seconds()

friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name]
    print(f)

add_friend()
