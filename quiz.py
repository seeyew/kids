# QUIZ APP STARTER
# Ask questions, check answers, and keep score.
# Runs in any Python editor, no extra setup needed.

# Each question is a pair: (question, answer)
# TRY THIS: change these to your own questions!
questions = [
    ("What is 7 x 8? ", "56"),
    ("What planet is closest to the sun? ", "mercury"),
    ("How many legs does a spider have? ", "8"),
]

score = 0

print("Welcome to my quiz!")
name = input("What is your name? ")

for question, answer in questions:
    guess = input(question)
    # .lower() and .strip() so "Mercury " still counts as "mercury"
    if guess.lower().strip() == answer:
        print("Correct!")
        score = score + 1
    else:
        print("Not quite. The answer was", answer)

print(name + ", you got", score, "out of", len(questions))

# LEVEL UP IDEAS
# 1. Add 5 more questions.
# 2. Print a special message if they get a perfect score.
# 3. Ask "Play again?" and start over if they say yes.
# 4. Shuffle the questions with: import random, then random.shuffle(questions)
