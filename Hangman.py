import random

words = ["banana", "minion", "orange", "pineapple"]

word = random.choice(words)
game = ["-" for i in word]
tries = 4
while tries > 0:
    if "-" in game:
        print("Enter your guess")
        guess = str(input())
        rightGuess = False
        if len(guess) > 1:
            print("Only enter a single letter")
        i = 0
        for a in word:
            if a == guess:
                game[i] = a
                rightGuess = True
                i += 1
            else:
                i += 1
                continue

        if not rightGuess:
            tries -= 1

        print(''.join(game))
    else:
        print("You Win")
        break

if tries <= 0:
    print("You Lose")
            
