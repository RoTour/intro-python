userInput = None
numbers = []


def print_list(to_print):
  print(f"Current list: {str(to_print)}")


while userInput != "q":
  userInput = input("Enter a number or q to quit: ")
  if userInput != "q":
    try:
      userInput = int(userInput)
    except ValueError:
      print("Not a valid input")
      continue

    if userInput in numbers:
      print("This number is already in the list")
      print_list(numbers)
      continue

    numbers.append(int(userInput))
    print(f"Adding {userInput} to list.")
    print_list(numbers)
