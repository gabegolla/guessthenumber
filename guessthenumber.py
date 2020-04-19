import random
number = random.randint(1, 100)
attempts = 0

user_number = int(input("I'm thinking about the number between 1 and 100... Can you guess it? Pleas type an integer:"))

while number != "guess":
    if user_number < number:
        print(f"Nope, {user_number} is toooo low!")
    elif user_number > number:
        print(f"Nope, {user_number} is toooo big!")
    else:
        print(f"Yup, I was thinking about {user_number}! Congratulation, you needed {attempts} attempts to guess.")
        break
    attempts += 1
    if attempts == 3 and number <= 10:
        print(f"Don't give up! This number is lower than {(number + 10)}.")
    elif attempts == 3:
        print(f"Don't give up! This is a number between {(number - 10)} and {(number + 10)}.")
    elif attempts == 6 and number <= 5:
        print(f"Maybe it's a bit too hard! This number is lower than {(number + 5)}.")
    elif attempts == 6:
        print(f"Maybe it's a bit too hard! This is a number between {(number - 5)} and {(number + 5)}.")
    elif attempts == 12 and number <= 2:
        print(f"I thought it would be faster... This number is lower than {(number + 2)}.")
    elif attempts == 12:
        print(f"I thought it would be faster... This is a number between {(number - 2)} and {(number +2)}.")
    user_number = int(input("Try one more time: "))
