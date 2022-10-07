def is_valid(_user_input):
    return _user_input is not None and _user_input.isdigit() and 1 <= int(_user_input) <= 3


def choice(_user_input):
    print(f"Your choice: {_user_input}")


def is_not_one(_user_input):
    return _user_input != "1"


user_input = None
while not is_valid(user_input):
    user_input = input("Enter a number between 1 and 3: ")

choice(user_input)
if not is_not_one(user_input):
    print("Your choice doesn't fit between the interval [2, 3]")
else:
    print("Your choice fits between the interval [2, 3]")
