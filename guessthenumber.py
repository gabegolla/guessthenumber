import random
max_attempts = 10
attempts = 0
difficulty_level = {
    'easy': 30,
    'normal': 60,
    'hard': 100
}
level = (input(f"First choose difficulty level: ")).lower()
number = random.randint(1, difficulty_level.get(level))
attempt_fails = {
    3: f"Don't give up! This is a number between {(number - 10)} and {(number + 10)}." if number > 10 else f"Don't give up! This number is lower than {(number + 10)}.",
    6: f"Maybe it's a bit too hard! This is a number between {(number - 5)} and {(number + 5)}." if number > 5 else f"Maybe it's a bit too hard! This number is lower than {(number + 5)}.",
    8: f"I thought it would be faster... This is a number between {(number - 2)} and {(number +2)}." if number > 2 else f"I thought it would be faster... This is a number between {(number - 2)} and {(number +2)}."
}
user_number = int(input(f"I'm thinking about the number between 1 and {difficulty_level[level]}... Can you guess in {max_attempts} attempts? "
                        "Please type an integer:"))
for attempt in range(1, max_attempts + 1):
    if user_number < number:
        print(f"Nope, {user_number} is toooo low!")
    elif user_number > number:
        print(f"Nope, {user_number} is toooo big!")
    else:
        print(f"Yup, I was thinking about {user_number}! Congratulations, you needed {attempts} attempts to guess.")
        exit(0)
    fail_message = attempt_fails.get(attempt, 'Loading next try...')
    print(fail_message)
    user_number = int(input("Guess one more time: "))
print("Sorry... Maybe next time you will guess!")
